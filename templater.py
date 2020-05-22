#!/usr/bin/env python

import re
import sys
import os
import click
from jinja2 import TemplateSyntaxError, TemplateNotFound, UndefinedError, Environment, FileSystemLoader


def exit_with_error(msg):
    click.secho("Error: %s" % msg)
    exit(128)


def set_environment(env_file):
    """ Set environment variables from .env file """
    reg = re.compile('(?P<name>\w+)(=(?P<value>.+))')
    try:
        for line in open(env_file):
            m = reg.match(line)
            if m:
                name = m.group('name')
                value = ''
                if m.group('value'):
                    value = m.group('value')
                os.environ[name] = value
    except IOError as e:
        exit_with_error("Opening environment file: %s" % e)


def render(template, output):
    loader = FileSystemLoader(searchpath=os.path.dirname(template), followlinks=True)
    environment = Environment(loader=loader)
    try:
        template = environment.get_template(os.path.basename(template))
    except TemplateNotFound as e:
        exit_with_error('Template not found')
    except TemplateSyntaxError as e:
        exit_with_error("Template syntax: %s" % e)

    try:
        output = template.render(os.environ)
    except UndefinedError as e:
        raise Exception(e)
    else:
        return output


@click.command()
@click.option('--template', required=True, help="Input template file")
@click.option('--output', default='-', help="Rendered Output file")
@click.option('--env-file', help='Environment File (Context)', envvar='ENV_FILE')
def main(env_file, template, output):

    if env_file is not None:
        set_environment(env_file)

    content = render(template, output)

    if output == '-':
        sys.stdout.write(content)
    else:
        with open(output, 'w') as f:
            f.write(content)

if __name__ == '__main__':
    main()
