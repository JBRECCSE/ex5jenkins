from app import add, multiply
def test_add():
    assert add(30, 20) == 50
def test_multiply():
    assert multiply(10, 5) == 50
print("All tests passed successfully!")
