from pymongo import MongoClient
from faker import Faker
from bson import ObjectId
import random
import datetime
import json

fake = Faker()

# Connect to MongoDB
client = MongoClient('mongodb+srv://kharyalkashish3:Kashish0301@cluster0.hevoqie.mongodb.net/')
db = client["Amazone-test-db"]

# Function to generate random past and current orders
def generate_orders(customer_id, order_count):
    orders = []
    for i in range(order_count):
        order = {
            "orderID": str(ObjectId()),
            "customerID": customer_id,
            "totalCost": round(random.uniform(10, 200), 2),
            "orderDate": fake.date_between(start_date='-1y', end_date='today'),
            "status": random.choice(["delivered", "in transit", "pending"]),
            "orderItems": generate_order_items()
        }
        orders.append(order)
    return orders

# Function to generate random order items
def generate_order_items():
    order_items = []
    product_ids = [str(ObjectId()) for _ in range(random.randint(1, 5))]
    for product_id in product_ids:
        order_item = {
            "productID": product_id,
            "quantity": random.randint(1, 10)
        }
        order_items.append(order_item)
    return order_items

# Insert customers with orders into the database
for _ in range(20):  # Insert 20 customers for example
    customer = {
        "customerID": str(ObjectId()),
        "name": fake.name(),
        "gender": fake.random_element(elements=('Male', 'Female')),
        "age": random.randint(18, 65),
        "address": [
            {
                "addressID": str(ObjectId()),
                "houseNumber": fake.building_number(),
                "street": fake.street_name(),
                "city": fake.city(),
                "postcode": fake.zipcode(),
                "addressType": random.choice(["billing", "shipping"])
            }
        ],
        "pastOrders": generate_orders(customer_id, random.randint(1, 5)),
        "currentOrders": generate_orders(customer_id, random.randint(1, 2)),
        "ratings": [],
        "recommendedProducts": []
    }
    db.customers.insert_one(customer)

# Function to generate random ratings
def generate_ratings(customer_id, product_ids):
    ratings = []
    for product_id in product_ids:
        if random.random() < 0.01:  # 1% chance to give a rating
            rating = {
                "customerID": customer_id,
                "productID": product_id,
                "score": random.randint(1, 5),
                "comment": fake.sentence(),
                "ratingDate": fake.date_between(start_date='-1y', end_date='today')
            }
            ratings.append(rating)
    return ratings

# Insert ratings for customers
customers = db.customers.find()
product_ids = [str(ObjectId()) for _ in range(10)]  # Assuming 10 product samples for each type
for customer in customers:
    ratings = generate_ratings(customer["customerID"], product_ids)
    db.ratings.insert_many(ratings)

# Function to generate fresh products
def generate_fresh_products(category):
    fresh_products = []
    for _ in range(5):  # Assuming 5 fresh products for each category
        fresh_product = {
            "productID": str(ObjectId()),
            "category": category,
            "productName": fake.word(),
            "shortDescription": fake.sentence(),
            "productDimensions": {
                "length": random.uniform(1, 50),
                "width": random.uniform(1, 50),
                "height": random.uniform(1, 50)
            },
            "productWeight": round(random.uniform(0.5, 5), 2),
            "expiryDate": fake.date_between(start_date='today', end_date='+30d'),
            "countryOfOrigin": fake.country(),
            "averageCustomerRating": round(random.uniform(1, 5), 2),
            "standardPrice": round(random.uniform(1, 20), 2),
            "cost": round(random.uniform(0.5, 15), 2),
            "dailyInventoryLevels": generate_daily_inventory_levels(),
            "store": generate_store(),
        }
        fresh_products.append(fresh_product)
    return fresh_products

# Function to generate store details
def generate_store():
    return {
        "storeId": str(ObjectId()),
        "name": fake.company(),
        "location": {
            "latitude": random.uniform(50, 55),
            "longitude": random.uniform(-5, 0)
        }
    }

# Function to generate other products
def generate_other_products(product_type):
    other_products = []
    for _ in range(10):  # Assuming 10 products for each type
        other_product = {
            "productID": str(ObjectId()),
            "productName": fake.word(),
            "shortDescription": fake.sentence(),
            "productDimensions": {
                "length": random.uniform(1, 50),
                "width": random.uniform(1, 50),
                "height": random.uniform(1, 50)
            },
            "shippingWeight": round(random.uniform(0.5, 10), 2),
            "averageCustomerRating": round(random.uniform(1, 5), 2),
            "standardPrice": round(random.uniform(5, 100), 2),
            "cost": round(random.uniform(3, 80), 2),
            "dailyInventoryLevels": generate_daily_inventory_levels(),
            "specificAttributes": generate_specific_attributes(product_type),
        }
        other_products.append(other_product)
    return other_products

# Function to generate specific attributes based on product type
def generate_specific_attributes(product_type):
    if product_type == "book":
        return {
            "authorName": fake.name(),
            "publisher": fake.company(),
            "yearOfPublication": fake.year(),
            "ISBN": fake.isbn13()
        }
    elif product_type == "CD":
        return {
            "artistName": fake.name(),
            "numberOfTracks": random.randint(5, 20),
            "totalPlayingTime": f"{random.randint(30, 120)} min",
            "publisher": fake.company()
        }
    elif product_type == "mobilePhone":
        return {
            "brand": fake.company(),
            "model": fake.word(),
            "color": fake.color_name(),
            "features": fake.sentence()
        }
    elif product_type == "homeAppliance":
        return {
            "color": fake.color_name(),
            "voltage": random.randint(110, 240),
            "style": fake.word()
        }
    else:
        return {}

# Function to generate daily inventory levels
#def generate_daily_inventory_levels():
 #   inventory_levels = []
  #          "date": fake.date_between(start_date='-2d', end_date='-1d'),
   #         "inventoryQuantity": random.randint(10, 100),
    #        "storageWarehouseLocation": fake.city(),
     #       "storageWarehouseName": fake.company()
      #  }
       # inventory_levels.append(inventory_level)
   # return inventory_levels

# Insert fresh products into the database
fresh_categories = ["bakery", "drinks", "fruits and vegetables"]
for category in fresh_categories:
    fresh_products = generate_fresh_products(category)
    db.freshProducts.insert_many(fresh_products)

# Insert other products into the database
product_types = ["book", "CD", "mobilePhone", "homeAppliance"]
for product_type in product_types:
    other_products = generate_other_products(product_type)
    db.otherProducts.insert_many(other_products)

# Insert locations into the database
locations = []
for _ in range(5):
    location = {
        "locationID": str(ObjectId()),
        "latitude": random.uniform(50, 55),
        "longitude": random.uniform(-5, 0),
        "name": fake.city()
    }
    locations.append(location)
db.locations.insert_many(locations)

# Insert partners into the database
partners = []
for _ in range(5):
    partner = {
        "partnerID": str(ObjectId()),
        "name": fake.name(),
        "gender": fake.random_element(elements=('Male', 'Female')),
        "age": random.randint(18, 60),
        "location": {
            "latitude": random.uniform(50, 55),
            "longitude": random.uniform(-5, 0)
        },
        "status": random.choice(["idle", "active"]),
        "deliveryErrand": random.choice([True, False]),
        "ratings": []
    }
    partners.append(partner)
db.partners.insert_many(partners)

# Function to associate fresh products with store locations
def associate_fresh_products_with_locations():
    for category in fresh_categories:
        products = db.freshProducts.find({"category": category})
        for product in products:
            location = db.locations.find_one()
            product["store"] = {
                "storeId": location["locationID"],
                "name": location["name"],
                "location": {
                    "latitude": location["latitude"],
                    "longitude": location["longitude"]
                }
            }
            db.freshProducts.save(product)

# Associate fresh products with store locations
associate_fresh_products_with_locations()

# Function to associate orders with partners
def associate_orders_with_partners():
    orders = db.currentOrders.find()
    for order in orders:
        partner = db.partners.find_one()
        order["deliveryPartner"] = {
            "partnerID": partner["partnerID"],
            "name": partner["name"],
            "location": partner["location"],
            "ratings": partner["ratings"]
        }
        db.currentOrders.save(order)

# Associate current orders with partners
associate_orders_with_partners()

# Print a message indicating successful data insertion
print("Data insertion completed successfully.")

