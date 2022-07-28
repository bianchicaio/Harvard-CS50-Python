
def main():
    phrase = input('write a phrase: ')
    playback(phrase)


def playback(phrase):
    new_phrase = phrase.replace(' ', '...')
    print(new_phrase)


main()