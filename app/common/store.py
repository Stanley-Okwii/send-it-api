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
