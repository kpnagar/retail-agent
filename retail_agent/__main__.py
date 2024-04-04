import keyboard
import speech_recognition
import tools as t
from routing_layer import rl


def main():
    recognizer = speech_recognition.Recognizer()
    print("Agent: Hello, how may I help you with your shopping today?")
    recording_started = False

    while True:
        try:
            event = keyboard.read_event(suppress=True)
            if event:
                if event.event_type == keyboard.KEY_DOWN:
                    if not recording_started:
                        recording_started = True
                        message = listen_for_input(recognizer)
                        process_input(message)
                elif event.event_type == keyboard.KEY_UP and recording_started:
                    recording_started = False
        except Exception as e:
            recognizer = speech_recognition.Recognizer()
            recording_started = False
            print(f"An error occurred: {e}")
            continue


def listen_for_input(recognizer):
    with speech_recognition.Microphone() as mic:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)
        return recognizer.recognize_whisper(audio_data=audio, model="small.en") or input("\nYou: ")


def process_input(message):
    print("Processing...")
    out = rl(message)
    response = get_response(out)
    print(f"Agent: {response}")


def get_response(out):
    response_functions = {
        'chitchat': t.chitchat,
        'product_purchase': t.product_purchase,
        'scheduled_purchase': t.schedule_purchase,
        'price_tracking': t.price_tracking,
        'order_tracking': t.order_tracking
    }
    response_function = response_functions.get(out.name, t.chitchat)
    return response_function(**out.function_call)


if __name__ == "__main__":
    main()
