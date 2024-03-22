from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Lista de produtos
produtos = []

# Função que retorna o conteúdo do template
def get_template_index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Lista de Produtos</title>
    </head>
    <body>
        <h1>Lista de Produtos</h1>
        <table border="1">
            <thead>
                <tr>
                    <th>Nome</th>
                    <th>Valor</th>
                </tr>
            </thead>
            <tbody>
                {% for produto in produtos %}
                    <tr>
                        <td>{{ produto.nome }}</td>
                        <td>R$ {{ produto.valor }}</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>

        <h2>Adicionar Produto</h2>
        <form action="/" method="post">
            <label for="nome">Nome do Produto:</label><br>
            <input type="text" id="nome" name="nome"><br>
            <label for="descricao">Descrição do Produto:</label><br>
            <input type="text" id="descricao" name="descricao"><br>
            <label for="valor">Valor do Produto:</label><br>
            <input type="text" id="valor" name="valor"><br>
            <label for="disponivel">Disponível para venda:</label><br>
            <select id="disponivel" name="disponivel">
                <option value="sim">Sim</option>
                <option value="nao">Não</option>
            </select><br>
            <input type="submit" value="Adicionar Produto">
        </form>
    </body>
    </html>
    '''

# Rota para a página inicial
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        valor = request.form['valor']
        disponivel = request.form['disponivel']

        produto = {
            'nome': nome,
            'descricao': descricao,
            'valor': valor,
            'disponivel': disponivel
        }

        produtos.append(produto)
        return redirect(url_for('index'))

    # Ordena os produtos pelo valor
    produtos_ordenados = sorted(produtos, key=lambda x: float(x['valor']), reverse=True)

    return render_template_string(get_template_index(), produtos=produtos_ordenados)

if __name__ == '__main__':
    app.run(debug=True)
