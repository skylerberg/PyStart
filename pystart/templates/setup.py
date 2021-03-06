from setuptools import setup, find_packages
from os.path import join, dirname

import {{ project }}


setup(
    name='{{ project }}',
    version={{ project }}.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    )
