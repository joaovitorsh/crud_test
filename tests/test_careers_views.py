import pytest
from careers.models import Post
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    """Cliente de teste para interagir com a API."""
    return APIClient()


@pytest.fixture
def post_data():
    """Dados válidos para criar um novo post."""
    return {"username": "test_user", "title": "Título de Teste", "content": "Conteúdo de teste para o post."}


@pytest.fixture
def create_posts():
    """Cria posts no banco de dados para testes."""
    posts = [
        Post.objects.create(username="user1", title="Postagem 1", content="Conteúdo do Post 1"),
        Post.objects.create(username="user2", title="Postagem 2", content="Conteúdo do Post 2"),
    ]
    return posts


@pytest.mark.django_db
def test_list_posts(api_client, create_posts):
    """Teste para listar posts."""
    url = "/careers/"
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data["results"]) == len(create_posts)
    sorted_posts = sorted(create_posts, key=lambda post: post.created_datetime, reverse=True)
    assert response.data["results"][0]["title"] == sorted_posts[0].title


@pytest.mark.django_db
def test_create_post(api_client, post_data):
    """Teste para criar um post."""
    url = "/careers/"
    response = api_client.post(url, post_data)
    assert response.status_code == 201
    assert Post.objects.filter(title=post_data["title"]).exists()


@pytest.mark.django_db
def test_retrieve_post(api_client, create_posts):
    """Teste para recuperar um post específico."""
    post = create_posts[0]
    url = f"/careers/{post.id}/"
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data["title"] == post.title


@pytest.mark.django_db
def test_update_post(api_client, create_posts):
    """Teste para atualizar um post."""
    post = create_posts[0]
    url = f"/careers/{post.id}/"
    updated_data = {"title": "Título Atualizado", "content": "Conteúdo atualizado para o post."}
    response = api_client.put(url, updated_data)
    assert response.status_code == 200
    post.refresh_from_db()
    assert post.title == updated_data["title"]


@pytest.mark.django_db
def test_partial_update_post(api_client, create_posts):
    """Teste para atualização parcial de um post."""
    post = create_posts[0]
    url = f"/careers/{post.id}/"
    updated_data = {"content": "Atualização parcial do conteúdo."}
    response = api_client.put(url, updated_data)
    assert response.status_code == 200
    post.refresh_from_db()
    assert post.content == updated_data["content"]


@pytest.mark.django_db
def test_delete_post(api_client, create_posts):
    """Teste para exclusão de um post."""
    post = create_posts[0]
    url = f"/careers/{post.id}/"
    response = api_client.delete(url)
    assert response.status_code == 204
    assert not Post.objects.filter(id=post.id).exists()


@pytest.mark.django_db
def test_invalid_post_creation(api_client):
    """Teste para verificar erros ao criar um post com dados inválidos."""
    url = "/careers/"
    invalid_data = {
        "username": "test_user",
        "content": "Falta o título.",  # Título ausente
    }
    response = api_client.post(url, invalid_data)
    assert response.status_code == 400
    assert "title" in response.data
