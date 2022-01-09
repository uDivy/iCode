import time


def generateDocument(characters, document):
    start_time = time.time()
    # Write your code here.
    for char in document:
        if char not in characters:
            return False

        loc = characters.index(char)
        characters = characters.replace(characters[loc], "", 1)
    print("--- %s seconds ---" % (time.time() - start_time))
    return True