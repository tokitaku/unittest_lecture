from datetime import datetime, timedelta
from unittest import TestCase

from working.payroll import Payroll
from working.worker import Worker

OVERTIME_RATE = 1.25
HOLIDAY_RATE = 1.35


class TestPayrollWeekdayScheduledWorker(TestCase):
    """平日労働者 (所定労働8時間、所定外労働0時間、休日労働0時間)"""

    def setUp(self):
        hourly_pay = 1000

        taro = Worker(
            name="Taro",
            starting_time=datetime(2022, 1, 1, 9, 0),
            finishing_time=datetime(2022, 1, 1, 18, 0),
            break_time=timedelta(hours=1),
            is_weekday=True
        )
        self.payroll = Payroll(worker=taro, hourly_pay=hourly_pay)

        self.scheduled_salary = taro.scheduled_worktime * hourly_pay
        self.overtime_salary = taro.over_worktime * hourly_pay * OVERTIME_RATE
        self.holiday_salary = taro.holiday_worktime * hourly_pay * HOLIDAY_RATE

    def test_scheduled_salary(self):
        """所定内労働時間の給与が正しいか"""
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


class TestPayrollWeekdayOverTimeWorker(TestCase):
    """平日労働者 (所定労働8時間、所定外労働2時間、休日労働0時間)"""

    def setUp(self):
        hourly_pay = 1000

        jiro = Worker(
            name="Jiro",
            starting_time=datetime(2022, 1, 1, 9, 0),
            finishing_time=datetime(2022, 1, 1, 20, 0),
            break_time=timedelta(hours=1),
            is_weekday=True
        )
        self.payroll = Payroll(worker=jiro, hourly_pay=hourly_pay)

        self.scheduled_salary = jiro.scheduled_worktime * hourly_pay
        self.overtime_salary = jiro.over_worktime * hourly_pay * OVERTIME_RATE
        self.holiday_salary = jiro.holiday_worktime * hourly_pay * HOLIDAY_RATE

    def test_scheduled_salary(self):
        """所定内労働時間の給与が正しいか"""
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
        hourly_pay = 1000

        saburo = Worker(
            name="Saburo",
            starting_time=datetime(2022, 1, 1, 9, 0),
            finishing_time=datetime(2022, 1, 1, 17, 0),
            break_time=timedelta(hours=1),
            is_weekday=False
        )
        self.payroll = Payroll(worker=saburo, hourly_pay=hourly_pay)

        self.scheduled_salary = saburo.scheduled_worktime * hourly_pay
        self.overtime_salary = saburo.over_worktime * hourly_pay * OVERTIME_RATE
        self.holiday_salary = saburo.holiday_worktime * hourly_pay * HOLIDAY_RATE

    def test_scheduled_salary(self):
        """所定内労働時間の給与が正しいか"""
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
