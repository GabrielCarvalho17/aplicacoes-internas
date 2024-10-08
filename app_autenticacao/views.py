from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from .serializers import CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer, UsuarioSerializer
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer


@extend_schema(
    tags=["Usuários"],
)
class UsuarioView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]


@extend_schema(
    tags=["Autenticação"],
    description="Endpoint para obtenção de tokens JWT.",
    responses={200: TokenObtainPairSerializer}
)
class ObterTokensView(TokenObtainPairView):
    permission_classes = []  # Nenhuma permissão exigida
    authentication_classes = []  # Nenhuma autenticação exigida
    serializer_class = CustomTokenObtainPairSerializer

@extend_schema(
    tags=["Autenticação"],
    description="Endpoint para atualização de tokens JWT.",
    responses={200: TokenRefreshSerializer}
)
class RenovarTokensView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer


