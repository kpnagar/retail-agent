import speech_recognition
import tools as t
from routing_layer import rl
from pynput import keyboard as kb
from gtts import gTTS
from io import BytesIO
import pygame


def on_release(key):
    pass


def listen_for_input(recognizer):
    with speech_recognition.Microphone() as mic:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)
        return recognizer.recognize_whisper(audio_data=audio, model="small.en") or input("\nYou: ")


def text_to_speech(text: str) -> None:
    tts = gTTS(text=text, lang='en')
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def process_input(message):
    print("Processing...")
    out = rl(message)
    if out.name is not None:
        response = get_response(out)
    else:
        response = t.chitchat(message)
    print(f"Agent: {response}")
    text_to_speech(response)


def get_response(out):
    response_functions = {
        'chitchat': t.chitchat,
        'product_purchase': t.product_purchase,
        'scheduled_purchase': t.schedule_purchase,
        'price_tracking': t.price_tracking,
        'order_tracking': t.order_tracking
    }
    response_function = response_functions.get(out.name)
    return response_function(**out.function_call)


def main():
    recording_started = False
    recognizer = speech_recognition.Recognizer()
    initial_message = "Hello, how may I help you with your shopping today?"
    print("Agent: ", initial_message)
    text_to_speech(initial_message)
    recording_started = False

    def on_press(key):
        nonlocal recording_started
        if key == kb.Key.space:
            if not recording_started:
                recording_started = True
                message = listen_for_input(recognizer)
                process_input(message)
            else:
                recording_started = False

    with kb.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()
