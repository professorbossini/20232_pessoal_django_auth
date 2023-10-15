from django.urls import path
from exemplo_autenticacao_autorizacao_app.views import CadastroNovoUsuarioView
urlpatterns = [
    path('signup/', CadastroNovoUsuarioView.as_view(), name='signup'),
]
