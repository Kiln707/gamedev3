
from functools import partial
from collections import namedtuple

EVENT = namedtuple('EVENT', ['EVENT_NAME', 'ID', 'DATA'])
e = parital(EVENT, "Generic_Event")
registered = partial(e, 0)

EventHandler.call(registered(['x','y','z'])

class EventHandler():
    pass
