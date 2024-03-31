class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l, total_gas, cur_gas, start = len(gas), 0, 0, 0

        for i in range(l):
            total_gas += (gas[i] - cost[i])
            cur_gas += (gas[i] - cost[i])
            
            if cur_gas < 0:
                cur_gas = 0
                start = i+1
        
        return start if total_gas >= 0 else -1