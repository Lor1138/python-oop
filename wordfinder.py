"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:

    """
    >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog
    """
    def __init__(self, file):
        
        """Read file and says number of words read."""

        word_file = open(file)

        self.words = self.extract(word_file)

        print(f"{len(self.words)} words read")
        
        
    def extract(self, word_file):
        """Extract word_file and turn into list of words."""

        lines=word_file.readlines()
        lines=[line.strip() for line in lines]
        return (lines)
    
    def random(self):
        """Uses random module to select a random word from word_file"""
        
        return random.choice(self.words)

   
        




    
