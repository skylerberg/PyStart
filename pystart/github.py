import json

import requests

import pystart.config


def get_auth():
    config = pystart.config.get_config()
    user = config['github']['username']
    password = config['github']['password']
    return (user, password)


def create_project(project_name):
    requests.post("https://api.github.com/user/repos",
                  data=json.dumps({"name": project_name}),
                  auth=get_auth())


def teardown_project(project_name):
    user, password = get_auth()
    url = "https://api.github.com/repos/%s/%s" % (user, project_name)
    requests.delete(url, auth=(user, password))


def push_to_github(project_name, repo):
    user, _ = get_auth()
    origin = "git@github.com:%(user)s/%(repo)s.git" % {
        "user": user,
        "repo": project_name,
    }
    repo.create_remote('origin', origin)
    repo.git.push('-u', 'origin', 'master')
