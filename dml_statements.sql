-- SQL DML Statements

-- Statement 1: Insert a New User
INSERT INTO User (user_id, username, email, password_hash, created_on)
VALUES (1, 'johndoe', 'johndoe@example.com', 'hashedpassword', '2024-06-16');

-- Statement 2: Update a Restaurant's Information
UPDATE Restaurant
SET description = 'A newly renovated place with a great ambiance'
WHERE restaurant_id = 1;

-- Statement 3: Delete a Tag
DELETE FROM Tag
WHERE tag_id = 5;

-- Statement 4: Create a Review
INSERT INTO Review (review_id, title, rating, review_text, created_on, num_upvotes, user_id, restaurant_id, dish_id)
VALUES (1, 'Great Experience', 5, 'The food was amazing!', '2024-06-16', 0, 1, 1, 1);

-- Statement 5: Insert a New Dish
INSERT INTO Dish (dish_id, name, description, price)
VALUES (1, 'Sample Dish', 'A delicious sample dish', 9.99);

-- Statement 6: Update a User's Email
UPDATE User
SET email = 'newemail@example.com'
WHERE user_id = 1;

-- Statement 7: Delete a Restaurant
DELETE FROM Restaurant
WHERE restaurant_id = 1;

-- Statement 8: Upvote a Review
UPDATE Review
SET num_upvotes = num_upvotes + 1
WHERE review_id = 1;
