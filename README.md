python-package-boilerplate
==========================

[![Build Status](https://travis-ci.org/mtchavez/python-package-boilerplate.png?branch=master)](https://travis-ci.org/mtchavez/python-package-boilerplate)

CLI tool to use ChatGPT API.

## Installation

pip install git+https://github.com/belyak/gptizecli.git@master

## Usage

Install your API key:
```shell
gptcli.sh save-api-key YOUR-API-KEY
```

Prompt the model

```shell
gptcli.sh prompt "What is the distance between Moscow and Saint-Petersburg, Russia?"

```

would produce:

```shell
The distance between Moscow and Saint-Petersburg, Russia is approximately 645 kilometers (401 miles).
```

To include the prompt in the output, use `--echo` flag:

```shell
gptcli.sh prompt --echo "What is the distance between Moscow and Saint-Petersburg, Russia?"
```

```shell
What is the distance between Moscow and Saint-Petersburg, Russia?
The distance between Moscow and Saint-Petersburg, Russia is approximately 645 kilometers (401 miles). 
```
