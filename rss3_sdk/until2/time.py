import tzlocal
from datetime import (
    datetime
)

def get_datetime_isostring() -> str:
    dt = datetime.now(tzlocal.get_localzone())
    try:
        utc = dt - dt.utcoffset()
    except TypeError as e:
        raise ("Get current UTC Time False, current time %r " % dt)
    isostring = datetime.strftime(utc, '%Y-%m-%dT%H:%M:%S.{0}Z')
    return isostring.format(int(round(utc.microsecond/1000.0)))