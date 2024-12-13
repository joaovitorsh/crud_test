import pytest
from careers.models import Post


@pytest.mark.django_db
def test_post_create():
    post = Post.objects.create(username="john_doe", title="Test Title", content="This is a test content.")
    assert Post.objects.count() == 1
    assert post.username == "john_doe"
    assert post.title == "Test Title"
    assert post.content == "This is a test content."


@pytest.mark.django_db
def test_post_retrieve():
    post = Post.objects.create(username="john_doe", title="Test Title", content="This is a test content.")
    retrieved_post = Post.objects.get(id=post.id)
    assert retrieved_post.username == "john_doe"
    assert retrieved_post.title == "Test Title"
    assert retrieved_post.content == "This is a test content."


@pytest.mark.django_db
def test_post_update():
    post = Post.objects.create(username="john_doe", title="Test Title", content="This is a test content.")
    post.title = "Updated Title"
    post.content = "This is updated content."
    post.save()

    updated_post = Post.objects.get(id=post.id)
    assert updated_post.title == "Updated Title"
    assert updated_post.content == "This is updated content."


@pytest.mark.django_db
def test_post_delete():
    post = Post.objects.create(username="john_doe", title="Test Title", content="This is a test content.")
    post_id = post.id
    post.delete()
    with pytest.raises(Post.DoesNotExist):
        Post.objects.get(id=post_id)
