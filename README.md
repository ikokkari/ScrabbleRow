# One-Dimensional Scrabble

An interesting Python programming project of Scrabble restricted on a single row that is already partially filled with letters.

Given a Scrabble row as a string such as `'--o----v---c---i--b-l--i-n-u-y-'`, the function that the students implement should return a string with some of the blanks replaced with letters under the constraint that every maximal word that appears in the returned string is a legal word in the wordlist. The goal is to maximize the total score of the row, when each word gets points both for its Scrabble value and the square of its length. For example, `'-convolvulic-trilobal-signeury-'` would be one pretty well-scoring solution for this particular instance.

Everyone who wishes to teach or learn Python is welcome to use and adapt this project for their own purposes as they see fit. The author welcomes feedback by email at `ilkka.kokkarinen@gmail.com` from computer science instructors who use this project in their courses.

The automated tester script `scrabblerun.py` is released under the [GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.txt), with no warranties implied by the author.

Wordlist `words_sorted.txt` adapted from [dwyl/english-words](https://github.com/dwyl/english-words).
