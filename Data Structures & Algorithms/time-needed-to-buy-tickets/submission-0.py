class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0

        for i in range(len(tickets)):
            if tickets[i] < tickets[k]:
                time += tickets[i]
            else:
                time += tickets[k]
        
        return time

         

        
            