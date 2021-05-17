EMAIL = $1
USER_NAME = $2
GIT_TOKEN = $3
REPO_NAME = $4


config:
	git config --global user.email EMAIL
	git config --global user.name USER_NAME
	git remote set-url origin https://USER_NAME:GIT_TOKEN@github.com/USER_NAME/REPO_NAME

lint:
	black .
	flake8 .

build:
	