#!/usr/bin/env python
import os
import click
from flask.cli import FlaskGroup
from dotenv import load_dotenv

load_dotenv()
APP_FOLDER = 'app'


def create_app(info):
    from app import create_app
    return create_app(os.environ.get('CONFIG') or 'default')


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    """This is a management script for the web application."""
    pass


@cli.command()
@click.option('--all', is_flag=True)
@click.option('--stats', is_flag=True)
def lint(all, stats):
    """Run the linter."""
    if all:
        click.echo('Running linter (including skeleton code).')
        args = ['flake8', '.']
    else:
        click.echo('Running Linter...')
        args = ['flake8', APP_FOLDER]

    if stats:
        args.extend(['--statistics', '-qq'])

    exit_code = os.system(' '.join(args))

    raise SystemExit(exit_code)


@cli.command()
def deploy():
    """Deploy application."""
    from flask_migrate import upgrade

    # Migrate database to latest revision.
    upgrade()


if __name__ == '__main__':
    cli()
