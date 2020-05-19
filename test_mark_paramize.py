import pytest
import sys

#传参，一个是字符串“”
@pytest.mark.parametrize("test_input, expected", [("3+5",8), ("2+5",7), ("9+21",30)])
def test_eval(test_input, expected):
    # eval关键字将字符串str当成有效的表达式来求值，并返回结果
    assert eval(test_input) == expected