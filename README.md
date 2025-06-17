# Pizza API Challenge

## Setup Steps

1. Clone the repository and navigate to the project directory.

2. Install dependencies using pipenv:

```bash
pipenv install
```

3. Activate the pipenv shell:

```bash
pipenv shell
```

4. Run the Flask application:

```bash
python -m server.app
```

The app will run by default on `http://127.0.0.1:5000`.

---

## Database Migration & Seeding Instructions

1. Initialize the migration environment (only needed once):

```bash
flask db init
```

2. Generate a migration script after model changes:

```bash
flask db migrate -m "Migration message"
```

3. Apply migrations to the database:

```bash
flask db upgrade
```

4. Seed the database with initial data:

```bash
python -m server.seed
```

This will drop all tables, recreate them, and populate with sample restaurants, pizzas, and their relationships.

---

## Route Summary

| Method | Endpoint                | Description                          |
|--------|-------------------------|------------------------------------|
| GET    | /restaurants            | Get all restaurants                 |
| GET    | /restaurants/<id> | Get a single restaurant by ID       |
| DELETE | /restaurants/<id> | Delete a restaurant by ID            |
| GET    | /pizzas                | Get all pizzas                     |
| POST   | /restaurant_pizzas      | Create a restaurant-pizza relation |

---

## Example Requests & Responses

### Get All Restaurants

**Request:**

```http
GET /restaurants HTTP/1.1
Host: localhost:5000
```

**Response:**

```json
[
  {
    "id": 1,
    "name": "Pizza Planet",
    "address": "123 Galactic Blvd"
  },
  {
    "id": 2,
    "name": "Mama Mia's",
    "address": "456 Italian Street"
  }
]
```

---

### Get Single Restaurant

**Request:**

```http
GET /restaurants/1 HTTP/1.1
Host: localhost:5000
```

**Response:**

```json
{
  "id": 1,
  "name": "Pizza Planet",
  "address": "123 Galactic Blvd",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Tomato, Mozzarella, Basil"
    },
    {
      "id": 5,
      "name": "Hawaiian",
      "ingredients": "Tomato Sauce, Mozzarella, Ham, Pineapple"
    }
  ]
}
```

---

### Delete Restaurant

**Request:**

```http
DELETE /restaurants/1 HTTP/1.1
Host: localhost:5000
```

**Response:**

Status Code: 204 No Content

---

### Get All Pizzas

**Request:**

```http
GET /pizzas HTTP/1.1
Host: localhost:5000
```

**Response:**

```json
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato, Mozzarella, Basil"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Tomato, Mozzarella, Pepperoni"
  }
]
```

---

### Create RestaurantPizza

**Request:**

```http
POST /restaurant_pizzas HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
  "price": 12,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

**Response:**

Status Code: 201 Created

```json
{
  "id": 1,
  "price": 12,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato, Mozzarella, Basil"
  },
  "restaurant": {
    "id": 2,
    "name": "Mama Mia's",
    "address": "456 Italian Street"
  }
}
```

---

## Validation Rules

- For `POST /restaurant_pizzas`, the JSON body must include:
  - `price` (number)
  - `pizza_id` (integer, must reference an existing pizza)
  - `restaurant_id` (integer, must reference an existing restaurant)
- If required fields are missing or invalid, the API returns a 400 status with error messages.
- For `GET` and `DELETE` requests with IDs, if the resource is not found, a 404 status with an error message is returned.

---

## Postman Usage Instructions

1. Import the provided Postman collection file `challenge-1-pizzas.postman_collection.json` into Postman.

2. Use the pre-defined requests to interact with the API endpoints.

3. Modify request parameters or bodies as needed to test different scenarios.

---
