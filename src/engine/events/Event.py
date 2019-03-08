class Event():
    id=None
    category=None
    callback=None
    def __init__(self, category):
        self.handled=False
    def getName(self):
        return self.__class__.__name__
    def getType(self):
        return self.id
    def __str__(self):
        return self.getName()
    def inCategory(self, category):
        return self.category & category
    def isCancelled(self):
        return self.handled == True
    @classmethod
    def setCategory(cls, category):
        if cls.category is None:
            if isinstance(category, list):
                cls.category=set(category)
        else:
            raise Exception("Event Category(s) for Event %s have already been set!"%cls.__name__)
    @classmethod
    def register(cls, id, callback):
        if cls.id is None:
            cls.id=id
            cls.callback=callback
        else:
            raise Exception("Event %s has already been registered! Attempted Registration Failed."%cls.__name__)

class EventCategory():
    def __init__(self, categoryName):
        self.id=None
        self.name=categoryName
    def register(self, id):
        if self.id is None:
            self.id=id
        else:
            raise Exception("EventCategory %s has already been registered! Attempted Registration Failed."%self.name)
    @property
    def ID(self):
        return self.id
