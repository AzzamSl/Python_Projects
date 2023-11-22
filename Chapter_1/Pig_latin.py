""""program that takes a word as input and return its Pig Latin equivalent"""
while True:
    word = input("Please enter a word : ")

    vowels = ('a', 'e', 'i', 'o', 'u')

    if word[0].lower() in vowels:
        word +="ay"

    else:
        word +="way"
    
    print(f"\n{word}\n")

    press = input("If you want to play again press Enter else press q : ")
    print("\n")
    if press.lower() == 'q':
        print("Thank you for playing please press enter \n")
        break