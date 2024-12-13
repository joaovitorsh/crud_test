from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Post
from .serializers import CareersSerializer


class CareersPagination(PageNumberPagination):
    """Classe para paginação personalizada de posts."""

    page_size = 10


class CareersViewSet(ViewSet):
    """Conjunto de views para operações de CRUD na API de posts."""

    def list(self, request):
        """Listar todos os posts com paginação."""
        queryset = Post.objects.all().order_by("-created_datetime")
        paginator = CareersPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = CareersSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    def create(self, request):
        """Criar um novo post."""
        serializer = CareersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Recuperar um post pelo ID."""
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CareersSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        """Atualizar um post existente."""
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        if any(field in ["id", "username", "created_datetime"] for field in data):
            raise ValidationError("Os campos 'id', 'username' e 'created_datetime' não podem ser alterados.")

        serializer = CareersSerializer(post, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Excluir um post existente."""
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
