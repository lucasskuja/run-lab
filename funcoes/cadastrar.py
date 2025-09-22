from flask import jsonify, request

def cadastrar_pessoa():
    dados = request.get_json()
    # Aqui você pode adicionar lógica para salvar a pessoa
    return jsonify({'mensagem': f"Pessoa cadastrada: {dados}"})
