class Utilisateur:

    nom = ""
    email = ""
    mot_de_passe = ""
    genre = ""
    age = 0

    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0):
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.genre = genre
        self.age = age

    def display(self):
        print(self.nom, "  ", self.email, "  ", self.mot_de_passe, "  ", self.genre, "  ", self.age)


class Module:

    nom = 0
    volume_horaire = 0
    semestre = ""
    ListMatiere = []
    def __init__(self, nom="", volume_horaire=0, semestre=""):
        self.nom = nom
        self.volume_horaire = volume_horaire
        self.semestre = semestre

    def display(self):
        print(self.nom, "\t", self.volume_horaire, "\t", self.semestre)


class Professeur(Utilisateur):

    ppr = 0
    grade = ""
    module = Module()
    ListeMatieres = []
    ListeAnnesAcademique = []

    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0, ppr=0, grade=""):
        super().__init__(self, nom, email, mot_de_passe, genre, age)
        self.ppr = ppr
        self.grade = grade

    def display(self):
        print(self.ppr, "\t", self.grade)


class Matiere:

    nom = 0
    pourcentage = 0
    module = Module()
    ListeAnnesAcademique = []
    def __init__(self, nom="", pourcentage=0):
        self.nom = nom
        self.pourcentage = pourcentage

    def display(self):
        print(self.nom, "\t", self.pourcentage)


class Annee_Academique:

    anne = ""
    Listetudiant = []
    Listematiesre = []
    Listeprofesseur = []

    def __init__(self, anne=""):
        self.anne = anne

    def display(self):
        print(self.anne)


class Etudiant(Utilisateur):

    code_massar = ""
    ListAnneAcademique = []

    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0, code_massar=""):
        super().__init__(nom, email, mot_de_passe, genre, age)
        self.code_massar = code_massar

    def display(self):
        print(self.code_massar)


class Evaluation:

    note = 0
    matiere = Matiere()
    annee_acadimique = Annee_Academique()
    etudiant = Etudiant()

    def __init__(self, note=0):
        self.note = note

    def display(self):
        print(self.note)

