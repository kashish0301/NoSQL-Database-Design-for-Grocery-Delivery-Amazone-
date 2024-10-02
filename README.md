# NoSQL-Database-Design-for-Grocery-Delivery-Amazone

## Case Background
Amazone has decided to expand its operations by delivering fresh groceries. To offer same-day and instant grocery delivery service, the company has partnered with a UK groceries retailer, Morrison. This partnership will enable Amazone to do fresh and same-day grocery delivery. Amazone has decided to experiment with same-day and instant grocery delivery using Manchester. Six Morrison grocery stores have been chosen for instant pick-up and delivery by delivery drivers who are Amazon partners.

The Amazone team has contacted your team to develop a new online platform that accommodates both the existing and new business models. Your team has been provided with the following information to help with the data modelling and implementation service.

![image](https://github.com/user-attachments/assets/8fc39d49-1648-41e9-9898-6d67c3ed6930)


## Introduction
Amazone's strategic initiative aims to expand its service offerings to include fresh groceries, partnering with Morrizon, a prominent UK grocery retailer. This collaboration introduces same-day and instant grocery delivery services, initially launching in Manchester. Our team is tasked with developing an integrated online platform that seamlessly incorporates both existing and new business models, facilitating efficient operations across six selected Morrizon grocery stores, enabling instant pick-up and delivery by Amazon's partnered delivery drivers.

## Database Design and Implementation

### Entity Relationship Diagram (ERD)
The design includes:
- **Customer Schema**
  - Unique identification using `ObjectId`.
  - Supports multiple addresses.
  - References to past and current orders, ratings, and recommended products.
  
- **Order Schema**
  - Direct link to customers.
  - Detailed order items linked to product ID and quantity.
  
- **Product Schema**
  - Unique product identification and attributes.
  - Inventory tracking linked to warehouse locations.
  
- **Warehouse Schema**
  - Location-based organization for inventory distribution.
  - Links to stored products.
  
- **Rating Schema**
  - Connections to customers and products for feedback collection.
  
- **Partner (Delivery) Schema**
  - Real-time location tracking for delivery management.
  
- **Store Schema**
  - Physical address and geolocation for optimized routing.
  - Inventory details for available grocery items.

## Collections and Sample Data

### Products Collection
- **Key Attributes**: Uses Faker library for data insertion, including product dimensions, country of origin, etc.
- **Product Categories**: Other and Fresh.

### Customers Collection
- **Key Attributes**: Includes multiple addresses, current orders, and past orders references.
- **Dynamic Recommendations**: Updates based on top-rated products.

### Orders Collection
- **Attributes**: Includes `totalCost`, `orderDate`, `transit status`, and `orderItems`.

### Ratings Collection
- **Attributes**: Includes `score`, `comment`, and `ratingDate`.

### Stores Collection
- **Attributes**: Includes `storeID`, address, geolocation, and available grocery items.

### Warehouse Collection
- **Attributes**: Includes `warehouseID`, address, and stored products.

### Partners Collection
- **Attributes**: Includes current location, delivery status, and statistics.

### Payments Collection
- **Attributes**: Includes `paymentID`, `orderID`, and `paymentMethod`.

## Queries

### Sample Queries Implemented
1. **Query 1(a)**: Efficient Partner Allocation based on location and ratings.
2. **Query 1(b)**: Optimized Fresh Product Delivery System.
3. **Query 2**: User searching for available fresh products near their location.
4. **Query 3**: Customers adding products to the cart and making payments.
5. **Query 4(a)**: Manager checking inventory performance using visualizations.
6. **Query 4(b)**: Manager checking sales performance visualized by month.
7. **Query 5**: Filtering stores with low stock levels and identifying top customers.

## Visualizations
- Utilized `matplotlib` for visualizing sales and inventory performance.

## Conclusion
The project effectively combines database design, querying, and visualization to create an integrated online platform for Amazone's grocery delivery service.

## Acknowledgments
Thank you to all team members for their contributions to this project.

