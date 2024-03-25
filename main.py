from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de produtos
produtos = []

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

    return render_template('index.html', produtos=produtos_ordenados)

if __name__ == '__main__':
    app.run(debug=True)
