from typing import List

from semantic_router.utils import llm
import requests
import json
from schemas import Product, Order
from store import orders
from datetime import datetime
from scheduler import Scheduler

schedule = Scheduler()


def fetch_products_from_api(item: str):
    url = "https://api.escuelajs.co/api/v1/products/"
    params = {"title": item}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        products = [Product(**item) for item in data]
        if not products:
            return "Unable to find the product you're looking for..."
        print(f"The following items are available for purchase. \n{data}")
        return products
    else:
        print("Error:", response.status_code)


def get_product_of_choice(products: List[Product]):
    choice = int(input("Type the Product ID of the product of your choice: "))
    for product in products:
        if product.id == choice:
            return product


def place_scheduled_order(product, placed_at):
    print(place_order(product, placed_at))


def place_order(product, placed_at):
    order = Order(product=product, total_amount=product.price, order_date=placed_at,
                  status="processing")
    orders.append(order)
    return f"Your order for {product.title} has been placed. OrderID for your purchase is: {order.id}"


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
    products = fetch_products_from_api(item)
    product = get_product_of_choice(products)
    return place_order(product, datetime.utcnow())


def schedule_purchase(item: str, datetime_to_schedule: datetime) -> bool:
    """
    Schedule a purchase of an item at a given datetime.

    Args:
    - item (str): The name or identifier of the item to be purchased.
    - datetime_to_schedule (datetime): The datetime object indicating when the purchase should be made.

    Returns:
    - bool: True if the purchase was successfully scheduled, False otherwise.
    """
    products = fetch_products_from_api(item)
    product = get_product_of_choice(products)
    order_purchased = schedule.once(datetime_to_schedule, place_scheduled_order,
                                    kwargs={"product": product, "placed_at": datetime_to_schedule})
    if not order_purchased:
        return False
    return True
