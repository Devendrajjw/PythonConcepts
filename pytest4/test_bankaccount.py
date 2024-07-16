import pytest
from bankaccount import BankAccount
import pytest


@pytest.fixture
def bankacc():
    return BankAccount("John Doe", 100)


def test_initial_balance(bankacc):
    assert bankacc.get_balance() == 100


def test_deposit(bankacc):
    bankacc.deposit(50)
    assert bankacc.get_balance() == 150


def test_withdraw(bankacc):
    bankacc.withdraw(30)
    assert bankacc.get_balance() == 70


def test_withdraw_insufficient_funds(bankacc):
    with pytest.raises(ValueError, match="Insufficient funds"):
        bankacc.withdraw(200)


def test_deposit_negative_amount(bankacc):
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        bankacc.deposit(-50)
