import socket

def start_server():
    host = '127.0.0.1'
    port = 8520
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
         
        server_socket.listen(1)
        print(f'Servidor iniciado. Aguardando conexões em {host}:{port}...')
        
        conn,addr = server_socket.accept()
        with conn:
            print(f'Conexão estabelecida com {addr}')
            
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                message = data.decode('utf-8')
                print(f'Mensagem recebida do cliente: {message}')
                
                response = f'Servidor recebeu: {message}'
                conn.sendall(response.encode('utf-8'))
            print('Contexão encerrada')
                
if __name__ == "__main__":
    start_server()    