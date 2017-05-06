class ss:

    def __init__(self):
        self.area = 4
        self.imperv = 5
        self.perv = 3


s = ss()

a = 'area'

vars(s)[a] = 10

print(vars(s))