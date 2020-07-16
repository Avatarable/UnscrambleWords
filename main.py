swords = []
num = int(input("number: "))
enemy = input("Unscramble: ")

with open("dict.txt", "r") as f:
    for word in f:
        grab = []
        scram_word = [x for x in enemy.strip()]
        for char in word.strip():
            if char in scram_word:
                grab.append(char)
                scram_word.pop(scram_word.index(char))
        if len(grab) == len(word.strip()):
            swords.append(word.strip())
            if len(swords) == num:
                break

print('unscrambled words: ', swords)
