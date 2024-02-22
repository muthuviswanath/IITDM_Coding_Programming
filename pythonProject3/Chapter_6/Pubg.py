from random import randint


class Weapon:

    def use_weapon(self):
        pass
class Knife(Weapon):

    def use_weapon(self):
        print ("Slit the throat or stab")


class Gun(Weapon):

    def use_weapon(self):
        print("Aim and Shoot")


class Grenade(Weapon):

    def use_weapon(self):
        print("Throw on Enemy")


class Pan(Weapon):

    def use_weapon(self):
        print("Defend yourself")

class Pubg:

    def generate_weapon(self,n):

        if n == 1:
            kn = Knife()
            kn.use_weapon()

        elif n==2:
            gun = Gun()
            gun.use_weapon()

        elif n == 3:
            grenade= Grenade()
            grenade.use_weapon()

        else:
            pan = Pan()
            pan.use_weapon()


P= Pubg()
n = randint(1,4)
P.generate_weapon(n)


# create an object of PUBG class
# create a random number between1 and 4
# call the generate_weapon method by passing the random number


