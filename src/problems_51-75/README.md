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