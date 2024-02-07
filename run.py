from src.main.server.server import app

# Executa o app (servidor)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

# - debug=True: Atualiza e roda o servidor se alterar algo no código
