#Iniciando o projeto

* Para iniciar o projeto rode 'make run' no terminal.

## Front-end

* Na parte de front foi utiliziado um site chamado bulma.
1. O container principal foi retirado da parte de exemplos de tample (https://bulma.io/documentation/overview/start/).
2. O cabeçalho foi retirado da parte de layout/Hero/Primary hero (https://bulma.io/documentation/layout/hero/).
3. A barra de navegação foi retirada da parte de Components/Navbar (https://bulma.io/documentation/components/navbar/).
4. O rodapé Bulma é um contêiner simples, com muito preenchimento na parte inferior, o que o torna ótimo como o último elemento de qualquer página da web. Retirado de Layout/Footer (https://bulma.io/documentation/layout/footer/).
5. Os restaurantes serão feitos utilizando cards, encontrados na parte de Componentes/Card (https://bulma.io/documentation/components/card/).
6. Para colocar varios cards foi preciso adicionar colunas, retiradas de Columns (https://bulma.io/documentation/columns/basics/).
7. Os tampletes foram componentizados utilizando o {% block nome %} / {% endblock nome %}.
8. O tamplate base contém as coisas comum para todo o site, o restante apenas o que for específico dele. Utilizando os blocos
é possível sobrepor o bloco desejavel, com o comando {% extends  "base.html" %} no template que vai herdar o base.
9. Com o intuito de reutilizar algum código é criado as macros.
10. A conexão do front com as paginas é feita atraves das rotas de http:
```
            <a class="navbar-item" href="{{url_for('site.restaurants')}}">
              Restaurantes
            </a>
```
onde o href utiliza uma função do flask (url_for()) para indicar a rota utilizada.
11. A extensão flask_debugtoolbar é utilizada para fazer o debug dos tamplate, para utiliza-lá é necessário
criar um config com uma chave secreta.

## SQLite

* Consultas estruturais
1. CREATE TABLE
2. ALTER TABLE
3. DROP TABLE

* Consultas de dados
1. CRUD: Create - Read - Update - Delete
    1. Create: INSERT INTO nomeDaTabela VALUE(....);
    2. Read: SELECT campoDesejavel from nomeDaTabela;
    3. Update: UPDATE nomeDaTabela SET campoAserMudado where;
    4. Delete: DELETE from nomeDaTabela where;

* Cadastro de usuarios no banco de dados através do python:

1. flask shell
2. from apilanches.ext.db import db
3. from apilanches.ext.site.model import User, Store, Category
4. Novo usuário: user = User(email = 'ss', password = 'ss', admin=True)
5. Adicionar o user no banco de dados: db.session.add(user) e depois db.session.commit()

* Atualização do banco de dados utilizando o migrate do flask

1. Sempre que mudar os atributos de uma classe que espelha o banco de dados é preciso rodar
o comando:
  1. flask db init
  2. flask db migrate -m "initial migrate"
  3. flask db migrate -m "add novoAtributo to ClasseDoNovoAtributo" (Um novo arquivo será adicionado a pasta migrations/versions)
  4. flask db upgrade

* Configurações
1. As configurações são feitas utilizando um arquivo .toml e o dynaconf para ler esse arquivo. No __init__ do config, basta ter o seguinte código:

```
from dynaconf import FlaskDynaconf

def init_app(app):
    FlaskDynaconf(app)
    #app.config.load_extensions("EXTENSIONS")

```

O proprio dynaconf procura por padrão arquivos com o nome conffig e .secrets .toml.

* Formulários: permitem que o usuário preencha inputs e envie para a aplicação. Formulários podem ser feitos utilizando html puro, no qual retorna uma string ou através de classes.

1. html puro:

```
@app.route("/form")
def formulario():
  return (
    "<form action = '/receiver' method='POST' enctype='multipart/form-data'>"
      "<label for'username'>Username:</label> "
      "<input type = 'text' name = 'username' /><br>"
      "<label for'lastname'>Lastname:</label> "
      "<input type = 'text' name = 'lastname' /><br>"
      "<input type = 'file' name = 'arquivo' /><br>"
      "<input type = 'submit' value = 'enviar' />"
    "</form>"
    )
```
O input pode ser um botão, uma caixa de texto, entre outros. Ao criar um input deve-se definir seu tipo, no caso do text, o parametro name indica o que vai escrito no bloco. E o tipo submit é um botão de enviar. O type igual a file cria um botão que permite enviar um arquivo. O enctype='multipart/formdata' diz para o formulário que ele pode aceitar arquivos os bits do arquivo submitido.

Quando um Formulário não tem seu método específicado ele entende get por padrão. A action define que o formulario enviara os dados para o caminho '/receiver', definido na função abaixo:

```
# O objeto request do flask, é um objeto de requisição criado pelo flask
import request

@app.route("\receiver", methods=["POST"])
def receiver():
  __import__("ipdb").set_trace()
  return f"{request.values}"
```
Quando ocorrer uma requesição no url "\receiver" o flask vai criar um objeto que recebe todas as informações passadas e vai jogar dentro da função, no qual dentro da função temos acesso ao objeto request.

O paramêtro methods dentro do app.route define que tipo de metodos http a função pode receber.



* Debug

Para debugar o código foi utilizado o pdb padrão do python.

1. request.form: acessa os dados enviados via request.
2. request.files: acessa os dados no caso de arquivos de multipart (como imagens).
