# Produit complexe
class Ordinateur:
    def __init__(self):
        self.composants = []

    def ajouter(self, composant):
        self.composants.append(composant)

    def afficher(self):
        print("Ordinateur avec :", ", ".join(self.composants))

# Builder
class BuilderOrdinateur:
    def __init__(self):
        self.ordinateur = Ordinateur()

    def ajouter_cpu(self):
        self.ordinateur.ajouter("CPU Intel i7")

    def ajouter_ram(self):
        self.ordinateur.ajouter("16GB RAM")

    def ajouter_stockage(self):
        self.ordinateur.ajouter("SSD 512GB")

    def get_resultat(self):
        return self.ordinateur

# Directeur
class Directeur:
    def __init__(self, builder):
        self.builder = builder

    def construire_pc_gamer(self):
        self.builder.ajouter_cpu()
        self.builder.ajouter_ram()
        self.builder.ajouter_stockage()

# Utilisation
builder = BuilderOrdinateur()
directeur = Directeur(builder)
directeur.construire_pc_gamer()
pc = builder.get_resultat()
pc.afficher()

