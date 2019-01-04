# Various utilities related to date handling
# TODO: Change the file name to 'date'

from datetime import date as Date
from datetime import datetime as DateTime
from datetime import timedelta as TimeDelta
import re

today = Date.today

FORMAT = re.compile(r'^\d{4}\-\d{1,2}\-\d{1,2}$')
JUST_DAY = re.compile(r'^(\d{1,2})$')
DAY_MONTH = re.compile(r'(\d{1,2})\-(\d{1,2})$')


def absolute_date(info):
    if isinstance(info, Date):
        return info
    elif isinstance(info, tuple):
        return Date(*info)
    elif isinstance(info, str) and FORMAT.match(info):
        return DateTime.strptime(info, '%Y-%m-%d').date()
    else:
        raise RuntimeError("Invalid date %s" % info)


def relative_date(time_info):
    if isinstance(time_info, str):
        t = today()
        if time_info == 'tomorrow':
            return t + TimeDelta(1)
        elif time_info == 'today':
            return t
        days_match = re.match(r'^(\d+)\s+days?$', time_info)
        if days_match:
            days = int(days_match.group(1))
            return t + TimeDelta(days)
        d_match = re.match(r'^(\d+)d$', time_info)
        if d_match:
            days = int(d_match.group(1))
            return t + TimeDelta(days)
        just_day_match = JUST_DAY.match(time_info)
        if just_day_match:
            day = int(just_day_match.group(1))
            if t.day < day:
                return Date(t.year, t.month, day)
            else:
                return Date(t.year + (t.month // 12), (t.month % 12) + 1, day)
        month_day_match = DAY_MONTH.match(time_info)
        if month_day_match:
            month = int(month_day_match.group(1))
            day = int(month_day_match.group(2))
            if t < Date(t.year, month, day):
                return Date(t.year, month, day)
            else:
                return Date(t.year + 1, month, day)

    return absolute_date(time_info)
