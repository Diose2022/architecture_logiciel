class Observateur:
    def actualiser(self, message):
        pass

class Utilisateur(Observateur):
    def __init__(self, nom):
        self.nom = nom

    def actualiser(self, message):
        print(f"{self.nom} a reçu une notification : {message}")

class SystemeNotification:
    def __init__(self):
        self.observateurs = []

    def ajouter_observateur(self, obs):
        self.observateurs.append(obs)

    def notifier_tous(self, message):
        for obs in self.observateurs:
            obs.actualiser(message)

# Utilisation
notif = SystemeNotification()
Mamadou = Utilisateur("Alice")
Ali = Utilisateur("Bob")
notif.ajouter_observateur(Mamadou)
notif.ajouter_observateur(Ali)

notif.notifier_tous("Nouvelle mise à jour disponible !")
