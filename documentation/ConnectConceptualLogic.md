# Connects Conceptual-Logical

## Goal
Translate functional dependencies (FDs) from an ERD and reverse engineer the relations back into an ERD.

## Evaluation Criteria
Successful translation and reverse engineering of FDs, with verification through comparison with the original ERD.

## Identify Functional Dependencies from ERD

#### User
- `user_id` → `username, email, password_hash, created_on`

#### Reviewer
- `reviewer_id` → `review_count, user_id`
- `user_id` → `reviewer_id`

#### Admin
- `admin_id` → `role, user_id`
- `user_id` → `admin_id`

#### Restaurant
- `restaurant_id` → `name, description, address, city, created_on`

#### Dish
- `dish_id` → `name, description, price, restaurant_id`
- `restaurant_id, name` → `dish_id, description, price`

#### Review
- `review_id` → `title, rating, review_text, created_on, num_upvotes, user_id, restaurant_id`

#### Tag
- `tag_id` → `name`

#### Relationships
- `Writes: user_id, review_id` → `user_id, review_id`
- `Reviewed In: review_id, restaurant_id` → `review_id, restaurant_id`
- `Offers: restaurant_id, dish_id` → `restaurant_id, dish_id`
- `Categorizes: restaurant_id, tag_id` → `restaurant_id, tag_id`

## Translate Functional Dependencies to Relations
```sql
#### User

User(user_id, username, email, password_hash, created_on)

### Reviewer

Reviewer(reviewer_id, review_count, user_id)

### Admin

Admin(admin_id, role, user_id)

### Restaurant

Restaurant(restaurant_id, name, description, address, city, created_on)

### Dish

Dish(dish_id, name, description, price, restaurant_id)

### Review

Review(review_id, title, rating, review_text, created_on, num_upvotes, user_id, restaurant_id)

### Tag

Tag(tag_id, name)

### Relationships

Writes(user_id, review_id)
ReviewedIn(review_id, restaurant_id)
Offers(restaurant_id, dish_id)
Categorizes(restaurant_id, tag_id)
```
## Reverse Engineer the Relations Back into an ERD
### Entities and Attributes
User

    Attributes: user_id (PK), username, email, password_hash, created_on
    Subtypes: Reviewer, Admin

Reviewer

    Attributes: reviewer_id (PK), review_count, user_id (FK)

Admin

    Attributes: admin_id (PK), role, user_id (FK)

Restaurant

    Attributes: restaurant_id (PK), name, description, address, city, created_on

Dish

    Attributes: dish_id (PK), name, description, price, restaurant_id (FK)

Review

    Attributes: review_id (PK), title, rating, review_text, created_on, num_upvotes, user_id (FK), restaurant_id (FK)

Tag

    Attributes: tag_id (PK), name

### Relationships

    Writes: between User and Review
    Reviewed In: between Review and Restaurant
    Offers: between Restaurant and Dish
    Categorizes: between Restaurant and Tag

## Reconstructed ERD
I'm sorry I'm not going to recreate our ERD from scratch but it will look like this:
![UPDATED_ERD drawio](https://github.com/milesrose13/csc370project/assets/106453865/92f30512-1552-48d4-8e8b-313049c39823)
