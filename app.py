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
    # listar todas as senhas

class RequisicaoHnalder(BaseHTTPRequestHandler):
    fila_atendimento = FilaAtendimento()

    def _set_heaaders(self, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
    
    def do_POST(self):
        if self.path == "/senha0":
            senha = self.fila_atendimento.gerar_senha()
            self._set_heaaders(201)
            self.wfile.write(json.dumps({"senha": senha}).encode())
        else:
            self._set_heaaders(404)
            self.wfile.write(json.dumps({"message": "Rota não encontrada"}).encode())

def run():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequisicaoHnalder)
    print("API rodando em http://localhost:8080")
    httpd.serve_forever()

if __name__ == "__main__":
    run()   