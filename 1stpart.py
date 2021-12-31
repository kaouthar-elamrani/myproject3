class Vecteur2D:
    # constructeur par defaut
    def __init__(self, x=0, y=0):
        self.x = x  # initialisation de x et y, attributs d'instance
        self.y = y
   # cette methode represente la classe des objects string ici il va permettre de d'afficher les valeurs de self.x self.y
    def __str__(self):
        return "( %d, %d)" % (self.x, self.y)

# Le programme main
if __name__ == '__main__':
    print(" Instance sans parametre : ")
    print(Vecteur2D())
    print(" Instance avec les parametres : ")
    print(Vecteur2D(5, 2))

# Surcharge des opérateurs


class Vecteur2D(object):
    def __init__(self, x=0, y=0):
        # Constructeur avec paramètres par défaut.
        self.x = x
        self.y = y

    # Methode d'addition.
    def __add__(self, obj):
        return Vecteur2D(self.x+obj.x, self.y+obj.y)

    # Affichage d'un Vecteur2D.
    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

# Main program
vec1  = Vecteur2D(3, 5)
vec2 = Vecteur2D(7, 4)
print(vec1)
print(vec2)
print(vec1 + vec2)

# Rectangle class
class Rectangle():
    # Constructeur
    def __init__(self, length=8, width=6):
        self.length = length
        self.width = width
        self.nom = "rectangle"
    # Calculer la surface du rectangle.
    def surface(self):
        return self.length*self.width
    # Affichage des instances.

    def __str__(self):
        return "\nLe %s a une longueur de  %s et largeur de %s alors une surface de %s" % (self.nom, self.length, self.width, self.surface())

# classe héritante de Rectangle.


class pow(Rectangle):
    # Constructeur par defaut
    def __init__(self, side=10):
        Rectangle.__init__(self, side, side)
        self.nom = "carré"  # surchage d'attribut d'instance


# Main program
if __name__ == '__main__':
    rec = Rectangle(12, 8)
    print(rec)
    p = pow()
    print(p)

# classe des points du plan.


class Point():
    # Constructeur par défaut
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)
# classe héritante de la classe point.
class Segment():
    # Le constructeur utilise deux objets de classe  Point.
    def __init__(self, x1, y1, x2, y2):
        self.orig = Point(x1, y1)
        self.extrem = Point(x2, y2)
    def __str__(self):
        return "Segment [(%d, %d), (%d, %d)]" % (self.orig.x, self.orig.y, self.extrem.x, self.extrem.y)


# Main program
if __name__ == '__main__':
    p = Segment(1, 2, 3, 4)
    print(p)

