"""coach URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Foi importado da pasta 'website' o arquivo 'views.py', ou seja, todas as suas funções podem ser utilizadas aqui
from website import views

# Aqui estão todos os urls para todas as páginas que o projeto tem
urlpatterns = [

    # Aqui está dizendo que quando o endereço com a extensão admin/ for acessado, a função url que está nos dicionário admin.site deve ser executada.
    path('admin/', admin.site.urls),

    # Como aqui o espaço é vázio, quer dizer que quando acessar o site 'cru', ele deve executar a função index que está dentro do arquivo views.py
    path('', views.index),

    # Depois que foi criado a página listar_coachs, foi necessário adicionar mais um endereço que é o 'listar/coachs' que ao ser acessado irá executar a função 'listar_coachs' que está no arquivo views.py
    path('listar/coachs', views.listar_coachs)
]
