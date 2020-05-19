import pytest

def test_four():
    print("shiyixia")


class TestDemo:
    def test_one(self):
        print("开始执行test_one方法")
        x = "this"
        assert 'i' in x

    def test_two(self):
        print("开始执行test_two方法")
        e = "hi"
        #必须要把字符串包起来，不然就是变量了
        assert 'h' in e

    def test_three(self):
        print("开始执行test_three方法")
        s = "secret"
        assert 'c' in s


if __name__ == '__main__':
    # pytest.main("-v -x TestDemo")
    # pytest.mian()
    #通过字典得方式传参执行
    pytest.mian(['-v', '-x', 'TestDemo'])

