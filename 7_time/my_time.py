from datetime import datetime, timedelta

TIME_FORMAT = '%H:%M:%S'


class MyTime:

    def __init__(self, time):
        self.__time = datetime.strptime(time, TIME_FORMAT)

    def get_time(self):
        return self.__time

    def get_hours(self):
        return self.__time.hour

    def get_minutes(self):
        return self.__time.minute

    def get_seconds(self):
        return self.__time.second

    def advance(self, **kwargs):
        self.__time = self.__time + timedelta(**kwargs)

    def is_less_than(self, time):
        return self.__time < time.get_time()

    def to_string(self):
        return self.__time.strftime(TIME_FORMAT)


