def load(file):
    try:
        with open("2of4brif.txt") as the_file:
            texts = the_file.read().strip().split("\n")
            texts = [x.lower() for x in texts]
            return texts
    except IOError as n:
        print(f"{n} :c ould not open the file")
    
    

file = "2of4brif.txt"
texts = load(file)
palindromes = []   
for text in texts:
    if text == text[::-1]:
        palindromes.append(text)

print(palindromes)