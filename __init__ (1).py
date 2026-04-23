from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Produto, Categoria, Pedido
from .forms import ProdutoForm, CategoriaForm, PedidoForm

def home(request):
    return render(request, 'core/home.html')

def cadastro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('home')
        else:
            messages.error(request, "Erro ao realizar o cadastro. Verifique os dados.")
    else:
        form = UserCreationForm()
    return render(request, 'core/cadastro.html', {'form': form})

# Views protegidas por login_required

@login_required
def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'core/produto_list.html', {'produtos': produtos})

@login_required
def produto_create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto cadastrado com sucesso!")
            return redirect('produto_list')
    else:
        form = ProdutoForm()
    return render(request, 'core/produto_form.html', {'form': form, 'title': 'Cadastrar Produto'})

@login_required
def produto_update(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto atualizado com sucesso!")
            return redirect('produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'core/produto_form.html', {'form': form, 'title': 'Editar Produto'})

@login_required
def produto_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, "Produto excluído com sucesso!")
        return redirect('produto_list')
    return render(request, 'core/confirm_delete.html', {'object': produto, 'type': 'Produto'})

@login_required
def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'core/categoria_list.html', {'categorias': categorias})

@login_required
def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria criada com sucesso!")
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'core/categoria_form.html', {'form': form, 'title': 'Criar Categoria'})

@login_required
def pedido_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'core/pedido_list.html', {'pedidos': pedidos})

@login_required
def pedido_create(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pedido realizado com sucesso!")
            return redirect('pedido_list')
    else:
        form = PedidoForm()
    return render(request, 'core/pedido_form.html', {'form': form, 'title': 'Novo Pedido'})
