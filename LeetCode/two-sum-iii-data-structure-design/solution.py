class TwoSum:
    def __init__(self):
        self.numbers = []

    # O(log n)
    def add(self, number: int) -> None:
        self.numbers.append(number)
        self.numbers.sort()

    # O(n)
    def find(self, value: int) -> bool:
        left = 0
        right = len(self.numbers) - 1

        while left < right:
            two_sum = self.numbers[left] + self.numbers[right]

            if two_sum == value:
                return True
            elif two_sum < value:
                left += 1
            else:
                right -= 1

        return False