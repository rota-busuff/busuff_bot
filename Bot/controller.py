import requests

class Controle:

    @staticmethod
    def rastrear():
        resposta = requests.get("https://8293-177-12-9-161.ngrok-free.app") #COLOCAR O LINK CERTO

        if (resposta.status_code != 200):
            dados = resposta.json()
            return dados
            '''
            return [
                {"rota": "Rota 1", "localizacao": "Valonguinho", "previsao": "20 min", "online": 1},
                {"rota": "Rota 2", "localizacao": "HUAP", "previsao": "25 min", "online": 1},
                {"rota": "Rota 3", "localizacao": "Valonguinho", "previsao": "0 min", "online": 0},
                {"rota": "Rota 4", "localizacao": "Praia Vermelha \(Bloco H\)", "previsao": "1 hora", "online": 1},
            ]
            '''
        else:
            return None