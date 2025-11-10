# this spellbook contains a collection of commands that can be used in the see-elle-eye 

import click 
from .magic import poly_add 

@click.group()  
def see_elle_eye():
    pass

@see_elle_eye.command()
def elena():
    click.echo("hey there")

@see_elle_eye.command()
@click.option("--pee")
@click.option("--queue")
def add(pee, queue):
    click.echo(poly_add(pee,queue))

