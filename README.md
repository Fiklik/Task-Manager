### Tests and linter status:
[![Actions Status](https://github.com/Fiklik/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Fiklik/python-project-52/actions)
[![Actions Status](https://github.com/Fiklik/python-project-52/actions/workflows/linter-and-test-check.yml/badge.svg)](https://github.com/Fiklik/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/571269021d84a1cddddd/maintainability)](https://codeclimate.com/github/Fiklik/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/571269021d84a1cddddd/test_coverage)](https://codeclimate.com/github/Fiklik/python-project-52/test_coverage)


# Task manager
[**Task manager**](https://task-manager-qlk7.onrender.com) is a tool for project management. 

With its help, you can assign tasks to employees and monitor their implementation

## Installation
- clone repository with one of the commands:
```
    git clone https://github.com/Fiklik/python-project-52.git
```

```
    git clone git@github.com:Fiklik/python-project-52.git
```

- install poetry with command:
```
    python -m pip install poetry
```

- **make install** - poetry will install all required dependencies for you
- create file '.env' and paste in secret key for django application to run (see '.env_example' file)
- **make runserver** - start server for development
- **make start** - start production server
