"""Map letters from string into dictionary & print bar chart of frequency."""
import pprint
from collections import defaultdict

text = 'Like the castle in its corner in a medieval game, I foresee terrible \
trouble and I stay here just the same.'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
mapped = defaultdict(list)
for character in text:
    character = character.lower()
    if character in ALPHABET:
        mapped[character].append(character)
print("text = ", end='')
print(f"\n{text}")
pprint.pprint(mapped, width=120)