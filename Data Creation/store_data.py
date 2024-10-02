from bson import ObjectId
from pymongo import MongoClient
from faker import Faker
import random
import names

# Connect to MongoDB
client = MongoClient('mongodb+srv://kharyalkashish3:Kashish0301@cluster0.hevoqie.mongodb.net/')
db = client["Amazone-test-1"]

# Create a collection for stores
stores_collection = db['stores']

# Insert sample data for 5 Morrizons stores
stores_data = [
    {
        "storeID": ObjectId(),
        "address": {
            "houseNumber": "25",
            "street": "Piccadilly Gardens",
            "city": "Manchester",
            "postcode": "M1 1LU"
        },
        "location": {
            "latitude": 53.4808,
            "longitude": -2.2426
        },
        "availableGroceryItems": []
    },
    {
        "storeID": ObjectId(),
        "address": {
            "houseNumber": "15",
            "street": "Grafton Street",
            "city": "Manchester",
            "postcode": "M13 9NU"
        },
        "location": {
            "latitude": 53.4612,
            "longitude": -2.1924
        },
        "availableGroceryItems": []
    },
    {
        "storeID": ObjectId(),
        "address": {
            "houseNumber": "40",
            "street": "Wilbraham Road",
            "city": "Manchester",
            "postcode": "M21 0UA"
        },
        "location": {
            "latitude": 53.4407,
            "longitude": -2.2726
        },
        "availableGroceryItems": []
    },
    {
        "storeID": ObjectId(),
        "address": {
            "houseNumber": "1",
            "street": "Lime Square",
            "city": "Manchester",
            "postcode": "M11 1ND"
        },
        "location": {
            "latitude": 53.4766,
            "longitude": -2.1843
        },
        "availableGroceryItems": []
    },
    {
        "storeID": ObjectId(),
        "address": {
            "houseNumber": "10",
            "street": "Poplar Street",
            "city": "Manchester",
            "postcode": "M35 0HY"
        },
        "location": {
            "latitude": 53.5095,
            "longitude": -2.1683
        },
        "availableGroceryItems": []
    }
]

# Insert the data into the MongoDB collection
result = stores_collection.insert_many(stores_data)

# Print the inserted document IDs
print("Inserted document IDs:", result.inserted_ids)

