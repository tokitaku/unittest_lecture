from .worker import Worker


class Payroll:
    """給与計算"""

    OVERTIME_RATE = 1.25  # 所定外労働の割増率
    HOLIDAY_RATE = 1.35  # 休日労働の割増率

    def __init__(self, worker: Worker, hourly_pay: int):
        """
        :param worker: 労働者
        :param hourly_pay: 時給
        """
        self._worker = worker
        self._hourly_pay = hourly_pay

    @property
    def scheduled_salary(self) -> int:
        """平日所定内労働の給与"""
        return int(self._worker.scheduled_worktime * self._hourly_pay)

    @property
    def overtime_salary(self) -> int:
        """平日所定外労働の給与"""
        return int(self._worker.over_worktime * self._hourly_pay * self.OVERTIME_RATE)

    @property
    def holiday_salary(self) -> int:
        """休日労働の給与"""
        return int(self._worker.holiday_worktime * self._hourly_pay * self.HOLIDAY_RATE)

    @property
    def total_salary(self) -> int:
        """給与合計"""
        return self.scheduled_salary + self.overtime_salary + self.holiday_salary
