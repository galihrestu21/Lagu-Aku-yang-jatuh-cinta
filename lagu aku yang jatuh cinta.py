import sys
from time import sleep

def print_lyrics():
    line = [
        ("aku yang jatuh cinta", 0.06),
        ("haruskah kau beri kuberi kesempatan", 0.07),
        ("ingin aku jadi kekasih yang baik", 0.07),
        ("berikan aku kesempatan ohh...", 0.08),
        ("tahukah dirimu, tahukah hatimu?", 0.06),
        ("berulang kuketuk aku, aku mencintaimu", 0.08),
        ("tapi dirimu, tak pernah sadari", 0.08),
        ("aku yang jatuh cinta", 0.06)
    ]
    delays = [2.5, 3, 2.5, 7.5, 3.5, 4, 3.2, 3.5]

    for  i, (line, char_delay) in enumerate(line):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        sleep(delays[i])
        print('')

print_lyrics()