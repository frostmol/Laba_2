import pytest
from Laba_2 import calculator

class TestCalculator:

    # Параметризованный тест для различных операций и ожидаемых результатов
    @pytest.mark.parametrize("a, b, operation, expected_result", [
        (3, 6, '+', 9),
        (11, 9, '-', 2),
        (5, 7, '*', 35),
        (6, 2, '/', 3),
    ])
    def test_calculator_positive(self, a, b, operation, expected_result):
        actual_result = calculator(a, b, operation)
        assert actual_result == expected_result

    # Тест для неподдерживаемой операции
    def test_calculator_invalid_operation(self):
        with pytest.raises(ValueError):
            calculator(3, 6, '%')

    # Тест для деления на ноль
    def test_calculator_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            calculator(8, 0, '/')
