from Block import Block


class RecurringBlock(Block):
    def __init__(self, name, type_, start_day, start_time, end_day, end_time, recurrence):
        Block.__init__(self, name, type_,
                       start_day, start_time, end_day, end_time)
        # self.name = name
        # self.type = type_
        # self.start_day = start_day
        # self.start_time = start_time
        # self.end_day = end_day
        # self.end_time = end_time
        self.recurrence = recurrence

    def get_length(self):
        length = 0

        for block in self.get_blocks():
            length += block.get_length()
            # print('Blocks length ' + str(length))
        return length
        # for occurrence in self.recurrence:

        #     if self.start_day == self.end_day:
        #         return self.end_time - self.start_time
        #     elif Block.days[self.start_day] < Block.days[self.end_day]:
        #         return ((Block.days[self.end_day] - Block.days[self.start_day] + 1) * 24) - self.start_time - (24 - self.end_time)
        #     else:
        #         return (6 - (Block.days[self.end_day]+1) + Block.days[self.start_day] + 1) - self.start_time - (24 - self.end_time)

    def get_blocks(self):
        blocks = []
        if Block.days[self.start_day] <= Block.days[self.end_day]:
            # print('Offset: ', self.get_day_offset())
            for occurrence in self.recurrence:
                end_day_num = (Block.days[occurrence] +
                               self.get_day_offset()) % 7

                for key, value in Block.days.items():    # for name, age in dictionary.iteritems():  (for Python 2.x)
                    if value == end_day_num:
                        end_day = key

                # print(end_day_num, occurrence, end_day)
                blocks.append(Block(self.name, self.type, occurrence,
                                    self.start_time, end_day, self.end_time))

            # print('Blocks returned from RecurringBlock.get_blocks: ' +
            #     str(len(blocks)))
            return blocks
