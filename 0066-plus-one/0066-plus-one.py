class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number = int("".join(str(d) for d in digits))
        number += 1
        return [int(d) for d in str(number)]