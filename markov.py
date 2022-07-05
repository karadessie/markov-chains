from random import choice


def open_and_read_file():

    file = open('green-eggs.txt')
    text_string = file.read()
    file.close()

    return text_string

def make_chains(text_string):

    chains = {}

    words = text_string.split()

    # To set a stop point, append None to the end of our word list.

    words.append(None)

    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

    return chains


def make_text(chains):
    
    key = choice(list(chains.keys()))
    words = [key[0], key[1]]
    word = choice(chains[key])

    # Keep looping until we reach a value of None
    # (which would mean it was the end of our original text)
    # Note that for long texts (like a full book), this might mean
    # it would run for a very long time.

    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])

    return ' '.join(words)

def main():

    text_string = open_and_read_file('green-eggs.txt')

    chains = make_chains(text_string)

    random_text = make_text(chains)

    print(random_text)

main()