from .event import Event, EventCategory

class EventHandler():
    def __init__(self):
        self.registered_events=[]
        self.registered_categories=[]
        self.registered_event_handlers=[]
        self.registered_category_handlers=[]

    def onEvent(self, event):
        # OnEvent will assume the event is registered.
        # If the event is not registered, then it will
        # cause issues and crash and burn.
        for handler in self.registered_event_handlers[event.getType()]: # For everything that wants this Specific Event!
            if event.isCancelled(): #If the event has been cancelled, just stop
                break
            handler(event)
        if not event.isCancelled(): #Continue to send to valid category handlers, if not cancelled
            for category in self.registered_categories:
                if event.isCancelled(): #Just stop already if canceled.
                    break
                elif event.inCategory(category): #If event is part of this category
                    for handler in self.registered_category_handler[category.ID]: #For everything that wants this category of events
                        if event.isCancelled(): #Stop it, Stop it, Stop it!
                            break
                        handler(event)

    def register_event(self, event):
        assert issubclass(event, Event), "Event to be registered must be child of Event."
        event.register(len(self.registered_events), self.onEvent)
        self.registered_events.append(event)
        self.registered_event_handlers.append([])

    def register_category(self, category):
        assert issubclass(category, EventCategory), "Category to be registered must be child of EventCategory."
        category.registered(len(self.registered_categories))
        self.registered_categories.append(category)
        self.registered_category_handlers.append([])

    def register_handler(self, event, callback):
        #   This ties callback functions to specific event, so that
        #   when an event fires, the call back is called with the event
        if event in self.registered_events: # Is event registered as an event?
            self.registered_event_handlers[event.getType()].append(callback)
        elif event in self.registered_categories: #Is the event really a category?
            self.registered_category_handlers[event.ID].append(callback)
        else: #Event is not registered, Can't register for non-existent event
            raise Exception("Received Non Registered Event! %s"%event)
