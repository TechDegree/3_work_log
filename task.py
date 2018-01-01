import re


class Task:
    """Task Class used in the Worklog
    """

    name = None
    date = None
    notes = None
    time = None

    def __init__(self, name, time, notes, date):
        """[summary]
        
        Arguments:
            name {[type]} -- [description]
            time {[type]} -- [description]
            notes {[type]} -- [description]
            date {[type]} -- [description]
        """
        self.name = name
        self.date = date
        self.notes = notes
        self.time = time

    def __repr__(self):
        representation = """-------------------
Name       - {}
Time (min) - {}
Notes      - {}
Date       - {}
-------------------\n""".format(self.name, 
                                self.time, 
                                self.notes, 
                                self.date)
        return representation

    def keep_string(self):
        cvs_row = "{}, {}, {}, {}".format(self.name,
                                          self.time,
                                          self.notes,
                                          self.date) 
        return cvs_row

n = Task(1,2,3,4)
print(n)
