class Etudiant :
    def __init__(self, Nom, Prenom, Age, Cne, Moyenne):
        self.Nom = Nom
        self.Prenom = Prenom
        self.Age = Age
        self.Cne = Cne
        self.Moyenne = Moyenne
 #list de type etudiant
Etudiant = [
{"Nom" : "EL AMRANI","Prenom" : "KAOUTHAR", "Age": 22,"Cne": 131490793, "Moyenne": 17},
{'Nom' : 'KHOUAKHI','Prenom' : 'MOHAMED', 'Age': 32,'Cne': 134157892, 'Moyenne': 18},
{'Nom': 'AHMADI','prenom' : 'GHIZLANE', 'Age': 19,'Cne': 154129876, 'Moyenne': 16},
{'Nom' : 'FAROUKI','Prenom' : 'HIND', 'Age': 16,'Cne': 146545655, 'Moyenne': 13},
]

#Sort with age
#sort function of trie / lambda nous permettre de recuperer la valeur des keys des keys indiquee
Etudiant.sort(key=lambda K: K.get('Age'))
print(Etudiant)
#Sort with moyenne
Etudiant.sort(key=lambda K: K.get('Moyenne'))
print(Etudiant)