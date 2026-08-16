class BalanceTool:

    def get_balance(self, account_id: str):

        # Mock banking data for learning
        accounts = {"1001": 50000, "1002": 75000, "2001": 12000}

        return accounts.get(account_id)
