from pytest import *
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('John')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'John'
        assert self.a1.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(-1.5) == False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(0) == False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(1.5) == True
        assert self.a1.get_balance() == 1.5

a