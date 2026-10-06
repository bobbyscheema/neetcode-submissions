class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [] # result[i] = num of days after ith 

        for i in range(len(temperatures)):
            j = i + 1
            count = 1
            while j < len(temperatures):
                if temperatures[i] < temperatures[j]:
                    break
                j += 1
                count += 1
            count = 0 if j == len(temperatures) else count
            result.append(count)
        return result