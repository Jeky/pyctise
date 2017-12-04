#
# Polymorphism (https://en.wikipedia.org/wiki/Polymorphism_(computer_science)) is one of the most important design method when creating new APIs.
# Lots of people think that there is no way to overload methods by type in Python. This example shows the correct way to overload methods in Python 3 (>=3.4)
#
from functools import singledispatch
from typing import List, Union


class Event(object):
    
    def __init__(self, start: str, end: str, name: str):
        self.start = start
        self.end = end
        self.name = name

    def __str__(self):
        return 'Doing {} from {} to {}'.format(self.name, self.start, self.end)


class Schedule(object):

    def __init__(self):
        self.events = []
        # overload add()
        self.add = singledispatch(self.add)
        # register Event type to add()
        # when the type of parameter passed in is Event, use __add_event()
        self.add.register(Event, self.__add_event)
        # register list type to add()
        # when the type of parameter passed in is list, use __add_events()
        self.add.register(list, self.__add_events)

    def add(self, event: Union[Event, List[Event]]):
        raise NotImplementedError('Unsupported type')

    def __add_event(self, event: Event):
        self.events.append(event)

    def __add_events(self, events: List[Event]):
        self.events += events

    def __str__(self):
        return '\n'.join([str(e) for e in self.events])


if __name__ == '__main__':
    events = [Event('2017-12-02', '2017-12-03', 'coding'),\
              Event('2017-12-03', '2017-12-04', 'playing')]
    special_event = Event('2018-01-01', '2018-12-31', 'coding all year long')

    schedule = Schedule()
    schedule.add(special_event)
    schedule.add(events)

    print(schedule)
