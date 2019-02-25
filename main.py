from Block import Block
from Schedule import Schedule
from RecurringBlock import RecurringBlock

schedule = Schedule()


def printStatus():
    print('Item Count: ' + str(schedule.count()))
    print('Free Time:' + str(schedule.get_free_time()))
    print('Scheduled Time: ' + str(schedule.get_scheduled_time()))
    print('\n')


printStatus()

sleep = RecurringBlock('Sleep', 'sleep', 'M', 23, 'T', 7, [
                       'M', 'T', 'W', 'Th', 'F', 'S', 'Su'])
schedule.add(sleep)


yoga = RecurringBlock('Yoga', 'mind_body', 'M', 19,
                      'M', 22, ['M', 'T', 'W', 'S'])
schedule.add(yoga)
printStatus()



work = RecurringBlock('Work', 'work', 'M', 9,
                      'M', 17, ['M', 'T', 'W', 'Th', 'F'])
schedule.add(work)
printStatus()


read = RecurringBlock('Read', 'learn', 'M', 21,
                      'M', 23, ['M', 'T', 'W'])
schedule.add(read)
printStatus()


learn = RecurringBlock('Code and stuff', 'learn', 'S', 19,
                      'S', 22, ['Th', 'S', 'Su'])
schedule.add(learn)
printStatus()



# line = '#################################################################################################################'
# grid = '{}  #\t{}\t#\t{}\t#\t{}\t#\t{}\t#\t{}\t#\t{}\t#\t{}\t#'
# header = grid.format('  ', 'M', 'T', 'W', 'T', 'F', 'S', 'S')

# print(line)
# print(header)

# for i in range(0, 24):
#     print(grid.format('{num:02d}'.format(num=i), '', '', '', '', '', '', ''))

#     if i == 11:
#         print(header)
