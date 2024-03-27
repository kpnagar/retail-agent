from semantic_router import Route
from semantic_router.encoders import HuggingFaceEncoder
from semantic_router.llms.ollama import OllamaLLM
from semantic_router import RouteLayer

encoder = HuggingFaceEncoder()

llm = OllamaLLM(llm_name="gemma:2b")

chitchat = Route(
    name="chitchat",
    utterances=[
        ""
    ]
)

product_purchase = Route(
    name="product_purchase",
    utterances=[
        ""
    ]
)

scheduled_purchase = Route(
    name="scheduled_purchase",
    utterances=[
        ""
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

