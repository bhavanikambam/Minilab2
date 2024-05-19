from Counters import Time

class Clock:
    """
    Our implementation of the Clock class
    """

    def getTime(self):
        return Time.getTime()
    
    def setTime(self, timetuple):
        Time.setTime(timetuple)

    def getHour(self):
        """
        Return the current hour as an int.
        """
        timetuple = Time.getTime()
        return timetuple[3]

    def setHour(self, hour):
        """
        Set the RTC hour to the provided hour.
        """
        timetuple = list(Time.getTime())  # Convert the tuple into a list
        timetuple[3] = hour               # Update the hour
        Time.setTime(tuple(timetuple))    # Save it back to the system

    def getMinute(self):
        """
        Return the current minute as an int.
        """
        timetuple = Time.getTime()
        return timetuple[4]
    
    def setMinute(self, minute):
        """
        Set the RTC minute to the provided minute.
        """
        timetuple = list(Time.getTime())  # Convert the tuple into a list
        timetuple[4] = minute             # Update the minute
        Time.setTime(tuple(timetuple))    # Save it back to the system

    def getDate(self):
        """
        Return the current date as an int.
        """
        timetuple = Time.getTime()
        return timetuple[2]
    
    def setDate(self, date):
        """
        Set the RTC date to the provided date.
        """
        timetuple = list(Time.getTime())  # Convert the tuple into a list
        timetuple[2] = date               # Update the date
        Time.setTime(tuple(timetuple))    # Save it back to the system
    
    def getMonth(self):
        """
        Return the current month as an int.
        """
        timetuple = Time.getTime()
        return timetuple[1]

    def setMonth(self, month):
        """
        Set the RTC month to the provided month.
        """
        timetuple = list(Time.getTime())  # Convert the tuple into a list
        timetuple[1] = month              # Update the month
        Time.setTime(tuple(timetuple))    # Save it back to the system

    def getDay(self):
        """
        Return the current day of the week as an int (0=Monday, 6=Sunday).
        """
        timetuple = Time.getTime()
        return timetuple[6]

    def setDay(self, day):
        """
        Set the RTC day of the week to the provided day (0=Monday, 6=Sunday).
        """
        timetuple = list(Time.getTime())  # Convert the tuple into a list
        timetuple[6] = day                # Update the day of the week
        Time.setTime(tuple(timetuple))    # Save it back to the system

    def getDaysInMonth(self, month, year):
        """
        Return the number of days in the given month of the given year.
        """
        if month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            # Check for leap year
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return 29
            else:
                return 28
        else:
            return 31
