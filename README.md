# SEND IT API
[![Coverage Status](https://coveralls.io/repos/github/Stanley-Okwii/send-it-api/badge.svg?branch=persistent-data)](https://coveralls.io/github/Stanley-Okwii/send-it-api?branch=development)
[![Build Status](https://travis-ci.org/Stanley-Okwii/send-it-api.svg?branch=persistent-data)](https://travis-ci.org/Stanley-Okwii/send-it-api/)
[![Requirements Status](https://requires.io/github/Stanley-Okwii/send-it-api/requirements.svg?branch=persistent-data)](https://requires.io/github/Stanley-Okwii/send-it-api/requirements/?branch=persistent-data)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e1b69a7d2b1a4e15a7ad9db7a7de6a64)](https://www.codacy.com/app/Stanley-Okwii/send-it-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Stanley-Okwii/send-it-api&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/deffc4af002cf7975420/maintainability)](https://codeclimate.com/github/Stanley-Okwii/send-it-api/maintainability)

A set of API endpoints to provide and manipulate data for the SendIT courier services

## Test Project 
This API is hosted at [send-it-api](https://sender-app.herokuapp.com) on [heroku](heroku.com)

## Dependencies
Flask 1.0.2  
Python 3.6.1

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

If the request is successful, a response with the structure below is returned:
```
{
    "data": {
        "message": "You have logged in successfully.",
        "user_token": "Generated token here"
    }
}
```
 **NOTE:** An authorization token must be attached in the Authorization header with the token generated up user sign in for all requests except sign in and sign up requests.

#### Update password and name
A user can update their details by sending a `PUT` request to `/api/v1/user` with the json request below. 
```json
{
  "name": "new name",
  "password": "new password",
  "role": "new role"
}
```
#### Update user roles
An admin can update user roles by sending a `PUT` request to `/api/v1/role` with the json request below.  
```json
{
  "email": "email_of_user_to_update_role",
  "role": "new role"
}
```

#### Delete account
A user can delete an account by sending a `DELETE` request to `/api/v1/user`.

#### Get all users
An admin can get all user information by sending a `GET` request to `/api/v1/users`. 

### Parcel delivery order
A user is able to create and fetch a list of their parcels.

#### Create parcel order
To create a parcel a `POST` request is sent to `/api/v1/parcels`. The request data will be in the format shown below.

```json
{
    "parcel": "Bit coins",
    "weight": "2",
    "price": "1500",
    "receiver": "Me",
    "pickup_location": "Kansanga",
    "destination": "Kireka"
}
```

#### Get user's parcels
A user can get their parcels by sending a `GET` request to `/api/v1/parcels`.

#### Get all users' parcels
An admin can get all users' parcels by sending a `GET` request to `/api/v1/parcels`. 

#### Get a user parcel by order id
A user can get their parcels by sending a `GET` request to `/api/v1/parcels/<orderId>`. Replace `<orderId>` with the corresponding order id to retrieve.

#### Cancel a parcel
A user can cancel a parcel by sending a `PUT` request to `/api/v1/parcels/cancel`.The request data will be in the format shown below. 
```json
{
    "id": "991"
}
```

#### Change destination of a parcel
A user can change destination a parcel by sending a `PUT` request to `/api/v1/parcels/destination`.The request data will be in the format shown below. 
```json
{
    "destination": "Tororo",
    "id": "1"
}
```

#### Edit status and current location of a parcel
An Admin can a given user's parcel by sending a `PUT` request to `/api/v1/parcels/status`.The request data will be in the format shown below. Only current_location and status can be updated, the rest of the information concerning a parcel order is maintained. Both current_location and status are optional.  
```json
{
    "id": "991",
    "current_location": "kampala road",
    "status": "delivered"
}
```

## Issues, suggestions and feature requests
This api is actively under maintenance, please report any issues or suggestion for improvement at  
https://github.com/Stanley-Okwii/send-it-api/issues

## Development and contribution
Please follow [development guide](/development.md)
