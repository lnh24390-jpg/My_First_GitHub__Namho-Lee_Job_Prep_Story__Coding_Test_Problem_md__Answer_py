from typing import List

MOD = 1_000_000_007


def solution(amount: int, coins: List[int]) -> int:
    """
    amount를 coins 조합으로 만드는 경우의 수를 반환한다.
    각 동전은 무한히 사용할 수 있다.
    """
    ways = [0] * (amount + 1)
    ways[0] = 1

    for coin in sorted(coins):
        for target in range(coin, amount + 1):
            ways[target] = (ways[target] + ways[target - coin]) % MOD

    return ways[amount]
