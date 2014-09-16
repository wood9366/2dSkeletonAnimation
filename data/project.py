from data import skeleton

class Project(object):
    """Project data"""

    ProjectId = 0

    def __init__(self):
        self.ProjectId += 1
        self.__name = "Project " + str(self.ProjectId)
        self.__skeleton = skeleton.Skeleton()

    @property
    def skeleton(self):
        return self.__skeleton

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
