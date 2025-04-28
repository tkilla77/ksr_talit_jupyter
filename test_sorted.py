from sorting import *

def test_sorted():
    assert is_sorted(['Apfel', 'Birne', 'Zwetschge'])
    assert not is_sorted(['Birne', 'Apfel', 'Zwetschge'])


def test_sorted_bug():
    assert not is_sorted(['Apfel', 'Zwetschge', 'Birne'])
