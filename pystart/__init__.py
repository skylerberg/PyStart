import os
import sys

import git
from jinja2 import Environment, PackageLoader


__version__ = "0.0.1"

ENV = Environment(loader=PackageLoader('pystart', 'templates'))


def get_project_name():
    return sys.argv[1]


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
    make_directories()
    os.chdir(get_project_name())
    repo = init_repo()
    build_files()
    commit_files(repo)


if __name__ == "__main__":
    main()
