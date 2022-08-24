import subprocess

python_venv = '{{cookiecutter.python_venv}}'

# add virtual envoronment
if python_venv == "Yes":   
    subprocess.run(["python3", "-m", "venv", ".venv"])
    subprocess.run([".venv/bin/python", "-m", "pip", "install", "--upgrade", "pip"])
