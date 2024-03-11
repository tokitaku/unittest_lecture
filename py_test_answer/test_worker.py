from datetime import datetime, timedelta

import pytest

from working.worker import Worker


@pytest.fixture
def setup():
    yield Worker(
        name='Taro',
        starting_time=datetime(2024, 1, 1, 8, 30),
        finishing_time=datetime(2024, 1, 1, 16, 30),
        break_time=timedelta(hours=1),
        is_weekday=True
    )


def test_total_worktime(setup):
    """総労働時間計算のテスト"""
    assert setup.total_worktime == 7.0


def test_scheduled_worktime(setup):
    """所定内労働時間計算のテスト"""
    assert setup.scheduled_worktime == 7.0


def test_overtime(setup):
    """所定外労働時間計算のテスト"""
    assert setup.over_worktime == 0.0


def test_holiday_worktime(setup):
    """休日労働時間計算のテスト"""
    assert setup.holiday_worktime == 0.0


class TestWeekdayOvertimeWorker:
    """平日、所定労働時間外で働く労働者"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.worker = Worker(
            name='Jiro',
            starting_time=datetime(2024, 1, 1, 8, 30),
            finishing_time=datetime(2024, 1, 1, 18, 30),
            break_time=timedelta(hours=1),
            is_weekday=True
        )

    def test_total_worktime(self):
        """総労働時間計算のテスト"""
        assert self.worker.total_worktime == 9.0

    def test_scheduled_worktime(self):
        """所定内労働時間計算のテスト"""
        assert self.worker.scheduled_worktime == 8.0

    def test_overtime(self):
        """所定外労働時間計算のテスト"""
        assert self.worker.over_worktime == 1.0

    def test_holiday_worktime(self):
        """休日労働時間計算のテスト"""
        assert self.worker.holiday_worktime == 0.0


class TestHolidayWorker:
    """休日に働く労働者"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.worker = Worker(
            name='Saburo',
            starting_time=datetime(2024, 1, 1, 8, 30),
            finishing_time=datetime(2024, 1, 1, 16, 30),
            break_time=timedelta(hours=1),
            is_weekday=False
        )

    def test_total_worktime(self):
        """総労働時間計算のテスト"""
        assert self.worker.total_worktime == 7.0

    def test_scheduled_worktime(self):
        """所定内労働時間計算のテスト"""
        assert self.worker.scheduled_worktime == 0.0

    def test_overtime(self):
        """所定外労働時間計算のテスト"""
        assert self.worker.over_worktime == 0.0

    def test_holiday_worktime(self):
        """休日労働時間計算のテスト"""
        assert self.worker.holiday_worktime == 7.0
