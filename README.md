# SEND IT API
[![Coverage Status](https://coveralls.io/repos/github/Stanley-Okwii/send-it-api/badge.svg?branch=persistent-data)](https://coveralls.io/github/Stanley-Okwii/send-it-api?branch=development)
[![Build Status](https://travis-ci.org/Stanley-Okwii/send-it-api.svg?branch=persistent-data)](https://travis-ci.org/Stanley-Okwii/send-it-api/)
[![Requirements Status](https://requires.io/github/Stanley-Okwii/send-it-api/requirements.svg?branch=persistent-data)](https://requires.io/github/Stanley-Okwii/send-it-api/requirements/?branch=persistent-data)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e1b69a7d2b1a4e15a7ad9db7a7de6a64)](https://www.codacy.com/app/Stanley-Okwii/send-it-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Stanley-Okwii/send-it-api&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/deffc4af002cf7975420/maintainability)](https://codeclimate.com/github/Stanley-Okwii/send-it-api/maintainability)

A set of API endpoints to provide and manipulate data for the SendIT courier services

## Test Project 
This API is hosted at [send-it-api](https://sender-app.herokuapp.com) on [heroku](heroku.com)

## Features
 - Create a user account
 - Update account user name, password and role
 - Get all users
 - Create a parcel delivery order
 - Update parcel details i.e status, current location and destination
 - Get all parcel delivery orders
 - Get all parcel delivery orders owned by a given user
 - Get a specific parcel delivery order
 - Cancel a parcel delivery order

## End points
### User
#### Sign up
A user can sign up by sending a `POST` request to `/api/v1/user` endpoint with request in `JSON` format.

An example would be
```json
{
  "name": "user",
  "email": "user@gmail.com",
  "password": "123456"
}
```
The email should be of a valid email format and the password should contain at least 4 characters.

#### Sign in
A user is able to login by sending a `POST` request to `/api/v1/auth/signin` with the json request below.
```json
{
  "email": "user@gmail.com",
  "password": "123456"
}
```

#### Update password, name and role
A user can update their details by sending a `PUT` request to `/api/v1/user/<email>` with the json request below. Ensure to replace `<email>` with the email of the user whose details are to be updated.
```json
{
  "name": "new name",
  "password": "new password",
  "role": "new role"
}
```

#### Delete account
A user can delete an account by sending a `DELETE` request to `/api/v1/user/<email>`. Ensure to replace `<email>` with the email of the user whose details are to be deleted.

#### Get all users
An admin can get all user information by sending a `GET` request to `/api/v1/users/<admin-email>`.
Replace `<admin-email>` with the email of the administrator.

### Parcel delivery order
A user is able to create and fetch a list of their parcels.

#### Create parcel order
To create a parcel a `POST` request is sent to `/api/v1/parcels`. The request data will be in the format shown below.

```json
{
    "email": "hemworth@gmail.com",
    "parcel": "Bit coins",
    "weight": "2",
    "price": "1500",
    "receiver": "Me",
    "pickup_location": "Kansanga",
    "destination": "Kireka"
}
```

#### Get user's parcels
A user can get their parcels by sending a `GET` request to `/api/v1/users/<email>parcels`. Replace `<email>` with the email of the user whose parcels are to be fetched.

#### Get all users' parcels
An admin can get all users' parcels by sending a `GET` request to `/api/v1/users/<admin-email>parcels`. Replace `<admin-email>` with the email of the administrator.

#### Get a user parcel by order id
A user can get their parcels by sending a `GET` request to `/api/v1/parcels/<orderId>`. Replace `<orderId>` with the corresponding order id to retrieve.

#### Edit a parcel
A user can edit their parcels by sending a `PUT` request to `/api/v1/parcels`.The request data will be in the format shown below. Only destination, current_location and status can be updated, the rest of the information concerning a parcel order is maintained. Status of parcel can be `pending`, `delivered` or `cancelled`.
```json
{
    "id": "991",
    "destination": "Kireka",
    "current_location": "kampala road",
    "status": "delivered"
}
```
### Sample of existing dummy test data
The data below is already existing data in the api and can be used for testing purposes.  
A list of users:  
```json
user_list = [
    {
        "name":"stanley",
        "email":"stanley@gmail.com",
        "password":"123456",
        "role": "user"
    },
    {
        "name":"okwii",
        "email":"okwii@gmail.com",
        "password":"000000",
        "role": "user"
    },
    {
        "name":"admin",
        "email":"admin@gmail.com",
        "password":"admin",
        "role": "admin"
    }
]
```

Parcel delivery orders:
```json
parcel_delivery_orders = {
        "stanley@gmail.com": [
            {
                "id": "001",
                "parcel": "Goat",
                "weight": 50,
                "price": 7000,
                "receiver": "Mary",
                "pickup_location": "Mbale",
                "destination": "Iganga",
                "current_location": "Mbale Town",
                "status": "pending"
            },
            {
                "id": "009",
                "parcel": "Pig",
                "weight": 150,
                "price": 1089000,
                "receiver": "Nicolette",
                "pickup_location": "Kampala",
                "destination": "Kumi",
                "current_location": "Mbale",
                "status": "delivered"
            }
        ],
        "okwii@gmail.com": [
            {
                "id": "089",
                "parcel": "Pig",
                "weight": 150,
                "price": 1089000,
                "receiver": "Nicolette",
                "pickup_location": "Kampala",
                "destination": "Kumi",
                "current_location": "Mbale",
                "status": "delivered"
            }
        ]
}
```

### Running tests without coverage
Run the tests from the terminal
```console
user@user:~$ pytest tests
```

### Running tests with coverage
Run tests with coverage by running this command in the terminal
```console
user@user:~$ pytest tests --cov=app --cov-report term-missing
```

### Running tests with coverage as html output
Run tests with an html code coverage output
```console
user@user:~$ pytest tests --cov=app --cov-report html --cov-report term-missing
```
