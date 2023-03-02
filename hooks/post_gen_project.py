import subprocess
import glob
import os

language = "{{cookiecutter.language}}"

# create Python project
if language == "Python":
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
