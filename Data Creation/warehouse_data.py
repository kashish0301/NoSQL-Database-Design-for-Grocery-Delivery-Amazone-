from bson import ObjectId
from pymongo import MongoClient
from faker import Faker
import random
import names

# Connect to MongoDB
client = MongoClient('mongodb+srv://kharyalkashish3:Kashish0301@cluster0.hevoqie.mongodb.net/')
db = client["Amazone-test-1"]

warehouses_collection = db['warehouses']  # Replace 'warehouses' with your actual collection name

# Insert data for the Amazon Warehouse
warehouse_data = {
    "location": ObjectId(),
    "warehouseName": "Amazon Warehouse Manchester",
    "address": {
        "street": "Trafford Park",
        "city": "Manchester",
        "postcode": "M17 1TN",
        "country": "England"
    },
    "storedProducts": []  # Initialize with an empty list for stored products
}

# Insert the data into the MongoDB collection
result = warehouses_collection.insert_one(warehouse_data)

# Print the inserted document ID
print("Inserted document ID:", result.inserted_id)