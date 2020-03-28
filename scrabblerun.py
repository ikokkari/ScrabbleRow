# Version March 28, 2020
# Ilkka Kokkarinen, ilkka.kokkarinen@gmail.com

import scrabblerow as sr
from random import Random

# Separator character denoting a blank space.
sep = '-'

# Seed for the random number generator that produces the patterns.
seed = 7373

# Minimum and maximum length of words we consider.
minlen, maxlen = 4, 30

# How many rounds to play this game.
rounds = 10

# Maximum possible consecutive run of blanks in the pattern.
maxblanks = 5

# Scrabble letter values.
letters = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1,
           'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1,
           's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10 }

# Word scoring function for scrabble.

def scrabble_value(word):
    if minlen <= len(word) <= maxlen:
        return sum(letters.get(c, 0) for c in word)
    else:
        return 0

def length_squared(word):
    if minlen <= len(word) <= maxlen:
        return len(word) ** 2
    else:
        return 0
    
def create_pattern(n, rng, valuef):
    prev, result, blanks = '', '', 0
    for i in range(n):
        if blanks < maxblanks and (prev != sep or rng.randint(0, 99) < 50):
            prev = sep
            blanks += 1
        else:
            prev = rng.choice('abcdefhijklmnopqrstuvwxyz')
            blanks = 0
        result += prev
    return result
    
def random_solvable_pattern2(n, rng, valuef):
    sol = ''
    while len(sol) < n:        
        next_word = rng.choice(words)
        if len(next_word) < 6:
            sol += sep if len(sol) > 0 else ''
            sol += next_word
    result, blanks, letters = '', 0, 0
    for c in sol:
        if letters == 1 or c == sep or (blanks < maxblanks and rng.randint(0, 99) < 50):
            result += sep
            letters, blanks = 0, blanks + 1
        else:
            result += c
            letters, blanks = letters + 1, 0
    #if verbose:
    #    print(f"Origin : '{sol}' ({score_answer(sol, sol, valuef)})")
    return result

def score_answer(result, pattern, scoring_f):
    curr, score = '', 0
    for (pos, (c1, c2)) in enumerate(zip(result + sep, pattern + sep)):
        if c2 != sep and c1 != c2:
            print(f"\nPATTERN MISMATCH AT POSITION {pos}!")
            return 0
        if c1 == sep:
            if curr in wordset:                    
                score += scoring_f(curr)
            elif len(curr) > 1:
                print(f"\nUNKNOWN WORD {curr} AT POSITION {pos}")
                return 0
            curr = ''
        else:
            curr += c1
    return score

def play_one_round(pattern, scoring_f):    
    score = 0
    print(f"\nPattern: {pattern}")
    try:
        result = sr.fill_words(pattern, words, scoring_f, minlen, maxlen)
    except Exception as e:
        print(f"CRASH! {e}")
        return 0
    print(f"Result : {result} ", end ='')    
    if len(result) == len(pattern):
        score += score_answer(result, pattern, scoring_f)
    else:
        print(f"\nRESULT AND PATTERN LENGTHS DIFFERENT!")
    print(f"({score})")
    return score
    
def play():
    print(f"scrabblerun with seed={seed} and rounds={rounds}.")
    scoring_f = lambda w: length_squared(w) + scrabble_value(w)
        
    # Just in case you want to try out some test cases of your own.
    testcases = []
    for pattern in testcases:
        play_one_round(pattern, scoring_f)
    
    total, rng = 0, Random(seed)
    for r in range(rounds):
        pattern = create_pattern(30 + r // 5, rng, scoring_f)
        total += play_one_round(pattern, scoring_f)
    print(f"{total} {sr.author()} {sr.student_id()}")

f = open('words_sorted.txt', 'r', encoding='utf-8')
words = [x.strip() for x in f]
words = [x for x in words if minlen <= len(x) <= maxlen]
f.close()

wordset = set(words)
play()