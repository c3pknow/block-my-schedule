class Block:
    days = {
        'M': 0,
        'T': 1,
        'W': 2,
        'Th': 3,
        'F': 4,
        'S': 5,
        'Su': 6}

    types = {
        'sleep',
        'work',
        'mind_body',
        'outdoors',
        'learn',
        'personal',
        'career',
        'fun',
        'free'
    }

    def __init__(self, name, type_, start_day, start_time, end_day, end_time):
        self.name = name
        self.type = type_
        self.start_day = start_day
        self.start_time = start_time
        self.end_day = end_day
        self.end_time = end_time

    def get_length(self):

        if self.start_day == self.end_day:
            return self.end_time - self.start_time
        elif Block.days[self.start_day] < Block.days[self.end_day]:
            return ((Block.days[self.end_day] - Block.days[self.start_day] + 1) * 24) - self.start_time - (24 - self.end_time)
        else:
            #print('((' + str(Block.days[self.end_day]) + ' - ' + str(Block.days[self.start_day]) + ' + 1) * 24) - ' + str(self.start_time) + ' - (24 - ' + str(self.end_time) + ')')
            return ((((Block.days[self.end_day] - Block.days[self.start_day] + 1) % 7)) * 24) - self.start_time - (24 - self.end_time)
            # return (6 - (Block.days[self.end_day]+1) + Block.days[self.start_day] + 1) - self.start_time - (24 - self.end_time)

    def get_day_offset(self):
        return (Block.days[self.end_day] - Block.days[self.start_day])

    def get_number_days(self):
        offset = super.get_offset()

        if offset > 0:
            return super.get_offset() + 1
        elif offset < 0:
            return abs(super.get_offset())
        else:
            return 0


#   M  T  W  Th  F  S  Su
#   0  1  2  3   4  5  6

# Start: 5
# End: 1
# offset: -4
