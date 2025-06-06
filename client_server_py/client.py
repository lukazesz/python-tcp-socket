import socket

def start_client():
    host = '10.10.29.112'
    port = 1025
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        
        client_socket.connect((host, port))
        print(f"Conectado ao servidor {host}:{port}")
        
        while True:
            message = input("Digite uma mensagem (ou 'sair' para encerrar):")
            
            if message.lower() == 'sair':
                break
            
            client_socket.sendall(message.encode('utf-8'))
            
            data = client_socket.recv(1024)
            print(f"Resposta do servidor: {data.decode('utf-8')}")
        print("Conexão encerrada.")
        
if __name__ == "__main__":
    start_client()