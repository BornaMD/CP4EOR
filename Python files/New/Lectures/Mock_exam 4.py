class triangle:
    def __init__(self, v1, v2, v3):
        self.i = v1
        self.j = v2
        self.k = v3

    @property
    def isEquilateral(self):
        if self.i == self.j == self.k:
            return True
        else:
            return False


    def gettype(self):
        if self.j == self.i and self.k == self.j and self.i == self.i:
            return 3
        elif self.i == self.j or self.i == self.k or self.k == self.j:
            return 2
        else:
            return 0



# GetAllTypes() should be defined outside the class, this only has filename as a variable, this uses the class triangle.
