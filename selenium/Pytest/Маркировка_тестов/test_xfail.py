import pytest

# @pytest.mark.xfail используется для пометки тестов, которые вы ожидаете, что будут провалены (fail),
# но это не является критической ошибкой. Это может быть полезно в различных ситуациях, например:
# Тесты, которые ожидают исправления
# Тесты для временного кода
# Тесты для нестабильных или экспериментальных функций

# Если вы ожидаете, что тест в конечном итоге будет успешным, вы можете добавить аргумент strict=True для того,
# чтобы убедиться, что он считается проваленным, если он проходит успешно:
@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False