from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#lista
filmes = []

@app.route('/')
def index():
    return render_template('index.html', filmes=filmes)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/adicionar_filme', methods=['GET', 'POST'])
def adicionar_filme():
    """
    Rota para incluir um novo filme.
    Se o método for POST, adiciona o novo filme à lista.
    Se não, exibe o formulário para adicionar um novo filme.
    """
    if request.method == 'POST':
        nomefilme = request.form['nome']
        lancamento = request.form['lancamento']
        genero = request.form['genero']
        duracao = request.form['duracao']
        codigo = len(filmes)
        filmes.append([codigo, nomefilme, lancamento, genero, duracao])
        return redirect('/mais')  # Redireciona de volta para a página inicial
    else:
        return render_template('adicionar_filme.html')  # Renderiza o formulário de adicionar filme


@app.route('/editar_filme/<int:codigo>', methods=['GET', 'POST'])
def editar_filme(codigo):
    """
    Rota para editar um filme existente.
    Se o método for POST, atualiza os detalhes do filme com o ID fornecido.
    Caso contrário, exibe o formulário preenchido com os detalhes do filme para edição.
    """
    if request.method == 'POST':
        nomefilme = request.form['nome']
        lancamento = request.form['lancamento']
        genero = request.form['genero']
        duracao = request.form['duracao']
        filmes[codigo] = [codigo, nomefilme, lancamento, genero, duracao]
        return redirect('/mais')  # Redireciona de volta para a página inicial
    else:
        filme = filmes[codigo]
        return render_template('editar_filme.html', filme=filme)  # Renderiza o formulário de edição


@app.route('/apagar_filme/<int:codigo>')
def apagar_filme(codigo):
    """
        Rota para excluir um filme existente.
    """
    del filmes[codigo]
    return redirect('/mais')  # Redireciona de volta para a página inicial

