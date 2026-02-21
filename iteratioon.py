class test:
    def __init__(self,limit):
        self.limit = limit
    def __iter__(self):
        self.x=1
        return self
    def __next__(self):
        x=self.x
        if x > self.limit:
            raise StopIteration
        self.x=self.x+1
        return x
for i in test(15):
    print(i)