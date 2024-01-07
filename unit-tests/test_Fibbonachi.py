import pytest
from Laba_2 import fibbonachi

class TestFibbonachi:

    # Параметризованный тест для различных значений n и ожидаемых результатов
    @pytest.mark.parametrize("n, expected_result", [
        (0, []),
        (1, [0]),
        (2, [0, 1]),
        (5, [0, 1, 1, 2, 3]),
        (15, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]),
        (20, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181])
    ])
    def test_fibbonachi(self, n, expected_result):
        actual_result = fibbonachi(n)
        assert actual_result == expected_result

    # Тест для случая n = -1 (отрицательное значение)
    def test_fibbonachi_negative_n(self):
        with pytest.raises(ValueError):
            fibbonachi(-1)


