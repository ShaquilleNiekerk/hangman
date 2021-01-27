import unittest
import hangman
from io import StringIO
from unittest.mock import patch

class Test_Hangman(unittest.TestCase):


    @patch('sys.stdin', StringIO("Y\n"))
    def test_step1_difficulty_fail(self):
        with patch(('sys.stdout'), new = StringIO()):            
            output = hangman.select_difficulty()
            self.assertEqual("Invalid", output)


    @patch('sys.stdin', StringIO("E\n"))
    def test_step1_difficulty_pass_easy(self):
        with patch(('sys.stdout'), new = StringIO()):            
            output = hangman.select_difficulty()
            self.assertEqual("Easy.txt", output)


    @patch('sys.stdin', StringIO("M\n"))
    def test_step1_difficulty_pass_medium(self):
        with patch(('sys.stdout'), new = StringIO()):            
            output = hangman.select_difficulty()
            self.assertEqual("Medium.txt", output)


    @patch('sys.stdin', StringIO("H\n"))
    def test_step1_difficulty_pass_hard(self):
        with patch(('sys.stdout'), new = StringIO()):            
            output = hangman.select_difficulty()
            self.assertEqual("Hard.txt", output)


    def test_step2_read_file(self):
        output = hangman.read_file('test.txt')
        self.assertEqual(['Success\n', 'Success'], output)


    def test_step3_choose_word(self):
        word_list = hangman.read_file('test.txt')
        output = hangman.choose_word(word_list)
        self.assertEqual('Success', output)


    def test_step4_hide_chars(self):
        for _ in range(0, 100):
            count = 0
            output = hangman.hide_chars('abcd')
            for x in output:
                if x == '_':
                    count += 1
            self.assertEqual(3, count)

    
    def test_step5_fill_char(self):
        self.assertEqual('ab_', hangman.fill_in_char('abc', 'a__', 'b'))
        self.assertEqual('a__', hangman.fill_in_char('abc', 'a__', 'a'))
        self.assertEqual('a__', hangman.fill_in_char('abc', 'a__', 'd'))

    
    def test_step6_draw_hangman(self):
            self.assertEqual('\n/----\n|\n|\n|\n|\n_______', 
                            hangman.draw_figure(4))
            self.assertEqual('\n/----\n|   0\n|\n|\n|\n_______', 
                            hangman.draw_figure(3))
            self.assertEqual('\n/----\n|   0\n|   |\n|   |\n|\n_______', 
                            hangman.draw_figure(2))
            self.assertEqual('\n/----\n|   0\n|  /|\\\n|   |\n|\n_______', 
                            hangman.draw_figure(1))
            self.assertEqual('\n/----\n|   0\n|  /|\\\n|   |\n|  / \\\n_______', 
                            hangman.draw_figure(0))