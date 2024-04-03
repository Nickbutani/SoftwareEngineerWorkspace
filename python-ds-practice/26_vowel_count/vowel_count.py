def vowel_count(phrase):
    return {letter: phrase.count(letter) for letter in phrase if letter.lower() in "aeiou"}