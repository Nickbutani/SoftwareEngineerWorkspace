"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, file):
        self.file = file
        self.words = self.read_file()
        print(f"{len(self.words)} words read")
    def read_file(self):
        return [word.strip() for word in open(self.file)]
    def random(self): 
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    def read_file(self):
        return [word.strip() for word in open(self.file) if word.strip() and not word.startswith("#")]
    