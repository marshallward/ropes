"""setup.py
   ========
   Installation script for ropes

   Additional configuration settings are in ``setup.cfg``.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

project_name = 'ropes'
project_version = __import__(project_name).__version__
project_readme_fname = 'README.rst'

with open(project_readme_fname) as f:
    project_readme = f.read()

setup(
    name = project_name,
    version = project_version,
    description = 'A Python implementation of the Rope data structure',
    long_description = project_readme,
    author = 'Marshall Ward',
    author_email = 'ropes@marshallward.org',
    url = 'http://github.com/marshallward/ropes',

    #packages = ['ropes'],
    py_modules = ['ropes'],

    classifiers = [
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ],

    keywords = ['ropes', 'rope', 'string'],
)
