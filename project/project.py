import os
import speech_recognition
from googletrans import Translator
import pyttsx3
from moviepy.editor import VideoFileClip, AudioFileClip
from pytube import YouTube



sr = speech_recognition.Recognizer()
engine = pyttsx3.init()


def count_words(texts):
    count_word = texts.split()
    return len(count_word)


def count_letters(texts):
    count_letter = [char for char in texts if char.isalpha()]
    return len(count_letter)


def translate_speech(target_language, text):
    try:
        translator = Translator()
        translated_text = translator.translate(text, dest=target_language)
        print(f"You said: {text}")
        print(f"Translated command: {translated_text.text}")

    except Exception as e:
        return f'Translation Error: {e}'


def recognize_your_voice(microphone):
    try:
        if microphone is None:
            return "No speech detected or microphone issue"
        sr.adjust_for_ambient_noise(microphone, duration=0.2)
        audio = sr.listen(microphone)
        return sr.recognize_google(audio)
    except speech_recognition.UnknownValueError:
        return "Speech Recognition Error: Unable to recognize speech"

def text_to_speech(text):
    try:
        engine.setProperty('rate', 120)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        return f'Text-to-Speech Error: {e}'


def convert_mp4_to_mp3():
    try:
        mp4_loc = input("Enter the location of the MP4 file: ")
        if os.path.exists(mp4_loc):
            video = VideoFileClip(mp4_loc)
            audio = video.audio
            mp3_loc = os.path.splitext(mp4_loc)[0] + ".mp3"
            audio.write_audiofile(mp3_loc)
            print("Converted successfully.")
        else:
            print("File not found.")
    except Exception as e:
        return f'MP4 to MP3 Conversion Error: {e}'


def audio_file_to_text_file(audio_file_location):
    try:
        if os.path.exists(audio_file_location):
            video = AudioFileClip(audio_file_location)
            video_loc = "temp_audio.wav"
            video.write_audiofile(video_loc)
            with speech_recognition.AudioFile(video_loc) as source:
                audio = sr.record(source)
                text = sr.recognize_google(audio)
                name_of_file = input("Name of the file: ")
                download_dir = f'C:\\Users\\er\\Documents\\gab.py\\{name_of_file}.txt'
                with open(download_dir, 'w') as file:
                    file.write(text)

                return "Audio file to text file conversion success!"
        else:
            return "Audio file not found."

    except Exception as e:
        return f'Audio File to Speech Error: {e}'
    finally:
        if os.path.exists(video_loc):
            os.remove(video_loc)

def video_file_to_text_file(video_file_location):
    try:
        if os.path.exists(video_file_location):
            video = AudioFileClip(video_file_location)
            audio_loc = "temp_audio.wav"
            video.write_audiofile(audio_loc)
            with speech_recognition.AudioFile(audio_loc) as source:
                audio = sr.record(source)
                text = sr.recognize_google(audio)
                name_of_file = input("Name of the file: ")
                download_dir = f'C:\\Users\\er\\Documents\\gab.py\\{name_of_file}.txt'
                with open(download_dir, 'w') as file:
                    file.write(text)
            os.remove(audio_loc)
            return "Video file to text file conversion success!"
        else:
            print("File not found.")
    except Exception as e:
        print(f'Video File to Text Error: {e}')


def on_progress_callback(stream, chunk, bytes_remaining):
    total_bytes = stream.filesize
    bytes_downloaded = total_bytes - bytes_remaining
    percentage = (bytes_downloaded / total_bytes) * 100
    print(f"\rDownloading... {percentage:.2f}% complete", end='')


def youtube_downloader(link, command):
    try:
        download_dir = 'C:\\Users\\er\\Documents\\gab.py'
        yt = YouTube(link, on_progress_callback=on_progress_callback)
        os.makedirs(os.path.dirname(download_dir), exist_ok=True)
        get = yt.streams.get_highest_resolution()

        print("Title:", yt.title)
        print("Author:", yt.author)
        print("Publish Date:", yt.publish_date)
        print("Description:", yt.description)


        if command == '8':
            audio_stream = yt.streams.filter(only_audio=True).first()
            if audio_stream:
                audio_stream.download(download_dir)
        else:
            get.download(download_dir)

        return 'Download successful'
    except Exception as e:
        return f'Error: {e}'

def helper():
    print("""This is a simple speech/downloader/converter code Hope you like it!.
Type the corresponding number for the command
1. Count words
2. Count letters
3. Translate to (desired language)
4. Speech to text
5. Text to speech
6. mp3 to text file
7. Download youtube video
8. Download audio file only from a youtube video
9. Convert mp4 to mp3
10. mp4 to text file""")

def main():

    helper()

    while True:
        try:

            command = input("Command: ")
            valid_command = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

            if command == 'help':
                helper()
            elif command not in valid_command:
                print("Invalid command")

            elif command == '5':
                text = input("Enter text to convert to speech: ")
                text_to_speech(text)
            elif command == '6':
                audio_file_location = input("Location of audio file: ")
                text = audio_file_to_text_file(audio_file_location)
                print(text)
            elif command == '7' or command == '8':
                link = input("link: ")
                print(youtube_downloader(link, command))
            elif command == '9':
                convert_mp4_to_mp3()
            elif command == '10':
                video_file_location = input("Location of video file: ")
                text = video_file_to_text_file(video_file_location)
                print(text)

            else:
                with speech_recognition.Microphone() as microphone:

                    print("You may now start speaking")
                    text = recognize_your_voice(microphone)

                    if command == '1':
                        num_words = count_words(text)
                        print(f"You said: {text}")
                        print(f"There are {num_words} words on what you said")
                    elif command == '2':
                        num_letters = count_letters(text)
                        print(f"You said: {text}")
                        print(f"There are {num_letters} letters in what you said")
                    elif command == '3':
                        text.strip("translate to")
                        target_lang = text.split("translate to")[1].strip()
                        translate_speech(target_lang, text)

                    elif command == '4':
                        print(f"You said: {text}")

        except KeyboardInterrupt:
            print("Goodbye")
            break
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
