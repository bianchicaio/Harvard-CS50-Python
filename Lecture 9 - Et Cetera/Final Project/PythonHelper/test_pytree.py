from pytree3 import PythonHelper

pyhelper = PythonHelper()

def test_get_sub():
    assert pyhelper.get_subject() == 'Data Science'