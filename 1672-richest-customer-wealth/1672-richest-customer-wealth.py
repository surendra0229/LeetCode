class Solution(object):
    def maximumWealth(self, accounts):
        maximun = 0
        for customer in accounts:
            wealth = sum(customer)
            maximun = max(maximun, wealth)
        return maximun