import tools as t
from routing_layer import rl
import speech_recognition

recognizer = speech_recognition.Recognizer()
print("Agent: Hello, how may i help you with your shopping today?")
while True:
    try:
        with speech_recognition.Microphone() as mic:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_whisper(audio_data=audio, model="small.en")
            if text:
                message = text
            else:
                message = input("\nYou: ")
            print("Processing...")
            out = rl(message)
            print(f"Evaluating task: {out.name}")
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
    except Exception:
        recognizer = speech_recognition.Recognizer()
        continue
