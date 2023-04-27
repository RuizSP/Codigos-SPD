import xmlrpc.server

mensagens = []

def enviar_mensagem(mensagem):
    mensagens.append(mensagem)
    print(f"Mensagem recebida: {mensagem}")
    return ""

def ler_mensagens():
    return mensagens

with xmlrpc.server.SimpleXMLRPCServer(("172.25.5.184", 8000)) as servidor:
    servidor.register_function(enviar_mensagem)
    servidor.register_function(ler_mensagens, "ler_mensagens")
    print("Servidor pronto para receber conexões.")
    servidor.serve_forever()
