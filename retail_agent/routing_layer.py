from semantic_router import Route
from semantic_router.encoders import HuggingFaceEncoder
from semantic_router import RouteLayer
from semantic_router.utils.function_call import get_schema
import tools as t
from semantic_router.llms.ollama import OllamaLLM

encoder = HuggingFaceEncoder(name="sentence-transformers/all-MiniLM-L6-v2")

llm = OllamaLLM(llm_name="mistral")

chitchat = Route(
    name="chitchat",
    utterances=[
        "Hi",
        "How are you?",
        "What's up?",
        "Hello",
        "Heyaa",
        "Good morning",
        "Good afternoon",
        "Hey there",
        "How's it going?",
        "What's new?",
        "Long time no see"
    ],
    function_schema=get_schema(t.chitchat)
)

product_purchase = Route(
    name="product_purchase",
    utterances=[
        "I want to buy a phone",
        "Order a box of cereals for me",
        "Buy me a Tshirt",
        "which earphones should I buy",
        "What is the price of a ...",
        "I'm interested in purchasing a smartwatch.",
        "Where can I buy a good bookshelf?",
        "I need to buy a new backpack for school.",
        "Could you find me a good deal on a blender?",
        "Can you get me a pair of sneakers?"
    ],
    function_schema=get_schema(t.product_purchase)
)

scheduled_purchase = Route(
    name="scheduled_purchase",
    utterances=[
        "Schedule a purchase for [specific date/time]",
        "I want to buy [product] on [specific date/time]",
        "Can you set up a purchase for [specific date/time]?",
        "Remind me to buy [product] on [specific date/time]",
        "Book a purchase for [specific date/time]",
        "I need to make a purchase on [specific date/time]",
        "Add [product] to my shopping list for [specific date/time]",
        "Arrange a purchase for [specific date/time]",
        "Put in an order for [product] on [specific date/time]",
        "Schedule buying [product] for [specific date/time]"
    ],
    function_schema=get_schema(t.schedule_purchase)
)

price_tracking = Route(
    name="price_tracking",
    utterances=[
        "Track the price of [product]",
        "Notify me when the price of [product] drops",
        "Alert me if there's a price reduction for [product]",
        "Let me know when the price of [product] decreases",
        "Keep me updated on any price cuts for [product]",
        "Inform me of any discounts on [product]",
        "Notify me of any price reductions for [product]",
        "I'm interested in receiving updates about price reductions for [product]",
        "Please alert me if [product] becomes cheaper",
        "Notify me of price changes for [product]",
        "Keep me informed about price drops for [product]",
        "Inform me when the price of [product] decreases",
        "Please let me know if there's a price decrease for [product]"
    ],
    function_schema=get_schema(t.price_tracking)
)

order_tracking = Route(
    name="order_tracking",
    utterances=[
        "How can I track my order?",
        "Where has my order reached?",
        "When will I get my Shirt that i ordered yesterday?",
        "How long do i have to wait for my perfume?",
        "What is the status of my order",
        "Give me the tracking details of my order",
        "Where's my delivery at right now?",
        "I ordered a book yesterday, when can I expect it?",
        "What's the expected delivery date for the watch I bought?",
        "I'm curious about the shipping status of my electronics order."
    ],
    function_schema=get_schema(t.order_tracking)
)

routes = [chitchat, product_purchase, scheduled_purchase, price_tracking, order_tracking]

rl = RouteLayer(encoder=encoder, routes=routes, llm=llm)
