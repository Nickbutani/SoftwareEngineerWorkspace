"""Word Finder: finds random words from a dictionary."""
import random       

class WordFinder:
    def __init__(self, file_path):
        self.words = self.read_words_from_file(file_path)
        print(f"{len(self.words)} words read")

    def read_words_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                words = [line.strip() for line in file]
            return words
        except FileNotFoundError:
            print("File not found.")
            return []

    def random(self):
        return random.choice(self.words) if self.words else None

class SpecialWordFinder(WordFinder):
    def read_words_from_file(self, file_path):
        return super().read_words_from_file(file_path) if file_path else []

    def random(self):
        return random.choice([word for word in self.words if word and not word.startswith("#")]) if self.words else None
    
# wf = WordFinder("words.txt")
# print(wf.random())

# swf = SpecialWordFinder("words.txt")
# print(swf.random())

