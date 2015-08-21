"""PyStart - Don't waste your time on boilerplate

Usage:
  pystart [options] <name>

Options:
  -h --help             Show this screen.
  --destroy-everything  Destroy repo locally and remotely.
  --all                 Equivalent to '--github'.
  --github              Put the new project on GitHub.
"""

import os
import sys

import git
from jinja2 import Environment, PackageLoader
from docopt import docopt

import pystart.github


__version__ = "0.0.1"

ENV = Environment(loader=PackageLoader('pystart', 'templates'))
PROJECT_NAME = ""


def get_project_name():
    return PROJECT_NAME


def get_template_to_file_mapping():
    project = get_project_name()
    return {
        "LICENSE": "LICENSE",
        "README.md": "README.md",
        "setup.py": "setup.py",
        ".gitignore": ".gitignore",
        "__init__.py": "%s/__init__.py" % project,
    }


def make_directories():
    project_name = get_project_name()
    os.mkdir(project_name)
    os.mkdir(os.path.join(project_name, project_name))
    os.mkdir(os.path.join(project_name, "tests"))


def init_repo():
    project_dir = os.getcwd()
    return git.Repo.init(project_dir)


def build_files():
    project = get_project_name()
    template_to_file = get_template_to_file_mapping()
    for src, dest in template_to_file.iteritems():
        template = ENV.get_template(src)
        content = template.render(project=project)
        with open(dest, 'w') as file:
            file.write(content)


def commit_files(repo):
    files = get_template_to_file_mapping().values()
    for file in files:
        repo.index.add([file])
    repo.index.commit("Create initial files with PyStart")


def main():
    options = docopt(__doc__, help=True)
    global PROJECT_NAME
    PROJECT_NAME = options['<name>']
    if options['--destroy-everything']:
        pystart.github.teardown_project(get_project_name())
        return
    if options['--all']:
        options['--github'] = True
    make_directories()
    os.chdir(get_project_name())
    repo = init_repo()
    build_files()
    commit_files(repo)
    if options['--github']:
        pystart.github.create_project(get_project_name())
        pystart.github.push_to_github(get_project_name(), repo)


if __name__ == "__main__":
    main()
