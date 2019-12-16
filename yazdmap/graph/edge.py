class edge():

    def __init__(self , first , last, weigth = 0):
        self.first = first
        self.last = last
        self.weigth = weigth
        self.key1 = '{first} - {last}'.format(first = self.first , last = self.last)
        self.key2 = '{last} - {first}'.format(first = self.first , last = self.last)

    def doesInclude(self, vertex):
        if(self.first is vertex or self.last is vertex):
            return True
        return False
