from setuptools import setup, find_packages
from os.path import join, dirname

import pystart


setup(
    name='pystart',
    version=pystart.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts': ['pystart = pystart:main']
        },
    install_requires=[
        "jinja2",
        "GitPython",
        ],
    )
