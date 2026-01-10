class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Soln 1 - Using In built Functions
        # return max(sum(customer) for customer in accounts)

        # Soln 2 - looping through the array
        max_wealth = 0 # intialzie amount
        for customer_acc in accounts:
            curr_wealth = 0 # currently no amount
            for val in customer_acc:
                curr_wealth += val
            max_wealth = max(max_wealth, curr_wealth)
        return max_wealth

        