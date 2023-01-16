import subprocess

venv_project = "{{cookiecutter.venv_project}}"
git_project = "{{cookiecutter.git_project}}"

# create venv project
if venv_project == "Yes":   
    subprocess.run(["python3", "-m", "venv", ".venv"], stdout=subprocess.DEVNULL)
    subprocess.run([".venv/bin/python", "-m", "pip", "install", "--upgrade", "pip"], stdout=subprocess.DEVNULL)

# gitignore config.yml
with open(".gitignore", "a") as f:
    lines = ["\n", "# configuration file\n", "config.yml\n"]
    f.writelines(lines)

# create git project
if git_project == "Yes":
    subprocess.run(["git", "init"], stdout=subprocess.DEVNULL)
    subprocess.run(["git", "add", "--all"], stdout=subprocess.DEVNULL)
    subprocess.run(["git", "commit", "-m", "'initial commit'"], stdout=subprocess.DEVNULL)
