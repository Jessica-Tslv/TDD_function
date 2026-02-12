
from lib.includes_todo import includes_todo

"""
Test is a line does not contain `#TODO`
Expected output should be False
"""
def test_returns_false_without_todo():
    line_example = includes_todo("Buy groceries")
    assert line_example == False

"""
Test if a line starts with `#TODO`
Expected output should be True
"""
def test_returns_true_with_todo_at_the_start():
    line_example = includes_todo("#TODO Buy groceries")
    assert line_example == True


"""
Test if a line ends with `#TODO`
Expected output should be True
"""
def test_returns_true_with_todo_at_the_end():
    line_example = includes_todo("Buy groceries #TODO")
    assert line_example == True


"""
Test with a line containing #TODO with punctuation - e.g. #TODO:
Expected output should be True
"""
def test_returns_true_with_punctuation():
    line_example = includes_todo("#TODO: Buy groceries")
    assert line_example == True

"""
Test with lower case #todo
Expected output should be True
"""
def test_returns_true_with_lowercase_todo():
    line_example = includes_todo("#todo: Buy groceries")
    assert line_example == True

"""
Test without the hash symbol - e.g. TODO
Expected output should be False
"""

def test_returns_false_without_hash_symbol():
    line_example = includes_todo("TODO Buy groceries")
    assert line_example == False