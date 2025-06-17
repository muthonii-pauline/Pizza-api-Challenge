from server.app import app
from server.models import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    db.drop_all()
    db.create_all()

    # Restaurants
    r1 = Restaurant(name="Pizza Planet", address="123 Galactic Blvd")
    r2 = Restaurant(name="Mama Mia's", address="456 Italian Street")
    r3 = Restaurant(name="Cheesy Crust", address="789 Deep Dish Ave")
    r4 = Restaurant(name="Slice City", address="321 Pepperoni Place")

    # Pizzas
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    p3 = Pizza(name="BBQ Chicken", ingredients="BBQ Sauce, Chicken, Red Onions, Cilantro")
    p4 = Pizza(name="Veggie Delight", ingredients="Bell Peppers, Olives, Mushrooms, Onions, Tomato Sauce")
    p5 = Pizza(name="Hawaiian", ingredients="Tomato Sauce, Mozzarella, Ham, Pineapple")

    db.session.add_all([r1, r2, r3, r4, p1, p2, p3, p4, p5])
    db.session.commit()

    # Restaurant-Pizza relationships
    rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=15, pizza_id=p2.id, restaurant_id=r2.id)
    rp3 = RestaurantPizza(price=13, pizza_id=p3.id, restaurant_id=r3.id)
    rp4 = RestaurantPizza(price=12, pizza_id=p4.id, restaurant_id=r4.id)
    rp5 = RestaurantPizza(price=14, pizza_id=p5.id, restaurant_id=r1.id)
    rp6 = RestaurantPizza(price=11, pizza_id=p1.id, restaurant_id=r2.id)
    rp7 = RestaurantPizza(price=16, pizza_id=p2.id, restaurant_id=r3.id)

    db.session.add_all([rp1, rp2, rp3, rp4, rp5, rp6, rp7])
    db.session.commit()

    print("✅ Seed complete with restaurants, pizzas, and relationships!")
