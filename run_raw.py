from flask import Flask, request, jsonify
from barcode import Code128
from barcode.writer import ImageWriter

app = Flask(__name__) # Criando um servidor em Flask

# Criando a rota
# A partir do flask faremos uma requisição pra esta rota
@app.route('/create_tag', methods=["POST"])
def create_tag():
    body = request.json
    product_code = body.get('product_code')

    tag = Code128(product_code, writer=ImageWriter())
    path_from_tag = f'{tag}'
    tag.save(path_from_tag)

    return jsonify ({ "tag path": path_from_tag })

if __name__ == '__main__': # Rodar o servidor
    app.run(host='0.0.0.0', port=3000) # Rodando no localhost (0.0.0.0) e na porta 3000
