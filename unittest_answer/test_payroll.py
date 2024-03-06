from datetime import datetime, timedelta
from unittest import TestCase

from working.payroll import Payroll
from working.worker import Worker


class TestPayrollWeekdayWorker(TestCase):
    """平日労働者 (所定労働8時間、所定外労働2時間、休日労働0時間)"""

    def setUp(self):
        self.taro = Worker(
            name="Taro",
            starting_time=datetime(2022, 1, 1, 9, 0),
            finishing_time=datetime(2022, 1, 1, 20, 0),
            break_time=timedelta(hours=1),
            is_weekday=True
        )
        self.payroll = Payroll(worker=self.taro, hourly_pay=1000)

        hourly_pay = 1000
        self.scheduled_salary = 8 * hourly_pay
        self.overtime_salary = 2 * hourly_pay * 1.25
        self.holiday_salary = 0

    def test_scheduled_salary(self):
        """所定労働時間の給与が正しいか"""
        self.assertEqual(self.payroll.scheduled_salary, self.scheduled_salary)

    def test_overtime_salary(self):
        """所定外労働時間の給与が正しいか"""
        self.assertEqual(self.payroll.overtime_salary, self.overtime_salary)

    def test_holiday_salary(self):
        """休日労働時間の給与が正しいか"""
        self.assertEqual(self.payroll.holiday_salary, self.holiday_salary)

    def test_total_salary(self):
        """合計給与が正しいか"""
        self.assertEqual(self.payroll.total_salary, self.scheduled_salary + self.overtime_salary + self.holiday_salary)


class TestPayrollHolidayWorker(TestCase):
    """休日労働者 (所定労働0時間、所定外労働0時間、休日労働7時間)"""

    def setUp(self):
        self.jiro = Worker(
            name="Jiro",
            starting_time=datetime(2022, 1, 1, 9, 0),
            finishing_time=datetime(2022, 1, 1, 17, 0),
            break_time=timedelta(hours=1),
            is_weekday=False
        )
        self.payroll = Payroll(worker=self.jiro, hourly_pay=1000)

        hourly_pay = 1000
        self.scheduled_salary = 0
        self.overtime_salary = 0
        self.holiday_salary = 7 * hourly_pay * 1.35

    def test_scheduled_salary(self):
        """所定労働時間の給与が正しいか"""
        self.assertEqual(self.payroll.scheduled_salary, self.scheduled_salary)

    def test_overtime_salary(self):
        """所定外労働時間の給与が正しいか"""
        self.assertEqual(self.payroll.overtime_salary, self.overtime_salary)

    def test_holiday_salary(self):
        """休日労働時間の給与が正しいか"""
        self.assertEqual(self.payroll.holiday_salary, self.holiday_salary)

    def test_total_salary(self):
        """合計給与が正しいか"""
        self.assertEqual(self.payroll.total_salary, self.scheduled_salary + self.overtime_salary + self.holiday_salary)
