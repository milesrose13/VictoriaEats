**Referential Integrity Constraints Documentation**

| Parent Table |     Child Table    | Foreign Key Column | On Update | On Delete |
|:------------:|:------------------:|:------------------:|:---------:|:---------:|
| Restaurant   | Categorizes        | restaurant_id      | NO ACTION | NO ACTION |
| Tag          | Categorizes        | tag_id             | NO ACTION | NO ACTION |
| Restaurant   | Dish               | restaurant_id      | NO ACTION | SET NULL  |
| Restaurant   | Offers             | restaurant_id      | NO ACTION | NO ACTION |
| Dish         | Offers             | dish_id            | NO ACTION | NO ACTION |
| Restaurant   | Review             | restaurant_id      | NO ACTION | SET NULL  |
| User         | Review             | user_id            | NO ACTION | SET NULL  |
| Review       | ReviewedDish       | review_id          | NO ACTION | CASCADE   |
| Dish         | ReviewedDish       | dish_id            | NO ACTION | CASCADE   |
| Review       | ReviewedRestaurant | review_id          | NO ACTION | CASCADE   |
| Restaurant   | ReviewedRestaurant | restaurant_id      | NO ACTION | CASCADE   |
| User         | Writes             | user_id            | NO ACTION | NO ACTION |
| Review       | Writes             | review_id          | NO ACTION | NO ACTION |
