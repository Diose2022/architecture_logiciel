from abc import ABC, abstractmethod

# Produit
class Transport(ABC):
    @abstractmethod
    def livrer(self):
        pass

# Produits concrets
class Camion(Transport):
    def livrer(self):
        return "Livraison par camion"

class Bateau(Transport):
    def livrer(self):
        return "Livraison par bateau"

# Créateur
class TransportFactory(ABC):
    @abstractmethod
    def creer_transport(self):
        pass

# Créateurs concrets
class CamionFactory(TransportFactory):
    def creer_transport(self):
        return Camion()

class BateauFactory(TransportFactory):
    def creer_transport(self):
        return Bateau()

# Utilisation
def client_code(factory: TransportFactory):
    transport = factory.creer_transport()
    print(transport.livrer())

client_code(CamionFactory())  # Livraison par camion
client_code(BateauFactory())  # Livraison par bateau
