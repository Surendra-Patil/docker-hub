# -*- encoding: utf-8 -*-
EPILOG = 'Docker Hub in your terminal'
DESCRIPTION = 'Access docker hub from your terminal'
HELPMSGS = {
 'method': 'The api method to query {%(choices)s}',
 'orgname': 'Your orgname',
 'reponame': 'The name of repository',
 'username': 'The Docker Hub username',
 'format': 'You can dispaly results in %(choices)s formats',
 'page': 'The page of result to fetch',
 'status': 'To query for only builds with specified status'
}
VALID_METHODS = ['repos', 'tags', 'builds', 'users', 'queue', 'version']
VALID_DISPLAY_FORMATS = ['table', 'json']
DOCKER_AUTH_FILE = '~/.docker/config.json'
CONFIG_FILE = '~/.docker-hub/config.json'
DOCKER_HUB_API_ENDPOINT = 'https://hub.docker.com/v2/'
PER_PAGE = 15

BUILD_STATUS = {
    -4: 'canceled',
    -2: 'exception',
    -1: 'error',
    0: 'pending',
    1: 'claimed',
    2: 'started',
    3: 'cloned',
    4: 'readme',
    5: 'dockerfile',
    6: 'built',
    7: 'bundled',
    8: 'uploaded',
    9: 'pushed',
    10: 'done'
}
