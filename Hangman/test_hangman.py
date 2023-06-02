import unittest
import haangman1

class TestHangman(unittest.TestCase):
    def test_get_random_guess_word(self):
        secret_word=haangman1.get_random_guess_word()
        self.assertEqual(type(secret_word),str)
        self.assertGreater(len(secret_word),6)

    def check_length_of_input_word(self):
        input_word=haangman1.check_length_of_input_word("a")
        self.assertGreater(len(input_word),1)
        
    # assert type(secret_word)==str


