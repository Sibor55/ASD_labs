import time


class TimerError(Exception):
    """Для ошибок"""


class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Запустить таймер"""
        if self._start_time is not None:
            raise TimerError(f"Таймер работает, нужно использовать .stop()")

        self._start_time = time.perf_counter()

    def stop(self):
        """Остановить таймер и показать время"""
        if self._start_time is None:
            raise TimerError(f"Таймер не работает, нужно запустить его .start()")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Время: {elapsed_time:0.10f} сек.")
