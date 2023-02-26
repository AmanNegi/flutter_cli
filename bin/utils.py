import re
import os
import subprocess

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

    subprocess.run(['dart', 'format', file], shell=True)
    print("Removed All Comments! 💚")  

def createTemplateFile(createAt, name, createFrom):
    data = '';
    with open(createFrom, 'r') as f:
        data = f.read();
        f.close();
    path = createAt+"/"+name;
    with open(path, 'w+') as f:
        f.seek(0);
        f.write(data);
        f.close();
        formatFile(path);
    return True;
        
def formatFile(dart_file_path):
    # Run the dart format command using subprocess
    process = subprocess.Popen(["dart", "format", dart_file_path],shell =True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Check the output
    if stderr:
     print("An error occurred while formatting ❌: ", stderr.decode("utf-8"))
    else:
     print("Formatted Successfully ✅");
     
    