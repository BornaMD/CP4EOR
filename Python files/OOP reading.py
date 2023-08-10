if __name__ == "__main__":
    class Robot:
      def __init__(self, 
                 name=None,
                 build_year=None):
        self.name = name   
        self.build_year = build_year

      def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
        if self.build_year:
            print("I was built in " + str(self.build_year))
        else:
            print("It's not known, when I was created!")

      def set_name(self, name):
        self.name = name

      def get_name(self):
        return self.name    

      def set_build_year(self, by):
        self.build_year = by

      def get_build_year(self):
        return self.build_year    


    x = Robot("Henry", 2008)
    y = Robot()
    y.set_name("Marvin")
    x.say_hi()
    y.say_hi()

    if __name__ == "__main__":
      x = Robot()
      y = Robot()
      y2 = y
      print(y == y2)
      print(y == x)

    x = Robot()
    y = Robot()

    x.name = "Marvin"
    x.build_year = "1979"

    y.name = "Caliban"
    y.build_year = "1993"

    print(x.name)
    print(y.build_year)

    print(x.__dict__, "\n",
    y.__dict__,"\n",
    Robot.__dict__,"\n",
    getattr(x, 'energy', 100))

    def f(x):
      f.counter = getattr(f, "counter", 0) + 1 
      return "Monty Python"

    for i in range(10):
      f(i)

    print(f.counter)

    def hi(obj):
      print("Hi, I am " + obj.name)

    x = Robot()
    x.name = "Marvin"
    Robot.say_hi(x)


    class robot_2:
    
        def __init__(self, name=None, build_year=2000):
            self.__name = name
            self.__build_year = build_year

        def say_hi(self):
            if self.__name:
                print("Hi, I am " + self.__name)
            else:
                print("Hi, I am a robot without a name")

        def set_name(self, name):
            self.__name = name

        def get_name(self):
            return self.__name    

        def set_build_year(self, by):
            self.__build_year = by

        def get_build_year(self):
            return self.__build_year    

        def __repr__(self):
            return "robot_2('" + self.__name + "', " +  str(self.__build_year) +  ")"

        def __str__(self):
            return "Name: " + self.__name + ", Build Year: " +  str(self.__build_year)


    if __name__ == "__main__":
        x = robot_2("Marvin", 1979)
        y = robot_2("Caliban", 1943)
        for rob in [x, y]:
            rob.say_hi()
            if rob.get_name() == "Caliban":
                rob.set_build_year(1993)
            print("I was built in the year " + str(rob.get_build_year()) + "!")

main()
