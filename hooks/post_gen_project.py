import subprocess

venv_project = "{{cookiecutter.venv_project}}"
git_project = "{{cookiecutter.git_project}}"

# createe venv project
if venv_project == "Yes":   
    subprocess.run(["python3 -m venv .venv"])
    subprocess.run([".venv/bin/python -m pip install --upgrade pip"])

# create git project
if git_project == "Yes":
    subprocess.run(["git init"])
    subprocess.run(["git add --all"])
    subprocess.run(["git commit -m 'initial commit'"])

# gitignore config.yml
with open(".gitignore", "a") as f:
    lines = ["\n", "# configuration file\n", "config.yml\n"]
    f.writelines(lines)
