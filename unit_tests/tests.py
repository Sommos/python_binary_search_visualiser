import main

def test_binary_search():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert main.binary_search(arr, 1) == 0
    assert main.binary_search(arr, 5) == 4
    assert main.binary_search(arr, 10) == 9
    assert main.binary_search(arr, 11) == -1
    assert main.binary_search(arr, 0) == -1

    arr = [1, 3, 5, 7, 9]
    assert main.binary_search(arr, 1) == 0
    assert main.binary_search(arr, 5) == 2
    assert main.binary_search(arr, 9) == 4
    assert main.binary_search(arr, 11) == -1
    assert main.binary_search(arr, 0) == -1

    arr = [2, 4, 6, 8, 10]
    assert main.binary_search(arr, 2) == 0
    assert main.binary_search(arr, 6) == 2
    assert main.binary_search(arr, 10) == 4
    assert main.binary_search(arr, 11) == -1
    assert main.binary_search(arr, 0) == -1