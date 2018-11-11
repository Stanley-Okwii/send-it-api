# SEND IT API
[![Coverage Status](https://coveralls.io/repos/github/Stanley-Okwii/send-it-api/badge.svg?branch=development)](https://coveralls.io/github/Stanley-Okwii/send-it-api?branch=development)
[![Build Status](https://travis-ci.org/Stanley-Okwii/send-it-api.svg?branch=development)](https://travis-ci.org/Stanley-Okwii/send-it-api/)
[![Requirements Status](https://requires.io/github/Stanley-Okwii/send-it-api/requirements.svg?branch=development)](https://requires.io/github/Stanley-Okwii/send-it-api/requirements/?branch=development)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/847d5ac9919144b88cb6c0807a36d2f9)](https://app.codacy.com/app/Stanley-Okwii/send-it-api?utm_source=github.com&utm_medium=referral&utm_content=Stanley-Okwii/send-it-api&utm_campaign=Badge_Grade_Dashboard)

A set of API endpoints to provide and manipulate data for the SendIT courier services

## Test Project 
This API is hosted at [send-it-api](https://sender-app.herokuapp.com) on [heroku](heroku.com)

## Features
 - Create user account
 - Update account user name and password 
 - Get all users
 - Create a parcel delivery order
 - Update parcel details i.e status, current location and destination
 - Get all parcel delivery orders
 - Get a specific parcel delivery order
 - Cancel a parcel delivery order

## End points
### User
#### Sign up
Send a `POST` request to `/api/v1/user` endpoint with request in **JSON** 

An example would be
```json
{
  "name": "user",
  "email": "user@gmail.com",
  "password": "123456"
}
```
The email should be of a valid email format and the password should contain at least 4 characters

#### Sign in
The user is able to login by send sending a `POST` request to `/api/v1/auth/signin` with the json request below.
```json
{
  "email": "user@gmail.com",
  "password": "123456"
}
```

#### Update password and name
The user can update their details by sending a `PUT` request to `/api/v1/user/<email>` with the json request below. Ensure to replace `<email>` with the email of the user whose details are to be updated
```json
{
  "name": "new name",
  "password": "new password"
}
```

#### Delete account
The user can delete an account by sending a `DELETE` request to `/api/v1/user/<email>`. Ensure to replace `<email>` with the email of the user whose details are to be deleted

#### Get all users
The admin can get all user information by sending a `GET` request to `/api/v1/users`.

### Parcel delivery order
The user is able to create and fetch a list of their parcels.

#### Create parcel order
To create a parcel a `POST` request is sent to `/api/v1/parcels`. The request data will be in the format shown below.

```json
{
    "email": "user@gmail.com",
    "id": "991",
    "parcel": "Bit coins",
    "weight": "2",
    "price": "1500",
    "receiver": "Me",
    "pickup_location": "Kansanga",
    "destination": "Kireka"
}
```

### Get user`s parcels
The user can get their parcels by sending a `GET` request to `/api/v1/parcels/<email>`. Replace `<email>` with the email of the user whose parcels are to be fetched.

### Get all users' parcels
The admin can get all users' parcels by sending a `GET` request to `/api/v1/parcels`.

### Get a user parcel by order id
The user can get their parcels by sending a `GET` request to `/api/v1/parcels/<email>/order/<orderId>`. Replace `<email>` with the email of the user whose parcel is to be fetched and `<orderId>` with the corresponding order id.

### Edit a parcel
The user can edit their parcels by sending a `PUT` request to `/api/v1/parcels`.The request data will be in the format shown below. Only destination, current_location and status can be updated, the rest of the information concerning a parcel order is maintained. Status of parcel can be `pending`, `deliverd` or ``cancelled`.
```json
{
    "email": "user@gmail.com",
    "id": "991",
    "destination": "Kireka",
    "current_location": "kampala road",
    "status": "delivered"
}
```

### Running tests without coverage
You can now run the tests from the terminal
```console
user@user:~$ pytest tests
```

### Running tests with coverage
You can also run tests with coverage by running this command in the terminal
```console
user@user:~$ pytest tests --cov=app --cov-report term-missing
```

### Running tests with coverage as html output
Create a html code coverage output
```console
user@user:~$ pytest tests --cov=app --cov-report html --cov-report term-missing
```
