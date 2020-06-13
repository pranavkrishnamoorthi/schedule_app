

import datetime as dt


class Event:
    """An event takes an indicated estimated time,
    """


    def __init__(self, name, time):
        """

        :param name: The name of the event in String
        :param time:
        """
        self.name = name
        self.time = time
        self.start, self.end = self.time_fit()
        self.type



    def time_fit(self, regulator):
        optimal_start_time = dt.datetime.now()
        optimal_end_time = dt.datetime.time()
        return optimal_start_time, optimal_end_time

    def find_best_time(self, regulator):



class Emergency(Event):


    def __init__(self):
        self.

