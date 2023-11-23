"""Map letters from string into dictionary & print bar chart of frequency."""
import pprint
from collections import defaultdict

TEXT = 'Like the castle in its corner in a medieval game, I foresee terrible \
trouble and I stay here just the same.'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
mapped = defaultdict(list)
for character in TEXT:
    character = character.lower()
    if character in ALPHABET:
        mapped[character].append(character)
print("text = ", end='')
print(f"\n{TEXT}")
pprint.pprint(mapped, width=120)
