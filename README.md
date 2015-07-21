# Enviro Templater

Simple templating with environment variables for Docker using Jinja2.

## Usage

All environment variables are available within the template context. If 
you specify a `--env-file` these variables will be loaded in addition to 
the current environment.


```
./templater.py --help
Usage: templater.py [OPTIONS]

Options:
  --template TEXT  Input template file  [required]
  --output TEXT    Rendered Output file
  --env-file TEXT  Environment File (Context)
  --help           Show this message and exit.
```
