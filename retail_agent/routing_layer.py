from semantic_router import Route
from semantic_router.encoders import HuggingFaceEncoder
from semantic_router.llms.ollama import OllamaLLM
from semantic_router import RouteLayer

encoder = HuggingFaceEncoder()

llm = OllamaLLM(llm_name="gemma:2b")

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
        ]
    )

product_purchase = Route(
    name="product_purchase",
    utterances=[
    ]
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
    ]
)

price_tracking = Route(
    name="price_tracking",
    utterances=[
        ""
    ]
)

order_tracking = Route(
    name="order_tracking",
    utterances=[
        ""
    ]
)

routes = [chitchat, product_purchase, scheduled_purchase, price_tracking, order_tracking]

rl = RouteLayer(encoder=encoder, routes=routes, llm=llm)

