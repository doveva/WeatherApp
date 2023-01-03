from datetime import datetime, timedelta, tzinfo


class SPbTz(tzinfo):

    UTCOffset = timedelta(hours=3)

    def utcoffset(self, dt):
        return self.UTCOffset

    def fromutc(self, dt):
        # Follow same validations as in datetime.tzinfo
        if not isinstance(dt, datetime):
            raise TypeError("fromutc() requires a datetime argument")
        if dt.tzinfo is not self:
            raise ValueError("dt.tzinfo is not self")
        return dt + self.UTCOffset

    def dst(self, dt):
        # Kabul does not observe daylight saving time.
        return timedelta(0)

    def tzname(self, dt):
        return "+03"


spb_timezone = SPbTz()
