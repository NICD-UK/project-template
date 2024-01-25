import glob
import os
import platform

language = "{{cookiecutter.project_language}}"

# create Python project
if language == "Python":
    with open(".python-version", "w") as file:
        file.write(platform.python_version())
    os.remove("MakefileR")
    os.rename("MakefilePython", "Makefile")
    os.remove("{{cookiecutter.project_directory_name}}.Rproj")
    for file in glob.glob("**/*.Rmd", recursive=True):
        os.remove(file)

# create R project
if language == "R":
    os.remove("MakefilePython")
    os.rename("MakefileR", "Makefile")
    for file in glob.glob("**/*.py", recursive=True):
        os.remove(file)
