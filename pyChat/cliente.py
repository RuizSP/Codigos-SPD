import xmlrpc.client
import os
proxy = xmlrpc.client.ServerProxy("http://172.25.5.184:8000/")

while True:
    os.system('clear') or None
    mensagens = proxy.ler_mensagens()
    print("Mensagens recebidas:")
    for m in mensagens:
        print(m)
    mensagem = input("Digite sua mensagem: ")
    proxy.enviar_mensagem(mensagem)
    
