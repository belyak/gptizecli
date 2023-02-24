#!/usr/bin/env python
import configparser

import click
import openai
import os

from openai.error import AuthenticationError

# Set up OpenAI API credentials
openai.api_key = os.environ.get("OPENAI_API_KEY")


DEFAULT_CONFIG_PATH = os.path.join(os.path.expanduser('~'), '.gptizecli')

@click.group()
def cli():
    pass


@cli.command()
@click.argument('prompt',
                type=str)
@click.option('--echo', is_flag=True, default=False)
@click.option('--model',
              default='text-davinci-003',
              help='GPT-3 model to use')
@click.option('--temperature',
              default=0,
              help='Temperature parameter for sampling')
@click.option('--max_tokens',
              default=1024,
              help='Maximum number of tokens to generate')
@click.option('--config', default=DEFAULT_CONFIG_PATH,
              help='Configuration file to save the API key')
def prompt(prompt, echo, model, temperature, max_tokens, config):
    # Create configuration file if it doesn't exist
    config_parser = configparser.ConfigParser()
    config_parser.read(config)

    if not config_parser.has_section('openai'):
        config_parser.add_section('openai')
        click.echo("Please set your OpenAI API key using the "
                   "`save-api-key` command", color=True)
        exit(0)
    else:
        api_key = config_parser.get('openai', 'api_key')

    # Generate text using OpenAI API
    try:
        openai.api_key = api_key
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        # Print response
        if echo:
            click.echo(prompt, color=True)
        click.echo(response.choices[0].text.strip(), color=True)
    except AuthenticationError as e:
        click.echo('Error: {}'.format(e), color=True)
        click.echo('Please set your OpenAI API key using the '
                   '`save-api-key` command', color=True)


@cli.command()
@click.argument('key', type=str)
@click.option('--config', default=DEFAULT_CONFIG_PATH,
              help='Configuration file to save the API key')
def save_api_key(key, config):
    # Create configuration file if it doesn't exist
    config_parser = configparser.ConfigParser()
    config_parser.read(config)
    if not config_parser.has_section('openai'):
        config_parser.add_section('openai')

    # Save API key to configuration file
    config_parser.set('openai', 'api_key', key)
    with open(config, 'w') as config_file:
        config_parser.write(config_file)


if __name__ == '__main__':
    cli()
