# Snootify

Snootify is a simple python utility with a command-line interface to send a notification via Pushover based on the current level of the SNOO rocker. 

It relies on the [SNOO](https://github.com/maebert/snoo) and [python-pushover](https://github.com/Thibauth/python-pushover) libraries. 

# Usage

Send a notification if the SNOO is the Soothing state:
```sh
$ snootify send
```

Customize which level triggers a notification:
```sh
$ snootify send --level Asleep
$ snootify send --level 2
```

# Installation

### Pushover

Configure your [Pushover](https://pushover.net/api) application, and create a `.pushoverrc` file in the user's Home directory.

```
[Default]
user_key = USERKEY
api_token = APITOKEN
```

[More documentation on configuring the python-pushover library can be found here.](https://github.com/Thibauth/python-pushover#configuration)

### SNOO

Login details for your HappiestBaby account are stored in the `.snoo_config` file in the user's Home directory. You can create this file manually, or it will be created for you on first run.

```
[default]
update_interval = 60

[auth]
username = USERNAME
password = PASSWORD
token = TOKEN_EXAMPLE
refresh_token = REFRESH_TOKEN_EXAMPLE
```

### Python package

Snootify isn't up on Pypi at this time. You can use `easy_install` to install the sources to your python `site-packages` and `bin` directories.

```sh
$ python setup.py install
```
