import socket
import time

def main():
    # Se connecter à localhost sur le port 4000
    HOST = "localhost"
    PORT = 4000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print(f"Connecté à {HOST}:{PORT}")

        while True:
            data = client.recv(1024)  # Recevoir les données du serveur
            if not data:
                break  # Sortir si aucune donnée n'est reçue
            
            received_string = data.decode('utf-8').strip()  # Supprimer les espaces autour
            print(f"{received_string}")

            # Extraire la partie après les '>>>'
            if '>>>' in received_string:
                message = received_string.split('>>>')[-1].strip()  # Récupérer ce qui est après '>>>'
            else:
                message = received_string

            # Inverser la chaîne de caractères
            reversed_string = message[::-1]

            print(f"{reversed_string}")
            
            # Envoyer la chaîne inversée au serveur
            client.sendall(f"{reversed_string}\n".encode('utf-8'))
            time.sleep(0.5)


            

if __name__ == "__main__":
    main()
