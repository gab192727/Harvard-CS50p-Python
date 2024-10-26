import unittest
from unittest.mock import patch
import io
from project import (
    count_words,
    count_letters,
    translate_speech,
    recognize_your_voice,
    text_to_speech,
)


class TestSpeechYouTubeDownloader(unittest.TestCase):

    def test_count_words(self):
        text = "Hello world! This is a test."
        self.assertEqual(count_words(text), 6)

    def test_count_letters(self):
        text = "Hello world! This is a test."
        self.assertEqual(count_letters(text), 21)

    @patch('builtins.input', return_value='translate to French Hello world')
    def test_translate_speech(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            translate_speech('fr', 'Hello world')
            self.assertEqual(mock_stdout.getvalue().strip(), 'You said: Hello world\nTranslated command: Bonjour le monde')

    @patch('builtins.input', return_value='Hello world')
    def test_recognize_your_voice(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            recognize_your_voice(None)
            self.assertEqual(mock_stdout.getvalue().strip(), '')

    @patch('builtins.input', return_value='Hello world')
    def test_text_to_speech(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            text_to_speech('Hello world')
            self.assertEqual(mock_stdout.getvalue().strip(), '')


if __name__ == '__main__':
    unittest.main()
