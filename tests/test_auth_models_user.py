import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create() -> None:
    User.objects.create_user(username="john", password="pass1234")

    assert User.objects.count() == 1
    user = User.objects.first()
    assert user.username == "john" # type: ignore[union-attr]
    assert user.is_active is True  # type: ignore[union-attr]
    assert user.is_staff is False  # type: ignore[union-attr]
