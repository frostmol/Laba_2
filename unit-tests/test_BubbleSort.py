import pytest
from Laba_2 import bubble_sort

class TestBubbleSort:

    # Параметризованный тест для различных входных данных
    @pytest.mark.parametrize("input_data, expected_result", [
        ([], []),
        ([7], [7]),
        ([4, 3, 32, 1, 6, 12], [1, 3, 4, 6, 12, 32]),
        ([2, 1, 2, 1], [1, 1, 2, 2]), #повторяющиеся числа
        ([10, 9, 8, 7], [7, 8, 9, 10]), # числа в обратном порядке
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) # проверить, что сортировка не изменяет уже отсортированный список
    ])
    

    def test_bubble_sort(self, input_data, expected_result):
        actual_result = bubble_sort(input_data)
        assert actual_result == expected_result


    # Тест для попытки сортировки списка, содержащего некорректные значения
    @pytest.mark.parametrize("input_data", [(4, None, 3, 7, 15), (6, "4", 2, 8, 19)])
    def test_bubble_sort_with_invalid_input(self, input_data):
        with pytest.raises(TypeError):
            bubble_sort(list(input_data))



