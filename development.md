# Development and contribution
## Prerequisites
    - Install git, pip and postgreSQL

## To contribute, fork and clone.  
```console
user@user:~$ git clone https://github.com/Stanley-Okwii/send-it-api.git
```
 
 The code is in python. Use a typescript IDE of your choice, like Visual Studio Code or WebStorm.
 
## To set up the development environment, run:
```console
user@user:~$ pip install -r requirements.txt
```

## Running tests without coverage
Run the tests from the terminal
```console
user@user:~$ pytest tests
```

## Running tests with coverage
Run tests with coverage by running this command in the terminal
```console
user@user:~$ pytest tests --cov=app --cov-report term-missing
```

## Running tests with coverage as html output
Run tests with an html code coverage output
```console
user@user:~$ pytest tests --cov=app --cov-report html --cov-report term-missing
```
