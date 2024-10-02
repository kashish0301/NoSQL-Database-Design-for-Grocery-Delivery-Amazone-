from bson import ObjectId
from pymongo import MongoClient
from faker import Faker
import random
import names

# Connect to MongoDB
client = MongoClient('mongodb+srv://kharyalkashish3:Kashish0301@cluster0.hevoqie.mongodb.net/')
db = client["Amazone-test-1"]

# Function to generate data for Amazone
def generate_amazone_data():
   partners = []
   products = list(db.products.find())  # Retrieve all products once


   for _ in range(10):  # Generate data for 10 partners
       total_deliveries = random.randint(1, 50)
       successful_deliveries = random.randint(1, total_deliveries)  # Ensure successful deliveries <= total deliveries


       partner = {
           "name": fake.name(),
           "gender": fake.random_element(elements=('Male', 'Female')),
           "age": fake.random_int(min=25, max=50),
           "currentLocation": {
               "latitude": random.uniform(53.0, 54.0),
               "longitude": random.uniform(-2.5, -1.5)
           },
           "status": fake.random_element(elements=('idle', 'active')),
           "deliveredProducts": [],
           "statistics": {
               "totalDeliveries": total_deliveries,
               "successfulDeliveries": successful_deliveries,
               "earnings": random.randint(100, 1000)
           }
       }


       if partner["status"] == "idle":
           partner["onDeliveryErrand"] = False
       elif partner["status"] == "active":
           partner["onDeliveryErrand"] = fake.boolean(chance_of_getting_true=50)  # 50% chance of being on a delivery errand


       partners.append(partner)


       # Add details of delivered products for active partners
       if partner["status"] == "active" and partner["onDeliveryErrand"]:
           for _ in range(total_deliveries):  # Simulate delivering all products
               random_product = random.choice(products)
               delivered_product = {
                   "productID": random_product["_id"],
                   "productName": random_product["productName"],
                   "quantity": random.randint(1, 5),
                   "deliveryStatus": fake.random_element(elements=('delivered', 'pending'))
               }
               partner["deliveredProducts"].append(delivered_product)


   db.partners.insert_many(partners)


generate_amazone_data()
