class Account:
    def __init__(self, name: str) -> None:
        '''
        Function to set up account object.
        :param name: account name
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Deposits the amount given into the account balance.
        :param amount: amount to deposit.
        :return: Boolean value to say if the amount was successful or not
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Withdraws the amount given from the account balance.
        :param amount: Amount to withdraw.
        :return: Boolean value to say if the withdraw was successful or not.
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Returns the balance of the account.
        :return: Float representinf the account balance.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Returns the name of account.
        :return: String representing the account name.
        """
        return self.__account_name