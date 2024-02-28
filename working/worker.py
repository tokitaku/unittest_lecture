from datetime import datetime, timedelta

SCHEDULED_WORKINGTIME = timedelta(hours=8)  # 所定労働時間


class Worker:
    """ 労働者 """

    def __init__(
            self,
            name: str,
            starting_time: datetime,
            finishing_time: datetime,
            break_time: timedelta,
            is_weekday: bool
    ):
        """
        :param name: 名前
        :param starting_time: 出勤時間
        :param finishing_time: 退勤時間
        :param break_time: 休憩時間
        :param is_weekday: 勤務日区分
        """

        self.name = name
        self.starting_time = starting_time
        self.finishing_time = finishing_time
        self.break_time = break_time
        self.is_weekday = is_weekday
        self.total_worktime = self._calc_total_worktime()  # 総労働時間
        self.scheduled_worktime = self._calc_scheduled_worktime()  # 平日所定内労働時間
        self.over_worktime = self._calc_overtime()  # 平日所定外時間
        self.holiday_worktime = self.total_worktime if not is_weekday else timedelta(0)  # 休日労働時間

    def _calc_total_worktime(self) -> timedelta:
        """総労働時間を計算する"""
        return self.finishing_time - self.starting_time - self.break_time

    def _calc_scheduled_worktime(self) -> timedelta:
        """平日所定内労働時間を計算する"""
        if self.is_weekday:
            overflow_time = self.total_worktime - SCHEDULED_WORKINGTIME
            if overflow_time > timedelta(0):
                return SCHEDULED_WORKINGTIME
            else:
                return self.total_worktime
        return timedelta(0)

    def _calc_overtime(self):
        """平日所定外時間を計算する"""
        if self.is_weekday:
            scheduled_over = self.total_worktime - SCHEDULED_WORKINGTIME
            if scheduled_over > timedelta(0):
                return scheduled_over
            else:
                return timedelta(0)
        return timedelta(0)
