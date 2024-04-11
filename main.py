from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de produtos
produtos = []

# Rota para a página inicial
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':  # Verifica se a requisição é do tipo POST
        # Obtém os dados do formulário enviado
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        valor = request.form.get('valor')
        disponivel = request.form.get('disponivel')

        # Verifica se todos os campos foram preenchidos
        if nome and descricao and valor and disponivel:
            try:
                valor = float(valor)  # Converte o valor para float
                # Cria um dicionário para representar o produto
                produto = {
                    'nome': nome,
                    'descricao': descricao,
                    'valor': valor,
                    'disponivel': disponivel
                }

                # Adiciona o produto à lista de produtos
                produtos.append(produto)

                # Redireciona de volta para a página inicial após a submissão do formulário
                return redirect(url_for('index'))
            except ValueError:
                return "Erro: O valor do produto deve ser numérico."

        else:
            return "Erro: Todos os campos devem ser preenchidos."

    # Ordena os produtos pelo valor antes de exibi-los
    produtos_ordenados = sorted(produtos, key=lambda x: float(x['valor']), reverse=True)

    # Renderiza o template 'index.html' passando a lista de produtos ordenados
    return render_template('index.html', produtos=produtos_ordenados)

if __name__ == '__main__':
    app.run(debug=True)  # Executa a aplicação Flask em modo de depuração
