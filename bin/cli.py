import click
from templates import defgen, shadow, create
# from command2 import command2
from context import cli_context

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = cli_context()

cli.add_command(defgen)
cli.add_command(shadow)
cli.add_command(create)