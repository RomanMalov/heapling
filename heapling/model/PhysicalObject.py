import model.GameObject as GameObject


class PhysicalObject(GameObject):
    """
    This is a base class for each object that is
    placed on screen and somehow "physical", so it can touch other objects
    """

    def collidePoint(self, point)->bool:
        """
        Check if point is inside of object
        :param point: Vector'ish thing, (x,y)
        :return:
        """
        pass

    def collide(self, other)->bool:
        """
        Check if other physical object is inside this one
        :param other: Other PhysicalObject
        :return:
        """
        pass