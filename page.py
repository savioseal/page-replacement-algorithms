class PageTask:
    """PageTask class"""

    def __init__(self, id_num, value):
        self.id = id_num
        self.value = value
        self.use_time = 0

    def __repr__(self):
        string = "P" + str(self.value)
        return string

    def __str__(self):
        string = "P" + str(self.value)
        return string

    def sort_value(self):
        return self.value

    def sort_use_time(self):
        return self.use_time
