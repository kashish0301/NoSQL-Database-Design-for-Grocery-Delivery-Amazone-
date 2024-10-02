from pymongo import MongoClient
import random

# Connect to MongoDB
client = MongoClient('mongodb+srv://kharyalkashish3:Kashish0301@cluster0.hevoqie.mongodb.net/')
db = client["Amazone-test-1"]

# Define the collections
products_collection = db["products"]
customers_collection = db["Customer"]
ratings_collection = db["Ratings"]

def get_customer_preferences(customer_id):
    # Get ratings given by the customer
    customer_ratings = ratings_collection.find({"customerID": customer_id})

    # Extract product IDs and corresponding ratings
    product_ratings = {rating["productID"]: rating["rating"] for rating in customer_ratings}

    return product_ratings

def recommend_products(customer_id, num_recommendations=2):
    # Get the customer's preferences
    customer_preferences = get_customer_preferences(customer_id)

    # Get products not yet rated by the customer
    unrated_products = list(products_collection.aggregate([
        {"$match": {"_id": {"$nin": list(customer_preferences.keys())}}},
        {"$sample": {"size": num_recommendations}}
    ]))

    # Sort unrated products by their average customer rating
    unrated_products.sort(key=lambda x: x["averageCustomerRating"], reverse=True)

    # Extract recommended product information
    recommendations = []
    for product in unrated_products[:num_recommendations]:
        recommendations.append({
            "productName": product["productName"],
            "price": product["standardPrice"],
            "category": product["productCategory"],
            "averageCustomerRating": product["averageCustomerRating"]
        })

    return recommendations

# Update customers with product recommendations
for customer in customers_collection.find():
    customer_id = customer["_id"]

    # Get recommendations for the customer
    recommendations = recommend_products(customer_id, num_recommendations=2)

    # Update the customer document with recommendations
    customers_collection.update_one(
        {"_id": customer_id},
        {"$set": {"recommendedProducts": recommendations}}
    )

print("Recommendations updated successfully.")
