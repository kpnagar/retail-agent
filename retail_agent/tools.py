from semantic_router.utils import llm
import requests
import json
from schemas import Product, Order
from store import orders
from datetime import datetime


def chitchat(user_query: str) -> str:
    """
    Do simple chitchat with user respectfully and honestly.

    :param user_query: The query provided by the user.
    :type user_query: str
    :return: Respectful response of user's query in string format
    """
    return llm.llm(user_query)


def product_purchase(item: str) -> str:
    """
    Use this when user wants to purchase a product.
    :param item: Type of item user wants to buy eg. phone, table etc
    :return order_id: ID of the order placed by the user
    """

    url = "https://api.escuelajs.co/api/v1/products/"
    params = {"title": item}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        products = [Product(**item) for item in data]
        if not products:
            return "Unable to find the product you're looking for..."
        print(f"The following items are available for purchase. \n{data}")
        choice = int(input("Type the Product ID of the product of your choice: "))
        for product in products:
            if product.id == choice:
                order = Order(product=product, total_amount=product.price, order_date=datetime.utcnow(),
                              status="processing")
                orders.append(order)
                return f"Your order for {product.title} has been placed. OrderID for your purchase is: {order.id}"
    else:
        print("Error:", response.status_code)
