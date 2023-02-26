import click
import re
import json
import subprocess


@click.command("clearComments")   
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

