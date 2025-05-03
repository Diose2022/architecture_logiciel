from abc import ABC, abstractmethod

# Interface stratégie
class StrategiePaiement(ABC):
    @abstractmethod
    def payer(self, montant):
        pass

# Stratégies concrètes
class PaiementCarte(StrategiePaiement):
    def payer(self, montant):
        print(f"Paiement de {montant}€ par carte bancaire.")

class PaiementPaypal(StrategiePaiement):
    def payer(self, montant):
        print(f"Paiement de {montant}€ via PayPal.")

class PaiementEspeces(StrategiePaiement):
    def payer(self, montant):
        print(f"Paiement de {montant}€ en espèces.")

# Contexte
class Panier:
    def __init__(self, strategie: StrategiePaiement):
        self.strategie = strategie

    def changer_strategie(self, strategie: StrategiePaiement):
        self.strategie = strategie

    def effectuer_paiement(self, montant):
        self.strategie.payer(montant)

# Utilisation
panier = Panier(PaiementCarte())
panier.effectuer_paiement(50)

panier.changer_strategie(PaiementPaypal())
panier.effectuer_paiement(75)
