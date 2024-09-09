from typing import Any, Callable


def log(filename: str = "") -> Callable:
    """Функция декоратор которая логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def wrapper(func: Callable) -> Callable:
        def inner(*args: Any, **kwargs: Any) -> Any:
            print(f"Старт функции {func.__name__}")
            try:
                result = func(*args, **kwargs)
                log_result = f"{func.__name__} завершена успешно"
            except Exception as e:
                log_result = f"{func.__name__} error: тип ошибки. {e}"
                result = None
            finally:
                if not filename:
                    print(log_result)
                else:
                    with open(filename, "a") as file:
                        file.write(log_result + "\n")
            return result

        return inner

    return wrapper
