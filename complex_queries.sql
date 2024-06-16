-- Complex SQL Queries

-- Query 1: View All Restaurants
SELECT * FROM Restaurant;

-- Query 2: View a Restaurant's Menu of Dishes
SELECT Dish.dish_id, Dish.name, Dish.description, Dish.price
FROM Dish
JOIN Offers ON Dish.dish_id = Offers.dish_id
WHERE Offers.restaurant_id = 1; -- Replace with the specific restaurant_id

-- Query 3: Search for a Restaurant by Name
SELECT * FROM Restaurant
WHERE name LIKE '%RestaurantName%'; -- Replace 'RestaurantName' with the search term

-- Query 4: Search for Restaurants Matching Certain Criteria (Location, Rating, Tags, Menu Item)
SELECT DISTINCT Restaurant.restaurant_id, Restaurant.name, Restaurant.description, Restaurant.address, Restaurant.city
FROM Restaurant
LEFT JOIN Review ON Restaurant.restaurant_id = Review.restaurant_id
LEFT JOIN Categorizes ON Restaurant.restaurant_id = Categorizes.restaurant_id
LEFT JOIN Tag ON Categorizes.tag_id = Tag.tag_id
LEFT JOIN Offers ON Restaurant.restaurant_id = Offers.restaurant_id
LEFT JOIN Dish ON Offers.dish_id = Dish.dish_id
WHERE (Restaurant.city = 'CityName' OR Tag.name = 'TagName' OR Review.rating >= 4 OR Dish.name LIKE '%MenuItem%'); -- Replace with specific criteria

-- Query 5: View Restaurant Reviews
SELECT * FROM Review
WHERE restaurant_id = 1; -- Replace with the specific restaurant_id

-- Query 6: View Specific Dish Reviews
SELECT * FROM Review
WHERE dish_id = 1; -- Replace with the specific dish_id

-- Query 7: Upvote a Restaurant Review
UPDATE Review
SET num_upvotes = num_upvotes + 1
WHERE review_id = 1; -- Replace with the specific review_id

-- Query 8: Top 5 Restaurants by Average Rating
SELECT Restaurant.restaurant_id, Restaurant.name, AVG(Review.rating) as avg_rating
FROM Restaurant
JOIN Review ON Restaurant.restaurant_id = Review.restaurant_id
GROUP BY Restaurant.restaurant_id, Restaurant.name
ORDER BY avg_rating DESC
LIMIT 5;

-- Query 9: Most Reviewed Dishes
SELECT Dish.dish_id, Dish.name, COUNT(Review.review_id) as review_count
FROM Dish
JOIN Review ON Dish.dish_id = Review.dish_id
GROUP BY Dish.dish_id, Dish.name
ORDER BY review_count DESC
LIMIT 5;

-- Query 10: Search Users by Username
SELECT * FROM User
WHERE username LIKE '%johndoe%'; -- Replace 'johndoe' with the search term

-- Query 11: Reviews Containing Specific Keywords
SELECT * FROM Review
WHERE review_text LIKE '%amazing%'; -- Replace 'amazing' with the keyword
