import tools as t
from routing_layer import rl

print("Agent: Hello, how may i help you with your shopping today?")
while True:
    message = input("\nYou: ")
    out = rl(message)
    print(out.name)
    match out.name:
        case 'chitchat':
            print(f"Agent: {t.chitchat(**out.function_call)}")
        case 'product_purchase':
            print(f"Agent: {t.product_purchase(**out.function_call)}")
        case 'scheduled_purchase':
            print(f"Agent: {t.schedule_purchase(**out.function_call)}")
        case 'price_tracking':
            print(f"Agent: {t.price_tracking(**out.function_call)}")
        case 'order_tracking':
            print(f"Agent: {t.order_tracking(**out.function_call)}")
        case _:
            print(f"Agent: {t.chitchat(message)}")
