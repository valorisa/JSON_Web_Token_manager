import jwt
import os
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

# Chemin vers les fichiers de clés RSA (privée et publique)
PRIVATE_KEY_PATH = "private.pem"
PUBLIC_KEY_PATH = "public.pem"

# Fonction pour générer un JWT signé avec RS256
def generate_jwt():
    if not os.path.exists(PRIVATE_KEY_PATH):
        print(f"Erreur : Le fichier de clé privée {PRIVATE_KEY_PATH} est introuvable.")
        return

    with open(PRIVATE_KEY_PATH, "r") as private_key_file:
        private_key = private_key_file.read()

    payload = {
        "sub": "1234567890",
        "name": "John Doe",
        "admin": True,
        "iat": 1739220356,
        "exp": 1739223956
    }

    token = jwt.encode(payload, private_key, algorithm="RS256")
    print("JWT généré avec succès :")
    print(token)
    return token

# Fonction pour vérifier un JWT signé avec RS256
def verify_jwt(token):
    if not os.path.exists(PUBLIC_KEY_PATH):
        print(f"Erreur : Le fichier de clé publique {PUBLIC_KEY_PATH} est introuvable.")
        return

    with open(PUBLIC_KEY_PATH, "r") as public_key_file:
        public_key = public_key_file.read()

    try:
        decoded_token = jwt.decode(token, public_key, algorithms=["RS256"])
        print("Token valide. Contenu :")
        print(decoded_token)
    except jwt.ExpiredSignatureError:
        print("Erreur : Token expiré.")
    except jwt.InvalidTokenError:
        print("Erreur : Token invalide.")

# Fonction pour générer les clés RSA
def generate_rsa_keys():
    key = RSA.generate(2048)  # Générer une clé RSA de 2048 bits
    private_key = key.export_key()
    with open(PRIVATE_KEY_PATH, "wb") as private_key_file:
        private_key_file.write(private_key)
    
    public_key = key.publickey().export_key()
    with open(PUBLIC_KEY_PATH, "wb") as public_key_file:
        public_key_file.write(public_key)
    
    print("Clés RSA générées avec succès.")
    print(f"Clé privée enregistrée dans {PRIVATE_KEY_PATH}")
    print(f"Clé publique enregistrée dans {PUBLIC_KEY_PATH}")

# Menu principal
def main():
    while True:
        print("\n🎯 Menu Principal :")
        print("1. Générer un JWT")
        print("2. Vérifier un JWT")
        print("3. Générer les clés RSA (si elles n'existent pas)")
        print("4. Quitter")
        choix = input("Choisissez une option (1-4) : ")

        if choix == "1":
            generate_jwt()
        elif choix == "2":
            token = input("Entrez le JWT à vérifier : ")
            verify_jwt(token)
        elif choix == "3":
            if not os.path.exists(PRIVATE_KEY_PATH) or not os.path.exists(PUBLIC_KEY_PATH):
                generate_rsa_keys()
            else:
                print("Les clés RSA existent déjà.")
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir une option entre 1 et 4.")

if __name__ == "__main__":
    main()
