python-package-boilerplate
==========================

[![Build Status](https://travis-ci.org/mtchavez/python-package-boilerplate.png?branch=master)](https://travis-ci.org/mtchavez/python-package-boilerplate)

CLI tool to use ChatGPT API.

## Installation


## Usage

```shell
(gptizecli) $ gptizecli/gptizecli.py save-api-key YOUR-API-KEY
(gptizecli) $ gptizecli/gptizecli.py prompt "What is the distance between Moscow and Saint-Petersburg, Russia?"
The distance between Moscow and Saint-Petersburg, Russia is approximately 645 kilometers (401 miles).
(gptizecli) $ gptizecli/gptizecli.py prompt --echo "What is the distance between Moscow and Saint-Petersburg, Russia?"
What is the distance between Moscow and Saint-Petersburg, Russia?
The distance between Moscow and Saint-Petersburg, Russia is approximately 645 kilometers (401 miles). 
```

## Requirements

Package requirements are handled using pip. To install them do

```
pip install -r requirements.txt
```

## Tests

Testing is set up using [pytest](http://pytest.org) and coverage is handled
with the pytest-cov plugin.

Run your tests with ```py.test``` in the root directory.

Coverage is ran by default and is set in the ```pytest.ini``` file.
To see an html output of coverage open ```htmlcov/index.html``` after running the tests.

## Travis CI

There is a ```.travis.yml``` file that is set up to run your tests for python 2.7
and python 3.2, should you choose to use it.
