class Cow:
    def gives(self):
        m = Milk()
        print(m)
        return m

class Milk:
    pass

c = Cow()
mlk = c.gives()
print(type(mlk))