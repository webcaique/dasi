# ANOTAÇÕES SOBRE COMO FUNCIONA O DJANGO
## INICIALIZAR O AMBIENTE VIRTUAL
https://github.com/dasiusp/VenDASI?tab=readme-ov-file => Link para inicializar

python -m venv venv
### Ubuntu
- sudo apt install python3-venv
- source venv/bin/activate
- deactivate

## BAIXAR O DJANGO
- pip install django

## INICIALIZANDO UM PROJETO
- django-admin => usa a permissão de admin
- django-admin createproject => criar o projeto (recomendável criar uma pasta para o projeto)
- django-admin startproject nameProject
- python manage.py runserver => inicializa o server

## CONFIGURANDO -- setting.py
- BASE_DIR = Path(__file__).resolve().parent.parent => /home/caique-s/Documentos/USP/dasi/ti/treinamento/python/django-learning/try-django/trydjango/djangoProject (caminho do projeto)
- DEBUG = False em num ambiente de trabalho
- DEGUB = True para testes e aprendizagem
- INSTALLED_APPS => tem um blog, sites, apps, components
- MIDLEWARE => REQUESTS, como secure etc
- ROOT_URLCONF = sabe qual é a url que estã usando
- TEMPLATE = Como as coisas funcionam
- WSGU_Aplication = Como o server funciona
- DATABASES = onde vai estar as bases de dados
- AUTH_PASSWORD_VALIDATOR => passwords
- static_urls = onde vai estar os htmls, js's e css's

------- SUPER IMPORTANTE -----------------------
- python manage.py migrate => toda vez que atualizar qualquer coisa no APP, migrar para o ambiente de produção
- python manage.py makemigrations
------- SUPER IMPORTANTE -----------------------

## CONSTRUINDO COMPONENTES
### Configurando o INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third-app

    #own-app
    'nameApp',
]

- python manage.py createsuperuser => criar um usuário "admin"
- http://127.0.0.1:8000/admin/ => gerenciar usuários e grupos
- python manage.py startapp nameApp => criar o app

#### nameApp/models.py => modelo no db
class nameApp(models.Model):
    title = models.TextField()
    description = models.TextField(default='Here')
    price = models.TextField()
    
#### nameApp/admin.py
from .models import nameApp

admin.site.register(nameApp)

Agora entrando em http://127.0.0.1:8000/admin/, o usuário pode cadastrar produtos pela tela

#### Criando o objeto pelo terminal
- python manage.py shell => abre o terminal da aplicação em formato de terminal de python
- from nameApp.models import nameApp => importa o app
- nameApp.object.all() => mostra a quantidade de objetos já cadastrado, e uma lista
- nameApp.objects.create(title="",description="",...)

#### Models
CharField(max_length=120) # max_length é requerido
TextField(blank=True, null=True) # blank permite ou não que o campo esteja vazio
DecimalField(decimal_places=2, max_digitis=100) #Representar decimal, decimal_place para numero de casas decimais, max_digitis para o número máximo da parte não decimal

#### MUDAR UM MODEL
Quando se adiciona um outro campo que não está nos antigos, por exemplo.
Colocar null=True ou default para preencher outros campos
Ou, quando for migrar, colocar um valor padrão.

### TROCAR HOMEPAGE PADRÃO PARA UMA CUSTOMIZADA
- python manage.py startapp pages
- Adicionar 'pages' ao INSTALLED_APPS
#### pages/views.py => caminhos para as páginas
adicionar:
from django.http import HttpResponse

def homepage_view(request, *args, **kargs):
#request.user
    #return "<h1>Hello World </h1>" => jeito inicial
    #return HttpResponse("<h1>Hello World </h1>") => jeito inicial

#### setting.py
ROOT_URLCONF

#### urls.py
- Importar o view para as urls
from pages import views ou from pages.views import homepage_view

urlpatterns = [
    #adicionar
    path('', views.homepage_view, name='home'), ou
    path('', homepage_view, name='home')
]


## ROTAS URL E CHAMADOS
urlpatterns = [
    #adicionar
    path('/page1', page1_view, name='page1'),
    path('/page2', page2_view, name='page2')
]

## DJANGO TEMPLATES
### pages/views.py
from django.http import HttpResponse

def homepage_view(request, *args, **kargs):
    return render(request,"home.html", {})
    
### Criar a pasta templates na raiz do projeto => onde vai ficar html

### settings.py
    TEMPLATES[
        {
            'DIR': [f'{BASE_DIR}/templates']
        }
    ]

## Django Templating Engine Basics
### Dentro do html
{{ comando }} => estrutura para usar recursos do python dentro do html
{{ request.user.is_authenticated }} => para identificar se o usuário é authenticado

### ROOT HTML => html que as outras páginas se basearam
- Como uma estrutura básica em todos os sites
#### root.html (na pasta dos templates)
<estrutura básica do html>
    {% block content %}replace{% endblock %}
</estrutura básica do html>
 
#### outros.html
{% extends 'root.html' %}
{% block content %}
    Conteudo que vai substituir o replace
{% endblock %}

## INCLUDE TEMPLATE TAG
### Fazer um html que sempre vai ser usado em outros códigos, como navbar
{% include 'navbar.html' %} => adiciona uma navbar no código que deseja

## RENDERING CONTEXT IN A TEMPLATE
- Mudar o conteúdo base dependendo da página
### pages/views.py
def page01_views(request, *args, **kargs):
    my_context = {
        "text":"A text",
        "number": 123,
        "list": [1,2,3,4],
    }
    return render(request, "page01.html", my_context)
    
### .html
{{ text }}, {{ number }}

## FOR LOOP IN A TEMPLATE
### no html
{% for item in list %}
    <tag>{{ forloop.counter }} - {{ item }} </tag>
{% endfor %}

## USING CONDITION IN A TEMPLATE
### html
{% if text == "text" %}
    <p> {{ text|add:22}} </p> #add adiciona valor
{% elif text=="my" %}
    <p></p>
{% else %}
    <p></p>
{% endif %}

## Template tags and filters => conferir a documentação do django
|add: => adiciona valor ou variáveis
|capfirst => capitalize
|upper
|safe => imprime tags
|title => tudo capitalizado

## Render Data From the Database with a Model
### no terminal
- Na pasta do projeto
- python manage.py shell
>>> from nameApp.models import appNameModel
>>> appModel.objects.get(id=1)
>>> obj = appModel.objects.get(id=1)
>>> dir(obj) # ver o que há no objeto, analisar o objeto
>>> obj.algo = acessar um espaço do objeto, como o elemento titulo

### views
from django.shortcuts import render
from .models import appNameModel

def appNameView(request):
    obj = appNameMode.objects.get(id=1)
    context = {
        'title': obj.title,
        'description':obj.description
    }
    context = {
        'object':obj,
    }
    render(request, "appName/index.html",{})


## How Django Templates Load with Apps

# IMPORTANTES
- python manage.py migrate => toda vez que atualizar qualquer coisa no APP, migrar para o ambiente de produção
- python manage.py makemigrations
- python manage.py createsuperuser => criar um "admin" (dever ser realizado toda vez que acontece é deletado o db)

