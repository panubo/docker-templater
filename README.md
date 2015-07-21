# Templater

Simple templating with environment variables for [Docker](http://docker.io) using [Jinja2](http://jinja.pocoo.org) templates.

## Usage

All environment variables are available within the template context. If 
you specify `--env-file` then those variables will be loaded in addition to 
the current system environment.


```
Usage: templater.py [OPTIONS]

Options:
  --template TEXT  Input template file  [required]
  --output TEXT    Rendered Output file
  --env-file TEXT  Environment File (Context)
  --help           Show this message and exit.
```
