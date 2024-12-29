class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_gas = sum(gas)
        sum_cost = sum(cost)

        if sum_gas < sum_cost:
            return -1
        
        tank = 0
        start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:  
                start = i + 1
                tank = 0
        
        return start