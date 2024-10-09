import click

@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.echo("Hello from CloudMesh!")

def main():
    cli()

if __name__ == "__main__":
    main()
