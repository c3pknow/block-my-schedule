class Schedule():
    hours_week = 168      # 168 hours in a week
    hours_day = 24

    def __init__(self):
        self.items = []

    def add(self, element):
        self.items.append(element)

    def count(self):
        return len(self.items)

    def get_free_time(self):
        return self.hours_week - self.get_scheduled_time()

    def get_scheduled_time(self):
        time = 0
        for item in self.items:
            time += item.get_length()
            # if item.__class__.__name__ == 'Block':
            #     time += item.get_length()
            # elif item.__class__.__name__ == 'RecurringBlock':
            #     time = item.get_blocks()

            #     for block in blocks:
            #         time += item.get_length()

        return time
