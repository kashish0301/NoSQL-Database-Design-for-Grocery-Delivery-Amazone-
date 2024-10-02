from bson import ObjectId
from pymongo import MongoClient
from faker import Faker
import random
import names

# Connect to MongoDB
client = MongoClient('mongodb+srv://kharyalkashish3:Kashish0301@cluster0.hevoqie.mongodb.net/')
db = client["Amazone-test-1"]
customer_collection = db["Customer"]

fake = Faker()

# List of Manchester postcodes
manchester_postcodes = [
    "M1 1AA", "M1 1AB", "M1 1AD", "M1 1AE", "M1 1AF", "M1 1AG",
    "M2 2AA", "M2 2AB", "M2 2AD", "M2 2AE", "M2 2AF", "M2 2AG",
    "M3 3AA", "M3 3AB", "M3 3AD", "M3 3AE", "M3 3AF", "M3 3AG",
    "M4 4AA", "M4 4AB", "M4 4AD", "M4 4AE", "M4 4AF", "M4 4AG",
]

# List of Manchester streets
manchester_streets = [
    "Oxford Street", "Deansgate", "Market Street", "Piccadilly", "Albert Square",
    "King Street", "Portland Street", "Princess Street", "Mosley Street", "St Ann's Square",
    "Castlefield", "Northern Quarter", "Ancoats", "Spinningfields", "Exchange Square",
    "Great Ducie Street", "Chepstow Street", "Peter Street", "Whitworth Street", "Chapel Street",
]

# Function to generate multiple Manchester-specific addresses for a customer
def generate_manchester_addresses():
    addresses = []

    # Primary address
    primary_address = {
        "_id": ObjectId(),
        "type": "Primary",
        "houseNumber": fake.building_number(),
        "street": random.choice(manchester_streets),
        "city": "Manchester",
        "postcode": random.choice(manchester_postcodes)
    }
    addresses.append(primary_address)

    # Secondary address
    secondary_address = {
        "_id": ObjectId(),
        "type": "Secondary",
        "houseNumber": fake.building_number(),
        "street": random.choice(manchester_streets),
        "city": "Manchester",
        "postcode": random.choice(manchester_postcodes)
    }
    addresses.append(secondary_address)

    return addresses


# Function to generate customer data with multiple Manchester-specific addresses
def generate_manchester_customer():
    return {
        "name": names.get_full_name(),
        "gender": fake.random_element(elements=('Male', 'Female')),
        "age": fake.random_int(min=20, max=50),
        "addresses": generate_manchester_addresses(),
        "pastOrders": [],
        "currentOrders": [],
        "ratings": [],
        "recommendedProducts": []
    }


# Insert 20 Manchester-specific customers
manchester_customers_data = [generate_manchester_customer() for _ in range(20)]
result = customer_collection.insert_many(manchester_customers_data)

print(f"Inserted {len(result.inserted_ids)} Manchester-specific customers.")