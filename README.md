# SEND IT API

[![Coverage Status](https://coveralls.io/repos/github/Stanley-Okwii/send-it-api/badge.svg?branch=development)](https://coveralls.io/github/Stanley-Okwii/send-it-api?branch=development)
[![Build Status](https://travis-ci.org/Stanley-Okwii/send-it-api.svg?branch=development)](https://travis-ci.org/Stanley-Okwii/send-it-api/)
[![Requirements Status](https://requires.io/github/Stanley-Okwii/send-it-api/requirements.svg?branch=development)](https://requires.io/github/Stanley-Okwii/send-it-api/requirements/?branch=development)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/847d5ac9919144b88cb6c0807a36d2f9)](https://app.codacy.com/app/Stanley-Okwii/send-it-api?utm_source=github.com&utm_medium=referral&utm_content=Stanley-Okwii/send-it-api&utm_campaign=Badge_Grade_Dashboard)

a set of API endpoints to provide and manipulate data for the SendIT courier services

## Demo App
This API is hosted [here](https://sender-app.herokuapp.com) on [heroku](heroku.com)

## End points

### Running tests without coverage
You can now run the tests from the terminal
```
pytest test/
```

### Running tests with coverage
You can also run tests with coverage by running this command in the terminal
```
pytest tests --cov=app --cov-report term-missing
```

### Running tests with coverage as html output
Create a html code coverage output
```
pytest tests --cov=app --cov-report html --cov-report term-missing
```
