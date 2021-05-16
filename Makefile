EMAIL = $1
USER_NAME = $2
GIT_TOKEN=

config:
	git config --global user.email EMAIL
	git config --global user.name USER_NAME
	git remote set-url origin https://username:token@github.com/nanaones/test-git

lint:
	black .
	flake8 .
