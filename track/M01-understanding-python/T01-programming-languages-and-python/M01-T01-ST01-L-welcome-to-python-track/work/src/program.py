class demo:
    def __init__(self):
        self.name = "suhasini"
        self.age = 22
        self.favcolour = "Blue"
    def selflove(self):
        print("i am always in selflove mood")
        print("self")
d = demo()
print(d.name)
print(d.age)
print(d.favcolour)
d.selflove()
print(d)
#modifying
d.age = 23
print(d.age)
#adding
d.movie = "sye"
print(d.movie)
#deleting
del d.favcolour
print(d.favcolour)