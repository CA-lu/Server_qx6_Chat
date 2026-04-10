import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 12345))
server.listen()

print("Server läuft... wartet auf Clients")

clients = []

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            clients.remove(client)

while True:
    client, addresse = server.accept()
    print(f"Neuer Client: {addresse}")

    clients.append(client)

    client.send("Hallo".encode())

    while True:
        try:
            nachricht = client.recv(1024)
            if not nachricht:
                break

            print(nachricht.decode())
            broadcast(nachricht)

        except:
            clients.remove(client)
            client.close()
            break