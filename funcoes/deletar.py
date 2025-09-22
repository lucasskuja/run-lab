from flask import jsonify, request

def deletar_pessoa():
    dados = request.get_json()
    # Aqui você pode adicionar lógica para deletar a pessoa
    return jsonify({'mensagem': f"Pessoa deletada: {dados}"})
