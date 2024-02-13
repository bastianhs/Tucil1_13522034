# Algorithm Strategy Small Project 1

## Cyberpunk 2077 Breach Protocol Puzzle Solver

Solving Cyberpunk 2077 Breach Protocol puzzle using brute force algorithm

## Requirements

- Python 3.12

## How to run

```
git clone https://github.com/bastianhs/Tucil1_13522034.git
```

```
cd Tucil1_13522034
```

```
python src/main.py
```

## Input from and output to .txt file

Text files (.txt) should be placed in the folder:

```
Tucil1_13522034/test
```

## Input from .txt file format

```
buffer_size
matrix_width matrix_height
matrix
number_of_sequences
sequences_1
sequences_1_reward
sequences_2
sequences_2_reward
…
sequences_n
sequences_n_reward
```

example:

```
7
6 6
7A 55 E9 E9 1C 55
55 7A 1C 7A E9 55
55 1C 1C 55 E9 BD
BD 1C 7A 1C 55 BD
BD 55 BD 7A 1C 1C
1C 55 55 7A 55 7A
3
BD E9 1C
15
BD 7A BD
20
BD 1C BD 55
30
```

## Randomized input from terminal format

```
number_of_unique_tokens
tokens
buffer_size
matrix_width matrix_height
number_of_sequences
max_size_of_sequences
```

example:

```
5
BD 1C 7A 55 E9
7
6 6
3
4
```

## Output to terminal and .txt file format

```
max_reward
buffer_solution
token1_coordinate
token2_coordinate
token3_coordinate
...
tokenN_coordinate

execution_time
```

example:

```
50
7A BD 7A BD 1C BD 55
1, 1
1, 4
3, 4
3, 5
6, 5
6, 4
5, 4

300 ms
```

## Creator

Bastian H. Suryapratama

13522034

K-02
