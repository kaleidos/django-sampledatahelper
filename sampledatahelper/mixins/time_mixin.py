import datetime as dt
import random
from django.utils.timezone import utc

from ..exceptions import ParameterError


class TimeMixin(object):
    def date_between(self, min_date, max_date):
        """Random date between a min_date and a max_date."""
        if min_date > max_date:
            raise ParameterError('min_date greater than max_date')

        delta = max_date - min_date
        int_delta = delta.days
        random_day = self.int(0, int_delta)

        return min_date + dt.timedelta(days=random_day)

    def future_date(self, min_distance=0, max_distance=365):
        """Random date between today and today + one year - one day."""
        if min_distance < 0:
            raise ParameterError('min_distance less than 0')

        if min_distance > max_distance:
            raise ParameterError('min_distance greater than max_distance')

        return dt.date.today() + dt.timedelta(days=random.randrange(min_distance, max_distance))

    def past_date(self, min_distance=0, max_distance=365):
        """Random date between today and today + one year - one day."""
        if min_distance < 0:
            raise ParameterError('min_distance less than 0')

        if min_distance > max_distance:
            raise ParameterError('min_distance greater than max_distance')

        return dt.date.today() - dt.timedelta(days=random.randrange(min_distance, max_distance))

    def datetime_between(self, min_datetime, max_datetime):
        """Random datetime between a min datetime and a max datetime."""
        if min_datetime > max_datetime:
            raise ParameterError('min_datetime greater than max_datetime')

        delta = max_datetime - min_datetime
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = self.int(0, int_delta)

        return min_datetime + dt.timedelta(seconds=random_second)

    def future_datetime(self, min_distance=0, max_distance=1440):
        """Random date between today and today + one year - one day."""
        if min_distance < 0:
            raise ParameterError('min_distance less than 0')

        if min_distance > max_distance:
            raise ParameterError('min_distance greater than max_distance')

        now = dt.datetime.utcnow().replace(tzinfo=utc)
        delta = dt.timedelta(minutes=random.randrange(min_distance, max_distance))

        return now + delta

    def past_datetime(self, min_distance=0, max_distance=1440):
        """Random date between today and today + one year - one day."""
        if min_distance < 0:
            raise ParameterError('min_distance less than 0')

        if min_distance > max_distance:
            raise ParameterError('min_distance greater than max_distance')

        now = dt.datetime.utcnow().replace(tzinfo=utc)
        delta = dt.timedelta(minutes=random.randrange(min_distance, max_distance))

        return now - delta

    def date(self, begin=-365, end=365):
        """Random date between today - one year and today + one year."""
        if begin > end:
            raise ParameterError('begin greater than end')

        return dt.date.today() - dt.timedelta(random.randrange(begin, end))

    def datetime(self, begin=-1440, end=1440):
        """Random date between today - one year and today + one year."""
        if begin > end:
            raise ParameterError('begin greater than end')

        return dt.datetime.utcnow().replace(tzinfo=utc) - dt.timedelta(minutes=random.randrange(begin, end))

    def time(self):
        """Random time"""
        return dt.time(
            self.int(0, 23),
            self.int(0, 59),
            self.int(0, 59),
            self.int(0, 999999),
        )
