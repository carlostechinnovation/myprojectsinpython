"""
Tests unitarios usando PYTEST sobre la clase definida en el fichero ../testUnitarios.py
    Se cumple lo indicado aqui: https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html#tests-as-part-of-application-code

    Y se prueba con: cd C:\DATOS\GITHUB_REPOS\myprojectsinpython\misChuletas\; pytest
"""


class BankAccount:
    def __init__(self, id):
        self.id = id
        self.balance = 0

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def deposit(self, amount):
        self.balance += amount
        return True

# ------------ PYTEST (mejor que UNITTEST)----------


def test_insufficient_deposit():
    # Arrange
    a = BankAccount(1)
    a.deposit(100)
    # Act
    outcome = a.withdraw(200)
    # Assert
    assert outcome == False
