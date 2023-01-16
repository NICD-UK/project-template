import subprocess

python_venv = '{{cookiecutter.python_venv}}'

# add virtual environment
if python_venv == "Yes":   
    subprocess.run(["python3", "-m", "venv", ".venv"])
    subprocess.run([".venv/bin/python", "-m", "pip", "install", "--upgrade", "pip"])

# gitignore config.yml
with open(".gitignore", "a") as f:
    lines = ["\n", "# configuration file\n", "config.yml\n"]
    f.writelines(lines)
