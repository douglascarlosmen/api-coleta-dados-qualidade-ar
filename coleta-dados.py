from flask import Flask, request, jsonify
app = Flask(__name__)

# Armazenamento em memória para simplificação. Em um cenário real, considere um banco de dados.
dados_recebidos = []

# Endpoint para receber dados
@app.route('/dados', methods=['POST'])
def receber_dados():
    data = request.json  # Assumindo que os dados são enviados em formato JSON
    dados_recebidos.append(data)
    # Aqui, você pode adicionar qualquer lógica de processamento básica de dados
    processar_dados(data)
    return jsonify({"status": "Dados recebidos com sucesso"}), 200

# Função de processamento de dados básica
def processar_dados(data):
    # Implemente sua lógica aqui. Exemplo: calcular a média, identificar tendências, etc.
    print(f"Dados processados: {data}")  # Exemplo de log para demonstração

# Endpoint para recuperar dados armazenados (para verificação)
@app.route('/dados', methods=['GET'])
def ver_dados():
    return jsonify(dados_recebidos), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
