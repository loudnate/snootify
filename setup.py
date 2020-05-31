from setuptools import setup, find_packages

long_description ='''snootify
Requires the following configuration files in the user's $HOME directory:

## .pushoverrc
```
[Default]
user_key = <user_key>
api_token = <api_token>
```

## .snoo_config
```
[default]
update_interval = 60

[auth]
username = <username>
password = <password>
```
Note: you can run the `$ snoo` command once to generate `.snoo_config`
'''

requires = ['snoo', 'python-pushover', 'Arrow']

__version__ = 0.1

setup(
    name='snootify',
    version=__version__,
    url='https://github.com/loudnate/snootify',
    # download_url='',
    license='MIT',
    author='Nathan Racklyeft',
    author_email='loudnate+pypi@gmail.com',
    description='snootify',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=requires,
    test_suite='tests',
    entry_points = {
       'console_scripts': ['snootify=snootify:run'],
    },
)