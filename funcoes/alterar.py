from flask import jsonify, request

def alterar_pessoa():
    dados = request.get_json()
    # Aqui você pode adicionar lógica para alterar o cadastro
    return jsonify({'mensagem': f"Cadastro alterado: {dados}"})
