class GameObject():
    """
    This object is base for each other that is drawn on the screen
    Like the heapling itself, walls around, even buttons.

    Why is there a need for that? They each have to have a render method
    In it they call for view rendering methods
    """
    def __init__(self, view):
        """
        Every game object must have some kind of view that will draw it
        :param view:
        """
        self._view = view

    def render(self)->None:
        """
        Does what it says - renders the game object.
        Where? Where the corresponding view will tell
        :return:
        """
        # base implementation if render isn't affected by state of object
        self._view.render(self)


    def step(self, dt : float)->None:
        """
        Method to update the game object with time, move it, etc
        :param dt: Time period
        :return:
        """
        pass
