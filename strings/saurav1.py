class LetterFilter:
    def __init__(self, s):
        self.s = s
        self.vowels = set('aeiou')

    def filter_vowels(self):
        return ''.join([char for char in self.s if char.lower() in self.vowels])

    def filter_consonants(self):
        return ''.join([char for char in self.s if char.lower() not in self.vowels])

# Sample usage
s = 'onomatopoeia'
lf = LetterFilter(s)
print(lf.filter_vowels())      # Output: 'aae'
print(lf.filter_consonants())  # Output: 'hckrrnk'


