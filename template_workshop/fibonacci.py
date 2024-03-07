from typing import Any


class Fibonacci:
    def __init__(self):
        self.mem = {}

    def __call__(self, n: int) -> Any:
        return self.fib(n)

    def fib(self, n: int) -> int:
        if n < 0:
            return None
        if n in self.mem:
            return self.mem[n]
        if n <= 1:
            return n
        self.mem[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.mem[n]
