import socket
import threading
from EncryptionUtils import EncryptionUtils

def receive_messages(client_socket):
    while True:
        try:
            encrypted_message = client_socket.recv(1024)  # Receive encrypted message
            if not encrypted_message:
                break

            decrypted_message = EncryptionUtils.decrypt(encrypted_message)  # Decrypt and display
            print(f"{decrypted_message}")

        except Exception as e:
            print(f"Error: {e}")
            break
        
def send_messages(client_socket):
    while True:
        try:
            message = input("Enter message: ")  # Get input from user
            if message.lower() == 'quit':  # Allow user to quit
                client_socket.close()
                break
            
            full_message = f"{message}"    
            encrypted_message = EncryptionUtils.encrypt(full_message)  # Encrypt message
            client_socket.send(encrypted_message)  # Send encrypted message

        except Exception as e:
            print(f"Error: {e}")
            break

def main():
    while True:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 12345))  # Connect to the server
        
        # User can genereate id
        client_id = input("Create ID: ")
        
        encrypted_id = EncryptionUtils.encrypt(client_id)
        
        # Encode the string ID to bytes and send to server
        client_socket.send(encrypted_id)
        
        # Wait for server response about ID usage
        try:
            
            # get the response from server
            encrypted_response = client_socket.recv(1024)
            
            #decrypt the response from server
            decrypted_response = EncryptionUtils.decrypt(encrypted_response)
            
            #the id already exists
            if "ID already in use" in decrypted_response:
                print(decrypted_response)
                client_socket.close()
                continue  # Restart the connection process
            
            #check if user is connected to the server
            print(f"You are connected with ID: {client_id}")
            
            # Start thread to receive messages
            threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
            # Start thread to send messages
            send_messages(client_socket)
            
        except Exception as e:
            print(f"Error receiving ID verification: {e}")
            client_socket.close()
            continue



if __name__ == "__main__":
    main()
