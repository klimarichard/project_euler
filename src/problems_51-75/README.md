## Problems 51 - 75
### 51 - Prime digit replacements
By replacing the 1<sup>st</sup> digit of the `2`-digit number `*3`, it turns out that
six of the nine possible values: `13`, `23`, `43`, `53`, `73`, and `83`, are all prime.\
\
By replacing the 3<sup>rd</sup> and 4<sup>th</sup> digits of `56**3` with the same digit,
this `5`-digit number is the first example having seven primes among the ten generated
numbers, yielding the family: `56003`, `56113`, `56333`, `56443`, `56663`, `56773`, and
`56993`. Consequently `56003`, being the first member of this family, is the smallest
prime with this property.\
\
Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.

### 52 - Permuted multiples
It can be seen that the number, `125874`, and its double, `251748`,
contain exactly the same digits, but in a different order.\
\
Find the smallest positive integer, `x`, such that `2x`, `3x`, `4x`,
`5x`, and `6x`, contain the same digits.

### 53 - Combinatoric selections
There are exactly ten ways of selecting three from five, `12345`:

<p align="center">
<code>123</code>, <code>124</code>, <code>125</code>, <code>134</code>,
<code>135</code>, <code>145</code>, <code>234</code>, <code>235</code>,
<code>245</code>, and <code>345</code>
</p>

In combinatorics, we use the notation, `(5 choose 3) = 10`.\
\
In general, `(n choose r) = n! / r!(n - r)!`, where `r <= n`,
`n! = n × (n - 1) × ... × 3 × 2 × 1`, and `0! = 1`.\
\
It is not until `n = 23` that a value exceeds one-million: `(23 choose 10) = 1144066`.\
\
How many, not necessarily distinct, values of `(n choose r)` for `1 <= n <= 100`, are
greater than one-million?

### 54 - Poker hands
In the card game poker, a hand consists of five cards and are ranked, from lowest
to highest, in the following way:
- **High Card**: Highest value card.
- **One Pair**: Two cards of the same value.
- **Two Pairs**: Two different pairs.
- **Three of a Kind**: Three cards of the same value.
- **Straight**: All cards are consecutive values.
- **Flush**: All cards of the same suit.
- **Full House**: Three of a kind and a pair.
- **Four of a Kind**: Four cards of the same value.
- **Straight Flush**: All cards are consecutive values of same suit.
- **Royal Flush**: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:\
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.\
\
If two players have the same ranked hands then the rank made up of the highest value
wins; for example, a pair of eights beats a pair of fives (see example 1 below). But
if two ranks tie, for example, both players have a pair of queens, then highest cards
in each hand are compared (see example 4 below); if the highest cards tie then
the next highest cards are compared, and so on.\
\
Consider the following five hands dealt to two players:

<table style="text-align:center">
<tr><td><b>Hand</b></td><td><b>Player 1</b></td>
<td><b>Player 2</b></td><td><b>Winner</b></td></tr>

<tr><td><b>1</b></td><td>5H 5C 6S 7S KD<br>Pair of Fives</td>
<td>2C 3S 8S 8D TD<br>Pair of Eights</td><td>Player 2</td></tr>

<tr><td><b>2</b></td><td>5D 8C 9S JS AC<br>Highest card Ace</td>
<td>2C 5C 7D 8S QH<br>Highest card Queen</td><td>Player 1</td></tr>

<tr><td><b>3</b></td><td>2D 9C AS AH AC<br>Three Aces</td>
<td>3D 6D 7D TD QD<br>Flush  with Diamonds</td><td>Player 2</td></tr>

<tr><td><b>4</b></td><td>4D 6S 9H QH QC<br>Pair of Queens<br>Highest card Nine</td>
<td>3D 6D 7H QD QS<br>Pair of Queens<br>Highest card Seven</td><td>Player 1</td></tr>

<tr><td><b>5</b></td><td>2H 2D 4C 4D 4S<br>Full House<br>With Three Fours</td>
<td>3C 3D 3S 9S 9D<br>Full House<br>with Three Threes</td><td>Player 1</td></tr>
</table>

The file, [poker.txt](../../res/p054_poker.txt), contains one-thousand random hands
dealt to two players. Each line of the file contains ten cards (separated by a single
space): the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear winner.\
\
How many hands does Player 1 win?

### 55 - Lychrel numbers
If we take `47`, reverse and add, `47 + 74 = 121`, which is palindromic.\
\
Not all numbers produce palindromes so quickly. For example,

<p align="center">
<code>349 + 943 = 1292</code>
<code>1292 + 2921 = 4213</code>
<code>4213 + 3124 = 7337</code>
</p>

That is, `349` took three iterations to arrive at a palindrome.\
\
Although no one has proved it yet, it is thought that some numbers,
like `196`, never produce a palindrome. A number that never forms
a palindrome through the reverse and add process is called a Lychrel
number. Due to the theoretical nature of these numbers, and for the
purpose of this problem, we shall assume that a number is Lychrel until
proven otherwise. In addition you are given that for every number below
ten-thousand, it will either
- (i) become a palindrome in less than fifty iterations, or,
- (ii) no one, with all the computing power that exists, has managed so far to map
it to a palindrome. In fact, `10677` is the first number to be shown to require over
fifty iterations before producing a palindrome: `4668731596684224866951378664` (53
iterations, 28-digits).\
\
Surprisingly, there are palindromic numbers that are themselves Lychrel numbers;
the first example is `4994`.\
\
How many Lychrel numbers are there below ten-thousand?

### 56 - Powerful digit sum
<p>
A googol (<code>10<sup>100</sup></code>) is a massive number: one
followed by one-hundred zeros; <code>100<sup>100</sup></code> is almost
unimaginably large: one followed by two-hundred zeros. Despite their
size, the sum of the digits in each number is only <code>1</code>.
</p>

<p>
Considering natural numbers of the form, <code>a<sup>b</sup></code>,
where <code>a, b < 100</code>, what is the maximum digital sum?
</p>

### 57 - Square root convergents
It is possible to show that the square root of two can be expressed as an infinite
continued fraction.

<p align="center">
<img src="../../res/img/p057_sqrt2.png" alt="Continued fraction" height="52"/>
</p>

By expanding this for the first four iterations, we get:

<p>
<img src="../../res/img/p057_expansion01.png" alt="First expansion" height="36"/><br>
<img src="../../res/img/p057_expansion02.png" alt="Second expansion" height="44"/><br>
<img src="../../res/img/p057_expansion03.png" alt="Third expansion" height="52" /><br>
<img src="../../res/img/p057_expansion04.png" alt="Fourth expansion" height="60"/>
</p>

<p>
The next three expansions are
<img src="../../res/img/p057_expansion05.png" alt="Fifth expansion" height="25"/>,
<img src="../../res/img/p057_expansion06.png" alt="Sixth expansion" height="25"/> and
<img src="../../res/img/p057_expansion07.png" alt="Seventh expansion" height="25"/>,
but the eighth expansion,
<img src="../../res/img/p057_expansion08.png" alt="Eight expansion" height="25"/>,
is the first example where the number of digits in the numerator exceeds the number
of digits in the denominator.
</p>

In the first one-thousand expansions, how many fractions contain a numerator with
more digits than the denominator?
