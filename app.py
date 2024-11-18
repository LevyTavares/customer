from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Classe para gerenciar Filas de atendimento
class FilaAtendimento:
    def __init__(self):
        self.fila = []
        self.proximo_numero = 1

    def gerar_senha(self):
        senha = self.proximo_numero
        self.fila.append(senha)
        self.proximo_numero += 1
        return senha
    
    def atender_cliente(self):
        if self.fila:
            return self.fila.pop(0)
        return None