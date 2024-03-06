from datetime import datetime, timedelta
from unittest import TestCase

from working.worker import Worker


class TestWeekdayScheduledWorker(TestCase):
    """ 平日、所定労働時間内で働く労働者 """

    @classmethod
    def setUpClass(cls):
        cls.taro = Worker(
            name='Taro',
            starting_time=datetime(2024, 1, 1, 8, 30),
            finishing_time=datetime(2024, 1, 1, 16, 30),
            break_time=timedelta(hours=1),
            is_weekday=True
        )

    def test_total_worktime(self):
        """総労働時間計算のテスト"""
        self.assertEqual(self.taro.total_worktime, timedelta(hours=7))

    def test_scheduled_worktime(self):
        """所定内労働時間計算のテスト"""
        self.assertEqual(self.taro.scheduled_worktime, timedelta(hours=7))

    def test_overtime(self):
        """所定外労働時間計算のテスト"""
        self.assertEqual(self.taro.over_worktime, timedelta(0))

    def test_holiday_worktime(self):
        """休日労働時間計算のテスト"""
        self.assertEqual(self.taro.holiday_worktime, timedelta(0))


class TestWeekdayOvertimeWorker(TestCase):
    """平日、所定労働時間外で働く労働者"""

    @classmethod
    def setUpClass(cls):
        cls.jiro = Worker(
            name='Jiro',
            starting_time=datetime(2024, 1, 1, 8, 30),
            finishing_time=datetime(2024, 1, 1, 18, 30),
            break_time=timedelta(hours=1),
            is_weekday=True
        )

    def test_total_worktime(self):
        """総労働時間計算のテスト"""
        self.assertEqual(self.jiro.total_worktime, timedelta(hours=9))

    def test_scheduled_worktime(self):
        """所定内労働時間計算のテスト"""
        self.assertEqual(self.jiro.scheduled_worktime, timedelta(hours=8))

    def test_overtime(self):
        """所定外労働時間計算のテスト"""
        self.assertEqual(self.jiro.over_worktime, timedelta(hours=1))

    def test_holiday_worktime(self):
        """休日労働時間計算のテスト"""
        self.assertEqual(self.jiro.holiday_worktime, timedelta(0))


class HolidayWorker(TestCase):
    """休日に働く労働者"""

    @classmethod
    def setUpClass(cls):
        cls.saburo = Worker(
            name='Saburo',
            starting_time=datetime(2024, 1, 1, 8, 30),
            finishing_time=datetime(2024, 1, 1, 16, 30),
            break_time=timedelta(hours=1),
            is_weekday=False
        )

    def test_total_worktime(self):
        """総労働時間計算のテスト"""
        self.assertEqual(self.saburo.total_worktime, timedelta(hours=7))

    def test_scheduled_worktime(self):
        """所定内労働時間計算のテスト"""
        self.assertEqual(self.saburo.scheduled_worktime, timedelta(0))

    def test_overtime(self):
        """所定外労働時間計算のテスト"""
        self.assertEqual(self.saburo.over_worktime, timedelta(0))

    def test_holiday_worktime(self):
        """休日労働時間計算のテスト"""
        self.assertEqual(self.saburo.holiday_worktime, timedelta(hours=7))
