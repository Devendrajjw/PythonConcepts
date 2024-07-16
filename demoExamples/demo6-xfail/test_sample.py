import pytest
from sample import BankAccount

@pytest.fixture
def account():
    return BankAccount("Alice", 100)

def test_initial_balance(account):
    assert account.get_balance() == 100

def test_deposit(account):
    account.deposit(50)
    assert account.get_balance() == 150

def test_withdraw(account):
    account.withdraw(30)
    assert account.get_balance() == 70


def test_overdraft(account):
    account.overdraft(200)
    assert account.get_balance() == -100
