Problem 20 in *How to Solve It*:

> In how many ways can you change one dollar? (The "way of changing" is determined if it is known how many coins of each kind -- cents, nickles, dimes, quarters, half dollars -- are used.)

The program is:

```python
COINS = [1, 5, 10, 25, 50]
LEN_COINS = len(COINS)
remain = 100
combination = [0] * LEN_COINS
combinations = set()

def change(offset):
    global remain, combination, combinations
    if remain == 0:
        combinations.add(",".join([str(i) for i in combination]))
        return
    for i in range(offset, LEN_COINS):
        coin = COINS[i]
        if remain >= coin:
            remain -= coin
            combination[i] += 1
            change(i)
            combination[i] -= 1
            remain += coin

change(0)
print(len(combinations))
```

The result is 292.