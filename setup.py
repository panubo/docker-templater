from setuptools import setup, find_packages


VERSION = '0.0.2'

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("Warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(
    name='templater',
    version=VERSION,
    description='Panubo Templater',
    long_description=read_md('README.md'),
    author='Andrew Cutler',
    author_email='andrew@panubo.com',
    url='https://github.com/panubo/templater',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: System :: Clustering',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Installation/Setup',
        'Topic :: Utilities'
    ],
    scripts=['templater.py'],
    install_requires=['click', 'jinja2'],
)
