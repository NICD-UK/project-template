import glob
import os
import platform

language = "{{cookiecutter.project_language}}"

# create Python project
if language == "Python":
    with open(".python-version", "w") as file:
        file.write(platform.python_version())
    os.remove("Makefile-r")
    os.rename("Makefile-python", "Makefile")
    os.remove("checklist-r.md")
    os.rename("checklist-python.md", "checklist.md")
    os.remove("{{cookiecutter.project_directory_name}}.Rproj")
    for file in glob.glob("**/*.Rmd", recursive=True):
        os.remove(file)

# create R project
if language == "R":
    os.remove("Makefile-python")
    os.rename("Makefile-r", "Makefile")
    os.remove("checklist-python.md")
    os.rename("checklist-r.md", "checklist.md")
    for file in glob.glob("**/*.py", recursive=True):
        os.remove(file)
