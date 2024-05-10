import socket
import threading
from EncryptionUtils import EncryptionUtils

clients = {}

def handle_client(client_socket,client_id):
    while True:
        try:
            ciphertext = client_socket.recv(1024)  # Receive encrypted data
            if not ciphertext:
                break

            decrypted_message = EncryptionUtils.decrypt(ciphertext)
            message_display = f"{client_id}: {decrypted_message}"
            print(f"Message from {client_id}: {decrypted_message}")

            # Encrypt and relay to all clients
            encrypted_message = EncryptionUtils.encrypt(message_display)
            for id, client in clients.items():
                if client != client_socket:
                    client.send(encrypted_message)

        except Exception as e:
            print(f"Error: {e}")
            break

    clients.pop(client_id, None)
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 12345))  # Bind server to localhost and port 12345
    server_socket.listen(10)  # Listen for up to 10 clients

    while True:
        client_socket, addr = server_socket.accept()  # Accept a new client connection
        encrypted_client_id = client_socket.recv(1024) # First message is the client ID
        
        decrypted_client_id = EncryptionUtils.decrypt(encrypted_client_id)
        
        if decrypted_client_id in clients:
            client_socket.send(EncryptionUtils.encrypt("ID already in use. Please reconnect with a different ID."))
        else:
            
            clients[decrypted_client_id] = client_socket
            print(f"Client {decrypted_client_id} connected from {addr}")
            
            # Send confirmation to the client
            confirmation_message = "ID accepted. You are now connected."
            client_socket.send(EncryptionUtils.encrypt(confirmation_message))

            # Start handling client in a separate thread
            client_thread = threading.Thread(target=handle_client, args=(client_socket,decrypted_client_id))
            client_thread.start()

if __name__ == "__main__":
    main()
