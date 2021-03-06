from datetime import time

from pandas.tseries.holiday import AbstractHolidayCalendar, GoodFriday, USLaborDay, USPresidentsDay, USThanksgivingDay
from pytz import timezone

from .holidays_us import (Christmas, USBlackFridayInOrAfter1993, USIndependenceDay, USMartinLutherKingJrAfter1998,
                          USMemorialDay, USNewYearsDay)
from .market_calendar import MarketCalendar


class CFEExchangeCalendar(MarketCalendar):
    """
    Exchange calendar for the CBOE Futures Exchange (CFE).

    http://cfe.cboe.com/aboutcfe/expirationcalendar.aspx

    Open Time: 8:30am, America/Chicago
    Close Time: 3:15pm, America/Chicago

    (We are ignoring extended trading hours for now)
    """
    aliases = ['CFE']

    @property
    def name(self):
        return "CFE"

    @property
    def tz(self):
        return timezone("America/Chicago")

    @property
    def open_time_default(self):
        return time(8, 31, tzinfo=self.tz)

    @property
    def close_time_default(self):
        return time(15, 15, tzinfo=self.tz)

    @property
    def regular_holidays(self):
        return AbstractHolidayCalendar(rules=[
            USNewYearsDay,
            USMartinLutherKingJrAfter1998,
            USPresidentsDay,
            GoodFriday,
            USIndependenceDay,
            USMemorialDay,
            USLaborDay,
            USThanksgivingDay,
            Christmas
        ])

    @property
    def special_closes(self):
        return [(
            time(12, 15),
            AbstractHolidayCalendar(rules=[
                USBlackFridayInOrAfter1993,
            ])
        )]
