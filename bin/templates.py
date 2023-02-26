import click
import subprocess
import os
from utils import clearComments, createTemplateFile
from utils import formatFile


@click.command("create")
@click.argument("name", required=True)
def create(name):
    print("Creating project...")
    result = subprocess.run(
        ['flutter', 'create', name], shell=True, capture_output=True, text=True)
    if (result.returncode != 0):
        # An error occured
        print("An error occured while creating the project ❗")
        print(result.stderr)
        return
    absPath = (os.path.abspath(name+"/lib/"))
    print(absPath)
    clearComments(absPath+"/main.dart")
    # Create a /pages folder
    pagesDir = absPath+"/pages"
    os.mkdir(pagesDir)
    createTemplateFile(pagesDir, "home_page.dart",
                       os.path.abspath("../data/temp_page.dart"))

    print("Created project successfully! ✅")


#! Generate basic page template with
# ? late var height, width and Stateful Widget
@click.command("defgen", help="Default Generate a .dart file")
@click.argument("path", required=True)
def defgen(path):
    print("Generating template file...")
    lines = ''
    with open("../data/temp_page.dart", 'r') as f:
        lines = f.readlines()
        f.close()

    if not os.path.exists(path):
        path = os.path.abspath(path)
        print(path)

    if not os.path.exists(path):
        os.makedirs(path)

    path = os.path.join(path, "temp_page.dart")

    with open(path, 'w') as f:
        f.writelines(lines)
        f.close()
    print("Generated file successfully! 🤖")

#! Generates Shadow Props at given line number
# ? You can alter the properties under ../data/shadow.dart


@click.command("shadow", help="Genrate Shadow Props at given line number")
@click.argument("path", required=True)
@click.option('--line', default=0, help="Specific Line you want to generate into")
def shadow(path, line):
    print(path, line)
    # Get Data from File first
    shadow = ''
    with open('../data/shadow.dart', 'r') as f:
        shadow = f.read()
        f.close()

    with open(path, 'r+') as file:
        # If file does not contain any data
        contents = file.readlines()
        if not contents:
            file.write(shadow)

        # If file contains some data
        else:
            # lines[line] = shadow.strip() + '\n'
            # print(lines);
            contents[line] = shadow
            file.seek(0)
            file.writelines(contents)
            file.truncate()
        file.close()
        # result = subprocess.run(['flutter'], capture_output=True, text=True)
        print(os.path.abspath(path))
        # result = subprocess.run(
        #     ['dart','format',os.path.abspath(path)],shell=True, capture_output=True, text=True)
        # print(result.stdout)
        formatFile(os.path.abspath(path))
        print("Added shadow at specified line 👍⚡")
