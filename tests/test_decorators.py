from src.decorators import log



def test_log():
    @log()
    def sum_num(a, b, c):
        return a + b + c

    result = sum_num(10, 15, 20)
    assert result == 45


@log()
def sum_num(a, b, c):
    return a + b + c

def test_log_capsus(capsys):
    sum_num(10, 15, 20)
    captured = capsys.readouterr()
    assert captured.out == 'Старт функции sum_num\nsum_num завершена успешно\n'


def test_log_capsus(capsys):
    sum_num(10, 15, "10")
    captured = capsys.readouterr()
    assert captured.out == """Старт функции sum_num
sum_num error: тип ошибки. unsupported operand type(s) for +: 'int' and 'str'\n"""


