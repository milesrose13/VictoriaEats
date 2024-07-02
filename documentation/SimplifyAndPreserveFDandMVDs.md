# Simplify and Preserve FD's and MVD's
## Simplification Goal

Calculate a minimal basis for a set of FDs to ensure a simple and efficient database design.
Evaluation Criteria

Identification and implementation of a minimal basis for FDs, confirmed through testing and peer review.
### Minimal Basis Calculation

    Remove Extraneous Attributes
        Check for and remove any extraneous attributes in the FDs.

    Remove Redundant FDs
        Ensure that each FD is necessary and cannot be inferred from other FDs.

### Minimal Basis for FDs
User

    user_id → username, email, password_hash, created_on

Reviewer

    reviewer_id → review_count
    user_id → reviewer_id

Admin

    admin_id → role
    user_id → admin_id

Restaurant

    restaurant_id → name, description, address, city, created_on

Dish

    dish_id → name, description, price, restaurant_id

Review

    review_id → title, rating, review_text, created_on, num_upvotes, user_id, restaurant_id

Tag

    tag_id → name

## FD Preservation Goal

Check if a decomposition preserves FDs and decompose relations into third normal form (3NF) when appropriate.
### Evaluation Criteria

Successful decomposition into 3NF with verification that FDs are preserved, confirmed by testing and peer review.
### 3NF Decomposition

    User:
        User(user_id, username, email, password_hash, created_on)

    Reviewer:
        Reviewer(reviewer_id, review_count, user_id)

    Admin:
        Admin(admin_id, role, user_id)

    Restaurant:
        Restaurant(restaurant_id, name, description, address, city, created_on)

    Dish:
        Dish(dish_id, name, description, price, restaurant_id)

    Review:
        Review(review_id, title, rating, review_text, created_on, num_upvotes, user_id, restaurant_id)

    Tag:
        Tag(tag_id, name)

Verification

    All decompositions preserve the original FDs.
    
## MVD Preservation Goal

MVD Check

    Identify Multi-Valued Dependencies (MVDs):
        In the schema, there are no MVDs.

    4NF Decomposition:
        Since no MVDs are identified, the current schema is already in 4NF.
