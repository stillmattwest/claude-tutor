from greetings.core import greet


def test_greet_uses_the_name():
    assert greet("Devon") == "Hello, Devon!"
