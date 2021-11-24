import glob
import sys
import os

language = '{{cookiecutter.language}}'

if language == "Python":
    files = glob.glob('./src/*/*.R', recursive=True)
elif language == "R":
    files = glob.glob('./src/*/*.py', recursive=True)
else:
    sys.exit(1)

for file in files:
    try:
        os.remove(file)
    except:
        sys.exit(1)
