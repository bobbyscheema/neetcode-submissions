class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pairs = {}

        for i in range(1, len(numbers)):
            for j in range(2, len(numbers)):
                if i + j == target:
                    return [i, j]