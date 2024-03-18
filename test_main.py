from main import process_numbers


def test_process_numbers():
    assert process_numbers((-10, -1, 0, 1, 2)) == 5
