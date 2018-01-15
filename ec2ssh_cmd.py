#!/bin/env python3
import os
import asyncio

from ec2ssh_py.ec2ssh import EC2SSH

import click
import click_completion
click_completion.init()

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = EC2SSH()

@cli.command()
@click.option('--dotfile', default='~/.ec2ssh')
@click.pass_obj
def init(obj, dotfile):
    obj.dotfile = dotfile
    obj.init_cmd()

@cli.command()
@click.pass_obj
def update(obj):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(obj.update_cmd(loop=loop))
    

@cli.command()
@click.pass_obj
def remove(obj):
    pass

@cli.command()
@click.argument('shell', type=str, default='bash')
def autocomplete_install(shell):
    click.echo(click_completion.get_code(shell))

if __name__ == '__main__':
    cli()