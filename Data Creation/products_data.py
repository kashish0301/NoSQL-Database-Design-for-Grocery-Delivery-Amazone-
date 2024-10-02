from bson import ObjectId
from pymongo import MongoClient
from faker import Faker
import random
import names

# Connect to MongoDB
client = MongoClient('mongodb+srv://kharyalkashish3:Kashish0301@cluster0.hevoqie.mongodb.net/')
db = client["Amazone-test-1"]

product_collection = db["products"]

products = {
    "Book": [
        {'productName': 'The Great Gatsby', 'price': 10.99, 'category': 'Book', 'shortDescription': 'A novel of wealth, lust, and betrayal set in the roaring 20s.', 'authorName': 'F. Scott Fitzgerald', 'publisher': "Charles Scribner's Sons", 'yearOfPublication': 1925},
        {'productName': 'To Kill a Mockingbird', 'price': 7.99, 'category': 'Book', 'shortDescription': 'A tale of race and injustice in the Deep South.', 'authorName': 'Harper Lee', 'publisher': 'J. B. Lippincott & Co.', 'yearOfPublication': 1960},
        {'productName': '1984', 'price': 8.99, 'category': 'Book', 'shortDescription': 'A dystopian novel about the dangers of totalitarianism.', 'authorName': 'George Orwell', 'publisher': 'Secker & Warburg', 'yearOfPublication': 1949},
        {'productName': 'Pride and Prejudice', 'price': 9.99, 'category': 'Book', 'shortDescription': 'A romantic novel of manners.', 'authorName': 'Jane Austen', 'publisher': 'T. Egerton, Whitehall', 'yearOfPublication': 1813},
        {'productName': 'The Catcher in the Rye', 'price': 12.99, 'category': 'Book', 'shortDescription': 'A story about the struggles of adolescence.', 'authorName': 'J.D. Salinger', 'publisher': 'Little, Brown and Company', 'yearOfPublication': 1951},
        {'productName': 'The Hobbit', 'price': 10.99, 'category': 'Book', 'shortDescription': 'A fantasy novel and prelude to The Lord of the Rings.', 'authorName': 'J.R.R. Tolkien', 'publisher': 'George Allen & Unwin', 'yearOfPublication': 1937},
        {'productName': 'Fahrenheit 451', 'price': 7.99, 'category': 'Book', 'shortDescription': 'A dystopian novel presenting a future American society where books are outlawed.', 'authorName': 'Ray Bradbury', 'publisher': 'Ballantine Books', 'yearOfPublication': 1953},
        {'productName': 'Jane Eyre', 'price': 9.99, 'category': 'Book', 'shortDescription': 'A novel following the emotions and experiences of its eponymous heroine.', 'authorName': 'Charlotte Brontë', 'publisher': 'Smith, Elder & Co.', 'yearOfPublication': 1847},
        {'productName': 'Moby Dick', 'price': 11.99, 'category': 'Book', 'shortDescription': 'A novel about the voyage of the whaling ship Pequod.', 'authorName': 'Herman Melville', 'publisher': 'Richard Bentley', 'yearOfPublication': 1851},
        {'productName': 'War and Peace', 'price': 13.99, 'category': 'Book', 'shortDescription': 'A novel that chronicles the French invasion of Russia.', 'authorName': 'Leo Tolstoy', 'publisher': 'The Russian Messenger', 'yearOfPublication': 1869}
    ],
    "CD": [
        {'productName': 'Thriller by Michael Jackson', 'price': 9.99, 'category': 'CD', 'shortDescription': 'The best-selling album of all time.', 'artistName': 'Michael Jackson', 'publisher': 'Epic Records'},
        {'productName': 'Back in Black by AC/DC', 'price': 8.99, 'category': 'CD', 'shortDescription': 'The second best-selling album of all time.', 'artistName': 'AC/DC', 'publisher': 'Atlantic Records'},
        {'productName': 'The Dark Side of the Moon by Pink Floyd', 'price': 11.99, 'category': 'CD', 'shortDescription': 'A concept album known for its sonic experimentation.', 'artistName': 'Pink Floyd', 'publisher': 'Harvest Records'},
        {'productName': 'The Bodyguard by Whitney Houston', 'price': 10.99, 'category': 'CD', 'shortDescription': 'The soundtrack album from the motion picture.', 'artistName': 'Whitney Houston', 'publisher': 'Arista Records'},
        {'productName': 'Rumours by Fleetwood Mac', 'price': 7.99, 'category': 'CD', 'shortDescription': 'An album that produced four U.S. Top 10 singles.', 'artistName': 'Fleetwood Mac', 'publisher': 'Warner Bros. Records'},
        {'productName': 'Abbey Road by The Beatles', 'price': 12.99, 'category': 'CD', 'shortDescription': 'The eleventh studio album by the English rock band.', 'artistName': 'The Beatles', 'publisher': 'Apple Records'},
        {'productName': 'Led Zeppelin IV by Led Zeppelin', 'price': 10.99, 'category': 'CD', 'shortDescription': 'One of the best-selling albums worldwide.', 'artistName': 'Led Zeppelin', 'publisher': 'Atlantic Records'},
        {'productName': 'Hotel California by Eagles', 'price': 9.99, 'category': 'CD', 'shortDescription': 'The fifth studio album by the American rock band.', 'artistName': 'Eagles', 'publisher': 'Asylum Records'},
        {'productName': 'The Wall by Pink Floyd', 'price': 11.99, 'category': 'CD', 'shortDescription': 'A rock opera that explores abandonment and isolation.', 'artistName': 'Pink Floyd', 'publisher': 'Harvest Records'},
        {'productName': 'Born in the U.S.A. by Bruce Springsteen', 'price': 8.99, 'category': 'CD', 'shortDescription': 'The seventh studio album by the American rock singer.', 'artistName': 'Bruce Springsteen', 'publisher': 'Columbia Records'}
    ],
    "Mobile Phone": [
        {'productName': 'iPhone 12 Pro Max', 'price': 1099.00, 'category': 'Mobile Phone', 'shortDescription': '5G capable phone with A14 Bionic chip.', 'brand': 'Apple', 'model': '12 Pro Max', 'color': 'Pacific Blue', 'features': 'Super Retina XDR display'},
        {'productName': 'Samsung Galaxy S21', 'price': 799.00, 'category': 'Mobile Phone', 'shortDescription': 'High-quality camera and display.', 'brand': 'Samsung', 'model': 'Galaxy S21', 'color': 'Phantom Gray', 'features': '8K video recording'},
        {'productName': 'Google Pixel 5', 'price': 699.00, 'category': 'Mobile Phone', 'shortDescription': 'Pure Android experience with excellent camera.', 'brand': 'Google', 'model': 'Pixel 5', 'color': 'Just Black', 'features': 'Water-resistant'},
        {'productName': 'OnePlus 9', 'price': 729.00, 'category': 'Mobile Phone', 'shortDescription': 'Fast and smooth performance.', 'brand': 'OnePlus', 'model': '9', 'color': 'Winter Mist', 'features': 'Hasselblad Camera for Mobile'},
        {'productName': 'Xiaomi Mi 11', 'price': 749.00, 'category': 'Mobile Phone', 'shortDescription': 'Top-tier performance at a competitive price.', 'brand': 'Xiaomi', 'model': 'Mi 11', 'color': 'Horizon Blue', 'features': '108MP triple camera'},
        {'productName': 'Sony Xperia 1 II', 'price': 1199.00, 'category': 'Mobile Phone', 'shortDescription': 'Designed for speed with a professional camera.', 'brand': 'Sony', 'model': 'Xperia 1 II', 'color': 'Black', 'features': '4K HDR OLED display'},
        {'productName': 'Motorola Edge Plus', 'price': 999.00, 'category': 'Mobile Phone', 'shortDescription': 'Immersive display with Endless Edge screen.', 'brand': 'Motorola', 'model': 'Edge Plus', 'color': 'Thunder Grey', 'features': '108 MP sensor camera'},
        {'productName': 'LG V60 ThinQ', 'price': 899.00, 'category': 'Mobile Phone', 'shortDescription': 'Best for multitasking with dual screen option.', 'brand': 'LG', 'model': 'V60 ThinQ', 'color': 'Classy Blue', 'features': '32-bit Hi-Fi Quad DAC'},
        {'productName': 'ASUS ROG Phone 5', 'price': 999.00, 'category': 'Mobile Phone', 'shortDescription': 'Gaming powerhouse with advanced cooling.', 'brand': 'ASUS', 'model': 'ROG Phone 5', 'color': 'Phantom Black', 'features': '144 Hz display refresh rate'},
        {'productName': 'Huawei P40 Pro', 'price': 899.00, 'category': 'Mobile Phone', 'shortDescription': 'Visionary photography with Ultra Vision Leica.', 'brand': 'Huawei', 'model': 'P40 Pro', 'color': 'Silver Frost', 'features': '50x SuperSensing Zoom'}
    ],
    "Home Appliance": [
        {'productName': 'Dyson V11 Torque Drive', 'price': 599.99, 'category': 'Home Appliance', 'shortDescription': 'Intelligent cleaning with real-time reporting.', 'color': 'Nickel/Blue', 'voltage': 220, 'style': 'High Torque cleaner head'},
        {'productName': 'LG WM3900HWA Washer', 'price': 899.00, 'category': 'Home Appliance', 'shortDescription': 'Ultra-large capacity with AI Fabric sensor.', 'color': 'White', 'voltage': 110, 'style': 'SmartThinQ Technology'},
        {'productName': 'Samsung RF28R7351SG Refrigerator', 'price': 2799.00, 'category': 'Home Appliance', 'shortDescription': 'Modern design with a Food Showcase Door.', 'color': 'Black Stainless Steel', 'voltage': 110, 'style': 'FlexZone Drawer'},
        {'productName': 'KitchenAid KSM150PSER Artisan Stand Mixer', 'price': 379.00, 'category': 'Home Appliance', 'shortDescription': 'Make up to 9 dozen cookies in a single batch.', 'color': 'Empire Red', 'voltage': 110, 'style': '10-speed slide control'},
        {'productName': 'Instant Pot Duo 7-in-1 Electric Pressure Cooker', 'price': 89.00, 'category': 'Home Appliance', 'shortDescription': 'Multi-use programmable pressure cooker.', 'color': 'Stainless Steel', 'voltage': 110, 'style': '14 one-touch smart programs'},
        {'productName': 'iRobot Roomba 960', 'price': 499.99, 'category': 'Home Appliance', 'shortDescription': 'Robot vacuum with Wi-Fi Connectivity.', 'color': 'Graphite', 'voltage': 110, 'style': 'iAdapt 2.0 Navigation with vSLAM technology'},
        {'productName': 'Breville BES870XL Barista Express', 'price': 599.95, 'category': 'Home Appliance', 'shortDescription': 'Espresso machine with integrated grinder.', 'color': 'Brushed Stainless Steel', 'voltage': 110, 'style': 'Dose-Control Grinding'},
        {'productName': 'Philips HD9641/96 Airfryer', 'price': 249.95, 'category': 'Home Appliance', 'shortDescription': 'Healthy cooking with TurboStar Technology.', 'color': 'Black', 'voltage': 110, 'style': 'QuickClean basket'},
        {'productName': 'Bose QuietComfort 35 II', 'price': 299.00, 'category': 'Home Appliance', 'shortDescription': 'Wireless noise-cancelling headphones.', 'color': 'Silver', 'voltage': None, 'style': 'Alexa-enabled for voice access'},
        {'productName': 'Nest Learning Thermostat', 'price': 249.00, 'category': 'Home Appliance', 'shortDescription': 'Smart thermostat with HVAC monitoring.', 'color': 'Stainless Steel', 'voltage': None, 'style': 'Remote control through the app'}
    ],
    "Drinks": [
        {'productName': 'Pure Spring Water', 'price': 0.99, 'category': 'Drinks', 'shortDescription': 'Naturally filtered spring water.', 'volume': '500ml'},
        {'productName': 'Organic Apple Juice', 'price': 2.49, 'category': 'Drinks', 'shortDescription': 'Sweet and refreshing juice from organic apples.', 'volume': '1L'},
        {'productName': 'Fair Trade Coffee', 'price': 5.99, 'category': 'Drinks', 'shortDescription': 'Rich ground coffee with fair trade certification.', 'volume': '500g'},
        {'productName': 'Green Tea', 'price': 3.99, 'category': 'Drinks', 'shortDescription': 'Calming green tea with natural antioxidants.', 'volume': '100g'},
        {'productName': 'Chocolate Almond Milk', 'price': 3.49, 'category': 'Drinks', 'shortDescription': 'Deliciously smooth chocolate-flavored almond milk.', 'volume': '1L'}
    ],
    "Fruits": [
        {'productName': 'Honeycrisp Apples', 'price': 1.49, 'category': 'Fruits', 'shortDescription': 'Crisp, juicy apples with a sweet flavor.', 'countryOfOrigin': 'USA'},
        {'productName': 'Organic Bananas', 'price': 0.29, 'category': 'Fruits', 'shortDescription': 'Rich in potassium and naturally sweet.', 'countryOfOrigin': 'Ecuador'},
        {'productName': 'Strawberries', 'price': 2.99, 'category': 'Fruits', 'shortDescription': 'Fresh and sweet strawberries perfect for desserts.', 'countryOfOrigin': 'Mexico'},
        {'productName': 'Navel Oranges', 'price': 1.99, 'category': 'Fruits', 'shortDescription': 'Seedless and packed with Vitamin C.', 'countryOfOrigin': 'Florida'},
        {'productName': 'Blueberries', 'price': 3.49, 'category': 'Fruits', 'shortDescription': 'Antioxidant-rich and great for snacking.', 'countryOfOrigin': 'Canada'}
    ],
    "Vegetables": [
        {'productName': 'Spinach', 'price': 1.99, 'category': 'Vegetables', 'shortDescription': 'Fresh spinach leaves rich in iron.', 'countryOfOrigin': 'USA'},
        {'productName': 'Tomatoes', 'price': 2.49, 'category': 'Vegetables', 'shortDescription': 'Ripe and juicy tomatoes for salads and sandwiches.', 'countryOfOrigin': 'Mexico'},
        {'productName': 'Red Bell Peppers', 'price': 0.99, 'category': 'Vegetables', 'shortDescription': 'Sweet and crunchy, perfect for grilling.', 'countryOfOrigin': 'Netherlands'},
        {'productName': 'Cucumbers', 'price': 0.69, 'category': 'Vegetables', 'shortDescription': 'Cool and crisp cucumbers ideal for refreshing salads.', 'countryOfOrigin': 'USA'},
        {'productName': 'Garlic', 'price': 0.50, 'category': 'Vegetables', 'shortDescription': 'Aromatic garlic cloves for flavorful cooking.', 'countryOfOrigin': 'China'}
    ],
    "Bakery": [
        {'productName': 'Sourdough Bread', 'price': 3.99, 'category': 'Bakery', 'shortDescription': 'Crusty bread with a tangy flavor.', 'weight': '500g'},
        {'productName': 'Chocolate Chip Cookies', 'price': 2.49, 'category': 'Bakery', 'shortDescription': 'Soft cookies loaded with chocolate chips.', 'weight': '300g'},
        {'productName': 'Blueberry Muffins', 'price': 4.49, 'category': 'Bakery', 'shortDescription': 'Moist muffins with fresh blueberries.', 'weight': '400g'},
        {'productName': 'Croissants', 'price': 3.99, 'category': 'Bakery', 'shortDescription': 'Buttery and flaky French pastries.', 'weight': '350g'},
        {'productName': 'Bagels', 'price': 3.49, 'category': 'Bakery', 'shortDescription': 'Chewy bagels perfect for a cream cheese spread.', 'weight': '450g'}
        ]
}

# Insert the data into the products collection
for category, products in products.items():
    for product in products:
        product["category"] = category  # Add the category field to each product
    product_collection.insert_many(products)

print(f"Inserted data into products collection")