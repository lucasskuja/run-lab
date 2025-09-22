
from flask import Flask
from funcoes.cadastrar import cadastrar_pessoa
from funcoes.alterar import alterar_pessoa
from funcoes.deletar import deletar_pessoa

app = Flask(__name__)

# Rota para cadastrar pessoa
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    return cadastrar_pessoa()

# Rota para alterar cadastro
@app.route('/alterar', methods=['PUT'])
def alterar():
    return alterar_pessoa()

# Rota para deletar pessoa
@app.route('/deletar', methods=['DELETE'])
def deletar():
    return deletar_pessoa()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
