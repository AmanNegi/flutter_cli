import click
import re
import json
import subprocess
import os

@click.group()
@click.option('--file',help="Enter a file name")
def cli(file):
    print("GROUP");
    pass


@cli.command("generate")
@click.option('--gpt',default= 0, help='Generate Page Template')
@click.option('--assets', default=0,help='Page Template')

def main(gpt, assets):
    print( gpt, assets)

@cli.command("help")
def help():
    """Show the help menu for the program."""
    with click.Context(main) as ctx:
        click.echo(main.get_help(ctx))
    print("ABC");
    
@cli.command("shadow")
@click.option('--file',required=True, help="The file you want to generate into")
@click.option('--line',default=0, help="Specific Line you want to generate into")
def shadow(file, line):
    print(file, line);
    with open(file, 'r+') as file:
        # Get Data from JSON File first
        shadow = '';
        with open('data.json', 'r') as f:
            data = json.load(f)
            f.close();
            shadow= data['shadow']

        if(file.readable() and not file.read(1)):
            file.write(shadow);
        else:
            lines= file.readlines();
            lines[line] = shadow;
            file.seek(0);
            file.writelines(lines);
            file.truncate();
        file.close();
        print("Added Code to your file")

@cli.command("clearComments")   
@click.option('--file', required=True, help="File to remove comments from")
def clearComments(file):
    print("Removing Comments from %s" %file)
    with open(file, 'r') as f:
     lines = f.readlines()
     f.close()
    # Remove comments from each line
    new_lines = []
    for line in lines:
        new_line = re.sub(r'//.*|/\*[\s\S]*?\*/', '', line)
        new_lines.append(new_line);

    # Write the modified lines back to the file
    with open(file, 'w') as f:
     f.writelines(new_lines) 
     f.close()

    subprocess.run(['dart format', '', file])
    print("Removed All Comments")  

if __name__ == "__main__":
    cli()