**FUNCTIONAL DEPENDENCIES:**

    User:
    - user_id → username, email, password_hash, created_on
    
    Review:
        -review_id → title, rating, created_on, review_text, num_upvotes
        -review_id, user_id → title, rating, created_on, review_text, num_upvotes
        -review_id, restaurant_id → title, rating, created_on, review_text, num_upvotes
    
    Dish:
        -dish_id → name, description, price
    
    Restaurant:
        -restaurant_id → name, description, address, city, created_on
    
    Tag:
       -tag_id → name


   
**Lets check if all FDs are in BCNF, meaning the left side of each FD is a superkey:**

    User:
        -user_id is a primary key, and all FDs have user_id as the left side. No BCNF violation here.

    Review:
        review_id is the primary key. However, for FDs like review_id, user_id → title, rating, created_on, review_text, num_upvotes, review_id, restaurant_id → title, rating, created_on, review_text, num_upvotes, review_id should be a superkey. We need to check if combining review_id with user_id or restaurant_id affects the BCNF compliance. If review_id alone determines all other attributes, there is no violation.

    Dish:
        dish_id is the primary key, and all FDs have dish_id as the left side. No BCNF violation here.

    Restaurant:
        restaurant_id is the primary key, and all FDs have restaurant_id as the left side. No BCNF violation here.

    Tag:
        tag_id is the primary key, and all FDs have tag_id as the left side. No BCNF violation here.

**Verify keys in relationships:**

  Writes (User writes Review)

    Composite Key: user_id, review_id
    This relationship is correct since a user can write multiple reviews, and each review is associated with a user.

Reviewed In (Review is about a Dish in a Restaurant)

    Composite Key: review_id, dish_id, restaurant_id
    This is correct as it captures the review context fully.

Offers (Restaurant offers Dish)

    Composite Key: restaurant_id, dish_id
    This is correct since a restaurant can offer multiple dishes, and each dish can be offered by multiple restaurants.

Categorizes (Restaurant categorizes Dish with Tag)

    Composite Key: restaurant_id, dish_id, tag_id
    This captures the category context fully.

**TO DO:**
Verify decomposed tables are correct by preforming natural joins for example: 

SELECT *
FROM User
NATURAL JOIN Review;
