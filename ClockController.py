from Displays import LCDDisplay
from Button import *
from Clock import *

class ClockController:
    """ Our implementation of the Clock Controller
        4 buttons for setting month, date, hour, min, and day
        LCD display to show the time
    """

    def __init__(self): 
        self._clock = Clock()
        self._display = LCDDisplay(sda=0, scl=1, i2cid=0)
        self._buttons = [
            Button(10, 'white', buttonhandler=self),
            Button(11, 'red', buttonhandler=self),
            Button(12, 'yellow', buttonhandler=self),
            Button(13, 'blue', buttonhandler=self)
        ]

    def showTime(self):
        # Show the time on the display
        year, month, date, hour, minute, sec, wd, yd = self._clock.getTime()
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
       # show the days on display
        day_str = days_of_week[wd]
        self._display.showText(f'{hour:02d}:{minute:02d}:{sec:02d}\n{month:02d} {date:02d} {day_str}')

        """
        If you want to make it so that the time shows as 00:00:00 instead of 0:0:0
        for single digit ints (i.e., 01:03:07 instead of 1:3:7) use :02d to add leading zeros.
        Example: {hour} retrieves 1 at 1am. {hour:02d} retrieves 01 at 1am.

        You can also change what shows on the display. Right now the display shows:
        hour:minute:sec
        month date day
        """

    def buttonPressed(self, name):                 
        if name == 'white':
        # white button display the month 
            month = self._clock.getMonth()
            if month == 12:
                self._clock.setMonth(1)
            else:
                self._clock.setMonth(month + 1)

        elif name == 'red':
            year = self._clock.getTime()[0]
            month, date = self._clock.getMonth(), self._clock.getDate()
            if date == self._clock.getDaysInMonth(month, year):
                self._clock.setDate(1)
                if month == 12:
                    self._clock.setMonth(1)
                else:
                    self._clock.setMonth(month + 1)
            else:
                self._clock.setDate(date + 1)
            
            day = self._clock.getDay()
            if day == 6:
                self._clock.setDay(0)  # Reset to Monday
            else:
                self._clock.setDay(day + 1)

        elif name == 'yellow':
            # yellow button shows the hour on display
            hour = self._clock.getHour()
            if hour == 23:
                self._clock.setHour(0)
                date = self._clock.getDate()
                month = self._clock.getMonth()
                year = self._clock.getTime()[0]
                if date == self._clock.getDaysInMonth(month, year):
                    self._clock.setDate(1)
                    if month == 12:
                        self._clock.setMonth(1)
                    else:
                        self._clock.setMonth(month + 1)
                else:
                    self._clock.setDate(date + 1)

                day = self._clock.getDay()
                if day == 6:
                    self._clock.setDay(0)  # Reset to Monday
                else:
                    self._clock.setDay(day + 1)
            else:
                self._clock.setHour(hour + 1)

        elif name == 'blue':
            # blue button shows the minute on display
            minute = self._clock.getMinute()
            if minute == 59:
                self._clock.setMinute(0)
                hour = self._clock.getHour()
                if hour == 23:
                    self._clock.setHour(0)
                    date = self._clock.getDate()
                    month = self._clock.getMonth()
                    year = self._clock.getTime()[0]
                    if date == self._clock.getDaysInMonth(month, year):
                        self._clock.setDate(1)
                        if month == 12:
                            self._clock.setMonth(1)
                        else:
                            self._clock.setMonth(month + 1)
                    else:
                        self._clock.setDate(date + 1)

                    day = self._clock.getDay()
                    if day == 6:
                        self._clock.setDay(0)  # Reset to Monday
                    else:
                        self._clock.setDay(day + 1)
                else:
                    self._clock.setHour(hour + 1)
            else:
                self._clock.setMinute(minute + 1)

    def buttonReleased(self, name):
        pass
