class MinStack:

    def __init__(self):
        self.stack = []
        self._min = []

    def push(self, val: int) -> None:
        if not self.stack:
            self._min.append(val)
        else:
            self._min.append(min(val, self._min[-1]))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self._min.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self._min[-1]
