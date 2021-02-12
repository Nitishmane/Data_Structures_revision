class dynamic_array(object):

    def __init__(self):
        self.n = 0 #Count of element
        self.capacity = 1 #Default Capacity
        self.A = self.make_array(self.capacity)


    def __len__(self):
        return self.n