import subprocess
import sys
import os

# Packages list
packages = ["django", "djangorestframework", "requests"]

print("Installing packages...")

for package in packages:
    subprocess.run([sys.executable, "-m", "pip", "install", package])

print("Packages installed!")

# Project name
project_name = "myproject"

# Create Django project
subprocess.run([sys.executable, "-m", "django", "startproject", project_name])

# Move into project folder
os.chdir(project_name)

# Create app
subprocess.run([sys.executable, "manage.py", "startapp", "myapp"])

print("Django project and app created successfully!")