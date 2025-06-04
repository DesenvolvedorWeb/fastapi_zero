from http import HTTPStatus

import pytest


def test_root_retorna_ola_mundo(client):
    """Testa se a rota raiz retorna uma página HTML com a mensagem correta."""
    # Act
    response = client.get('/')
    # Assert
    assert response.status_code == HTTPStatus.OK
    # Como estamos retornando HTML, não podemos verificar o JSON
    # Em vez disso, verificamos se a string está no conteúdo HTML
    assert 'FastAPI Zero' in response.text


def test_dashboard_retorna_status_ok(client):
    """Testa se a rota dashboard retorna status 200 OK."""
    # Act
    response = client.get('/dashboard')
    # Assert
    assert response.status_code == HTTPStatus.OK
    assert 'Bem-vindo ao Dashboard!' in response.text


def test_dashboard_contem_estatisticas(client):
    """Testa se a página de dashboard contém as estatísticas esperadas."""
    # Act
    response = client.get('/dashboard')
    # Assert
    assert response.status_code == HTTPStatus.OK
    # Verificar se os elementos esperados estão presentes no HTML
    assert 'Usuários' in response.text
    assert 'Ativos' in response.text
    assert 'Requisições' in response.text
    # Verificar se os valores estão presentes (como strings no HTML)
    assert '1250' in response.text  # número de usuários
    assert '847' in response.text  # usuários ativos
    assert '12345' in response.text  # requisições


def test_static_files_sao_servidos(client):
    """Testa se os arquivos estáticos estão sendo servidos corretamente."""
    # Act - tentar acessar um arquivo CSS ou JS que sabemos que existe
    response = client.get('/static/css/styles.css')
    # Assert
    assert response.status_code == HTTPStatus.OK
    # Verificar o tipo de conteúdo
    assert 'text/css' in response.headers['content-type']


def test_api_stats_retorna_json_valido(client):
    """Testa se a API de estatísticas retorna JSON válido com os dados esperados."""
    # Act
    response = client.get('/api/stats')
    expected_response_01 = 1250  # Número de usuários esperado
    expected_response_02 = 847  # Número de usuários ativos esperado
    expected_response_03 = 12345  # Número de requisições esperado
    # Assert
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data['success'] is True
    assert 'data' in data
    assert data['data']['users'] == expected_response_01
    assert data['data']['active'] == expected_response_02
    assert data['data']['requests'] == expected_response_03


@pytest.mark.parametrize(
    ('path', 'expected_text'),
    [('/', 'Olá Mundo!'), ('/dashboard', 'Bem-vindo ao Dashboard!')],
)
def test_rotas_retornam_textos_esperados(client, path, expected_text):
    """Testa múltiplas rotas para verificar se retornam os textos esperados."""
    # Act
    response = client.get(path)
    # Assert
    assert response.status_code == HTTPStatus.OK
    assert expected_text in response.text


def test_retorna_lista_de_usuarios(client):
    """Testa se a rota /api/users retorna uma lista de usuários."""
    # Act
    response = client.get('/api/users')
    # Assert
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert isinstance(data, list)  # Verifica se é uma lista
    assert len(data) > 0  # Verifica se a lista não está vazia
    for user in data:
        assert 'username' in user
        assert 'email' in user
        assert 'role' in user
