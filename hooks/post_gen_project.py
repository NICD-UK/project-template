import glob
import os
import platform

language = "{{cookiecutter.project_language}}"

# create Python project
if language == "Python":
    os.remove("Makefile-r")
    os.rename("Makefile-python", "Makefile")
    os.remove("src/2-clean/README-r.md")
    os.rename("src/2-clean/README-python.md", "src/2-clean/README.md")
    os.remove("src/3-wrangle/README-r.md")
    os.rename("src/3-wrangle/README-python.md", "src/3-wrangle/README.md")
    os.remove("{{cookiecutter.project_directory_name}}.Rproj")
    for file in glob.glob("**/*.Rmd", recursive=True):
        os.remove(file)

# create R project
if language == "R":
    os.remove("Makefile-python")
    os.rename("Makefile-r", "Makefile")
    os.remove("src/2-clean/README-python.md")
    os.rename("src/2-clean/README-r.md", "src/2-clean/README.md")
    os.remove("src/3-wrangle/README-python.md")
    os.rename("src/3-wrangle/README-r.md", "src/3-wrangle/README.md")
    for file in glob.glob("**/*.py", recursive=True):
        os.remove(file)
