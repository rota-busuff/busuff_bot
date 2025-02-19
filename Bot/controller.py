import requests

class Controle:

    @staticmethod
    def consultar():
        resposta = requests.get("https://8293-177-12-9-161.ngrok-free.app") #COLOCAR O LINK CERTO

        if (resposta.status_code != 200):
            dados = resposta.json()
            return dados
            '''
            return [
                {"rota": "Rota 1", "posicao": "Valonguinho", "mensagem": "20 min", "online": 1},
                {"rota": "Rota 2", "posicao": "HUAP", "mensagem": "25 min", "online": 1},
                {"rota": "Rota 3", "posicao": "Valonguinho", "mensagem": "0 min", "online": 0},
                {"rota": "Rota 4", "posicao": "Praia Vermelha \(Bloco H\)", "mensagem": "1 hora", "online": 1},
            ]
            '''
        else:
            return None