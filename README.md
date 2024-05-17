# datafun-03-analyticsP3
Project 3 repository

## Create project
Created a new repo in GitHub with the name 'datafun-03-analyticsP3' 

Added the default README.md 

Named the script karitaylor_analytics.py

## Clone project down to my machine
Opened VS Code 

Used file > open folder to access the folder where I want my project to reside

Opened a new terminal (with powershell as default) 

Used the 'git clone' command to clone the project to my machine

```shell

git clone site_URL

```

## Create a requirements.txt file
Created a new file in my datafun-03-analyticsP3 folder labeled requirements.txt

Typed requests in line 1

## Create and activate a Python virtual environment
Used the following command to create and activate a virtual environment:
```shell

py -m venv .venv
.\.venv\Scripts\Activate.ps1

```

## Install requests in the requirements.txt file and freeze
Installed requests and freezed the requirements.txt file using the following commands:
```shell

py -m pip install requests
py -m pip freeze > requirements.txt

```

## Create .gitignore
Created a new file in my datafun-03-analyticsP3 folder named .gitignore

Typed .venv/ into line 1

## Create docstring for .py project file
Created a docstring on line 1 of the file titled karitaylor_analytics.py with a brief explanation of the project

## Git add and commit
Periodically add, commit, and push files from my machine to the associated online repo using the following commands:
```shell

git add .
git commit -m "add .gitignore, cmds to readme"
git push origin main

```

## Specification
This project was built to the following specification:
- [datafun-03-spec](https://github.com/denisecase/datafun-03-spec)




