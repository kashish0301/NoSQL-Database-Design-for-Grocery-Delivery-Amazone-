from pymongo import MongoClient, GEOSPHERE
from faker import Faker
import random
import datetime
from datetime import date, timedelta
import bson

fake = Faker()

client = MongoClient('mongodb+srv://kharyalkashish3:Kashish0301@cluster0.hevoqie.mongodb.net/')
db = client['Amazone-test-1']

warehouses_collection = db['warehouses']
ratings_col = db['ratings-a']
products_col = db['products']
#Update Average rating for each product based on its ratingsss
def update_average_ratings():
    pipeline = [
        {
            "$group": {
                "_id": "$productID",
                "averageRating": {"$avg": "$score"}
            }
        }
    ]
    
    product_ratings = ratings_col.aggregate(pipeline)
    for product_rating in product_ratings:
        product_id = product_rating["_id"]
        average_rating = product_rating["averageRating"]

        # Update the average customer rating in the products collection
        products_col.update_one(
            {"productID": product_id},
            {"$set": {"averageCustomerRating": round(average_rating, 1)}}
        )

# Call the function to update average ratings
update_average_ratings()