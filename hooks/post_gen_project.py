import glob
import sys
import os
import subprocess

language = '{{cookiecutter.language}}'
environment = '{{cookiecutter.environment}}'

# remove Python or R scripts
if language == "Python":
    files = glob.glob('./src/*/*.Rmd', recursive=True)
    os.remove('{{cookiecutter.repo_name}}.Rproj')
elif language == "R":
    files = glob.glob('./src/*/*.py', recursive=True)
else:
    sys.exit(1)

for file in files:
    try:
        os.remove(file)
    except:
        sys.exit(1)

# add virtual envoronment
if environment == "venv":   
    packages = [
        "ipykernel", "pandas", "numpy", "scipy", "scikit-learn"
    ]
    subprocess.run(["python3", "-m", "venv", ".venv"])
    subprocess.run([".venv/bin/python", "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.run([".venv/bin/python", "-m" "pip", "install"] + packages)