import speech_recognition
from loguru import logger as log


def record_and_recognize_audio(*args: tuple):

    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    with microphone:
        recognizer.adjust_for_ambient_noise(microphone, duration=2)
        try:
            log.debug('Start >>')
            audio = recognizer.listen(microphone, 5, 5)
            recognized_data = recognizer.recognize_google(audio, language="en").lower()
        except speech_recognition.WaitTimeoutError:
            log.error('Can you check if your microphone is on, please?')
            return
        except speech_recognition.UnknownValueError:
            pass
        except speech_recognition.RequestError:
            log.error('Check your Internet Connection, please')
        finally:
            log.debug('The end >> ')

        return recognized_data



if __name__ == "__main__":

    while True:
        voice_input = record_and_recognize_audio()
        log.success(voice_input)
