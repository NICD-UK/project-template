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
    os.remove("README-r.md")
    os.rename("README-python.md", "README.md")
    os.remove("{{cookiecutter.project_directory_name}}.Rproj")
    for file in glob.glob("**/*.Rmd", recursive=True):
        os.remove(file)

# create R project
if language == "R":
    os.remove("Makefile-python")
    os.rename("Makefile-r", "Makefile")
    os.remove("README-python.md")
    os.rename("README-r.md", "README.md")
    for file in glob.glob("**/*.py", recursive=True):
        os.remove(file)
