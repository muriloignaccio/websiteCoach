from django.shortcuts import render, redirect

# Importando do arquivo models dentro da pasta website todas as classes
from website.models import *

# Create your views here.

# Criando uma função que irá ser acionada quando for feita sua requisição.
def index(request):

    # Utilizando o if para verificar se o método da requisição é POST, que é do tipo que irá mandar dados para o banco de dados.
    if request.method == 'POST':

        # Foi criada uma váriavel com o nome de 'data' que irá abrigar a classe 'Coach' que está no arquivo 'models.py'
        data = Coach()

        # Aqui está utilizando a váriavel declarada acima para acessar o atributo nome e está atribuindo o valor que o request.POST['nome'] irá receber no input do HTML. Isso funciona da seguinte maneira, para a função ser acionada ela precisa de uma requisição, quando isso acontecer o .POST['nome'] vai procurar nela quem no HTML está como método de POST e possui o apelido 'nome'.
        data.nome = request.POST['nome']

        # Esse funciona da mesma forma que o anterior, só que ao invés dele procurar por 'nome', ele irá procurar quem no HTML está como método de POST e possui o apelido 'frase'.
        data.frase = request.POST['frase']

        # Funciona da mesma forma que o anterior, mas irá abrigar o valor de quem está como método de POST e possui o apelido de 'inspirador'
        data.inspirador = request.POST['inspirador']

        # Isso irá avisar o nosso banco de dados que as informações obtidas acima devem ser salvas nele.
        data.save()

        # Aqui foi criado um dicionário com uma entrada chamada 'sucesso' que abriga uma string que possui 'Parabéns!!' como valor.
        args = {
            'sucesso': 'Parabéns!!'
        }

        # Aqui irá retornar uma renderização através da requisição com a página do index e o dicionário criado acima.
        return render(request, 'index.html', args)

    # Caso não caia na verificação acima irá retornar uma renderização através da requisição com a página index.
    return render(request, 'index.html')

# Criando uma função que irá ser acionada quando for feita sua requisição.
def listar_coachs(request):

    # Criando um váriavel com o nome de 'lista_objetos' que irá abrigar todos os objetos da classe Coach que constam no banco de dados
    lista_objetos = Coach.objects.filter(ativo = True)

    # Criando um dicionário com uma entrada chamada 'listar_coachs' que abriga a váriavel lista_objetos
    args = {
        'listar_coachs': lista_objetos
    }

    # Irá retornar uma renderização através da requisição com a página listar_coachs e o dicionário criado acima
    return render(request, 'listar_coachs.html', args)

# Essa função para ser acionada, além de precisar de uma requisição, ela vai precisar de um id que é passado para ele durante o for que tem no 'listar_coachs.html'
def apagar_item(request, id):
    item_apagar = Coach.objects.get(id=id)
    item_apagar.ativo = False
    item_apagar.save()
    return redirect('/listar/coachs')
    # if item is not None:
    #     item.ativo = False
    #     item.save()
    #     return redirect('/coachs/listar')
    # return render (request, 'listar_coachs.html', {'msg': 'apagou'})