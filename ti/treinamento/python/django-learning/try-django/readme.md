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

## How Django Templates Load with Apps => para reutilizar o código ou distribuir para outros
- criar uma pasta template dentro do app que quer reutilizar e utiliazr a mesma estrutura que utiliza no o##a no APP, migrar para o ambiente de produção

## Django Model Forms
- criar um forms.py no pasta do app
#### no forms.py
from django import forms
from .models import nameProductModel

class nameAppModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'titel',
            'description',
            'price'
        ]

#### no views.py
- add:
from .forms import nameAppModelForm

def name_create_view(resquest):
    form = nameAppModelForm(resquest.POST or None)
    if form.is_valid():
        form.save()
        form = nameAppModelForm() # reinicia o formulário
        
    context = {
        'form':form
    }
    return render(request,"name.html", context)

#### no name.html
<form method="POST"> {% csrf_token %}
{{ form.as_p }}
<input type='submit' value='Save' />
</form>

## Raw HTML Form
#### no html
<form action='.' method='POST'> {% csrf_token %}
    <input type='text' name='title' /> # name => ser igual do model boas práticas
    
    <input type='submit' value='Save' />
</form>

<form action='/search/' method='GET'>
    <input type='text' name='title' /> # name => ser igual do model boas práticas
    
    <input type='submit' value='Save' />
</form>

#### no views.py
- add:
from .forms import nameAppModelForm

def name_create_view(resquest):
    context = {}
    if request.method == "POST":
        new_title = request.POST.get('title')
        # nameModel.objects.create(title=new_title)
    return render(request,"name.html", context)

## PURE DJANGO FORM
#### no views.py
- add:
from .forms import nameAppModelForm, RawDjangoForm


def name_create_view(resquest):
    a_form = RawDjangoForm()
    if resquest.method == "POST":
        a_form = RawDjangoForm(request.POST)
        if a_form.is_valid():
            # now data is good
            print(a_form.cleaned_data)
            nameModel.objects.create(**a_form.cleaned_data) #cadastra
        else:
            print(a_form.errors)
    context = {
        'form': a_form,
    }
    return render(request,"name.html", context)

#### no forms.py
class RawDjangoForm(forms.Form):
    title       = forms.CharField()
    description = forms.CharField()
    price       = forms.DecimalField()
    
#### no .html
<form action='.' method='POST' > {% csrf_token %}
    {{ form.as_p }}
    <input type='submit' value='Save' />
</form>

## FORM WIDGETS
widget => usado para adicionar atributos html aos elementos
class RawDjangoForm(forms.Form):
    title       = forms.CharField(required=True,
                                  label='',
                                  widget=forms.TextInput(
                                        attrs={
                                            "placeholder":"Title"
                                        }
                                    )
                                  )
    description = forms.CharField(
                                widget=forms.Textarea(
                                attrs={
                                        "class":"class-name",
                                        "id":"id_name",
                                        "rows":100,
                                        "cols": 120
                                    }
                                )
    price       = forms.DecimalField(initial=199.99)

## FORM VALIDATION METHODS
#### views.py
from .forms import nameAppModelForm

def name_create_view(resquest):
    form = nameAppModelForm(resquest.POST or None)
    if form.is_valid():
        form.save()
        form = nameAppModelForm() # reinicia o formulário
        
    context = {
        'form':form
    }
    return render(request,"name.html", context)

#### forms.py
from django import forms
from .models import nameProductModel

class nameAppModelForm(forms.ModelForm):
    title       = forms.CharField(required=True,
                                  label='',
                                  widget=forms.TextInput(
                                        attrs={
                                            "placeholder":"Title"
                                        }
                                    )
                                  )
    description = forms.CharField(
                                widget=forms.Textarea(
                                attrs={
                                        "class":"class-name",
                                        "id":"id_name",
                                        "rows":100,
                                        "cols": 120
                                    }
                                )
    price       = forms.DecimalField(initial=199.99)
    
    class Meta:
        model = Product
        fields = [
            'titel',
            'description',
            'price'
        ]
    
    def clean_<field_name>(self, *args, **kargs):
        title = self.cleaned_data.get("title")
        if <condition>:
            return title
        else:
            raise forms.ValidationError("This is not a valid title")
    
OU

class nameAppModelForm(forms.Form):
    title       = forms.CharField(required=True,
                                  label='',
                                  widget=forms.TextInput(
                                        attrs={
                                            "placeholder":"Title"
                                        }
                                    )
                                  )
    description = forms.CharField(
                                widget=forms.Textarea(
                                attrs={
                                        "class":"class-name",
                                        "id":"id_name",
                                        "rows":100,
                                        "cols": 120
                                    }
                                )
    price       = forms.DecimalField(initial=199.99)
    
    def clean_<field_name>(self, *args, **kargs):
        title = self.cleaned_data.get("title")
        if <condition>:
            return title
        else:
            raise forms.ValidationError("This is not a valid title")


##Initial Values for Forms => dados iniciais
#### no arquivo de views
from .forms import RawDjangoForm, nameAppModelForm
from .models import nameModel

def render_initial_data(request):
    initial_data = {
        'title': "Title",
        
    }
    obj = Product.objects.get(id=1)
    #form = RawDjangoForm(request.POST or None, initial=initial_data)
    form = nameAppModelForm(request.POST or None, initial=initial_data, instance=obj)
    if form.is_valid(): # instance vai fazer atualizar o objeto dentro dele
        form.save()
    context = {
        'form':form
    }
    return render(request,"name.html", context)

## DYNAMIC URL ROUTING
#### no views.html
from django.shortcuts import render
from .models import nameModel

def dynamic_lookup_view(request, my_id):
    obj = Product.object.get(id=my_id)
    context = {
        'object': obj
    }
    return render(request, "name.html", context)

#### urls.py (importando o dynamic_lookup_view)
urlpatterns = [
    path('namePge/<int:my_id>/',dynamic_lookup_view, name='name')
    entre => /pode colocar qualquer variável para encontrar o resultado, como str, int, slug/
]

## HANDLE DoesNotExist
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import nameModel

def dynamic_lookup_view(request, my_id):
    #obj = Product.object.get(id=my_id)
    #obj = get_object_or_404(nameModel, id=my_id)
    try:
        obj = Product.object.get(id=my_id)
    except nameModel.DoesNotExist:
        raise Http404
    context = {
        'object': obj
    }
    return render(request, "name.html", context)


## DELETE AND CONFIRM
from django.shortcuts import render, get_object_or_404, redirect
from .models import nameModel

def nameApp_delete_view(request,id):
    obj = get_object_or_404(nameModel, id=id)
    #POST request para confirmar o deletar => fazer um forms que retorna isso
    if request.method == "POST":
        obj.delete()
        return redirect('../')
    context = {
        "object": obj
    }
    
    return render(request, "delete.html", context)

#### no html que vai deletar o dado
<form action="." method="POST"> {% csrf_token %}
    <input type="submit" value="Yes" />
    <a href="../">Cancel </a>


## VIEW OF A LIST OF DATABASE OBJECT
#### views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import nameModel


def product_list_view(request):
    queryset = nameModel.object.all() # list of object
    context = {
        'object_list': queryset
    }
    return render(request, "name.html", context)

#### html
{% for instance in object_list %}
    {{instance.titles}}
{% endfor %}

## DYNAMIC LINKING OF URLs
#### .html file
{% for instance in object %}
    <p>{{ instance.id }} - <a href='/product/{{ instance.id }}'>{{ instance.title }}</a></p>
{% endfor %}
### PRECISA DOS URLS DINÂMICOS (código abaixo é uma base)
#### no views.html
from django.shortcuts import render
from .models import nameModel

def dynamic_lookup_view(request, my_id):
    return render(request, "name.html", context)

#### urls.py (importando o dynamic_lookup_view)
urlpatterns = [
=>> path('namePge/<int:my_id>/',dynamic_lookup_view, name='name')
    entre => /pode colocar qualquer variável para encontrar o resultado, como str, int, slug/
]


# IMPORTANTES
- python manage.py migrate => toda vez que atualizar qualquer coisa no APP, migrar para o ambiente de produção
- python manage.py makemigrations
- python manage.py createsuperuser => criar um "admin" (dever ser realizado toda vez que acontece é deletado o db)

