# por convensão o teste do pytest sempre é uma função que começa com test_ 
# a palavra assert espera que o resultado seja true, se for falso significa que o teste falhou.


def test_app_is_created(app):
    '''
    Função que testa se a aplicação foi criada.
    Recebe como argumento a instância app definida no arquivo conftest.py
    '''
    assert app.name == 'apilanches.app'

def test_config_is_loaded(config):
    assert config['DEBUG'] is False

def test_request_returns_404(client):
    '''
    O argumento client é um função que emula uma requisição http sem a necessidade
    da aplicação estar rodando.
    '''
    assert client.get('/url_não_existe').status_code == 404

