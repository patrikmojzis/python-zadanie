import datetime as dt

def round_seconds(obj = dt.datetime.now()) -> dt.datetime:
    if obj.microsecond >= 500_000:
        obj += dt.timedelta(seconds=1)
    return obj.replace(microsecond=0)