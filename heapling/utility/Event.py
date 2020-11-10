class Event():
    """
    This type of objects has a simple purpose - they bundle together calling for a similar functions

    Example : you need to do a lot of actions on a click.
    You need to connect handlers to click once and then just throw this event
    Simple as that
    """

    def __init__(self):
        self.handlers = []

    def throw(self, *params):
        for handler in self.handlers:
            handler(*params)

    def addHandler(self, func):
        if callable(func):
            self.handlers.append(func)