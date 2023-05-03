"""Ejemplos de tests unitarios con UNITTEST y PYTEST
Para probar unittest: cd C:\DATOS\GITHUB_REPOS\myprojectsinpython\misChuletas; python -m unittest -v testUnitarios.py
"""
import unittest


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


# ------------ UNITTEST ----------
class TestBankOperations(unittest.TestCase):
    def test_insufficient_deposit(self):
        # Arrange
        a = BankAccount(1)
        a.deposit(100)
        outcome = a.withdraw(200)  # Act
        self.assertFalse(outcome)  # Assert

        # Otras comprobaciones:
        # self.assertEqual(x, y)  # Comprueba x == y
        # Comprueba si ha saltado una excepción específica
        # self.assertRaises(exception_type)
        # self.assertIsNone(x)  # Comprueba si x es None
        # self.assertIn(x, y)  # Comprueba si x está en y


# ------------ PYTEST (mejor que UNITTEST)----------
def test_insufficient_deposit():
    # Arrange
    a = BankAccount(1)
    a.deposit(100)
    # Act
    outcome = a.withdraw(200)
    # Assert
    assert outcome == False


# Si el código python se ejecuta desde un script con comando, se entra por aquí y se pueden capturar los parámetros fácilmente
if __name__ == '__main__':
    print("===== INICIO =====")

    print("===== FIN =====")
