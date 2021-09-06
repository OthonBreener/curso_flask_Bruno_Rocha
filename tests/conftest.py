import pytest
from apilanches.app import create_app

@pytest.fixture(scope="module")
def app():
    '''
    Instância principal do app flask
    '''
    return create_app()