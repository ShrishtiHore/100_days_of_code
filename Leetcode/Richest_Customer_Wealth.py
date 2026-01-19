class Solution:
    def maximumWealth(self, accounts):
        maximum_wealth = 0

        for i in range(len(accounts)):
            total_wealth = sum(accounts[i])
            
            if total_wealth > maximum_wealth:
                maximum_wealth = total_wealth

        return maximum_wealth
