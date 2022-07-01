from random import choice


def open_and_read_file():

    open_file = open(("green-eggs.txt", "r"))

    new_list = []
    
    for line in open_file:
        line = line.rstrip().split(" ", ",")
        new_list.append(line)

    return(new_list)


def make_chains(new_list):

    word_list = open_and_read_file()

    word_chains = {}

    index = 0

    for i in range(len(word_list)):
        word_keys = (word_list[i], word_list[i + 1])


    return(word_chains)


def make_text(word_chains):
    """Return text from chains."""

    words = make_chains()


    return ' '.join(words)


def main():

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(word_chains)

print(random_text)
