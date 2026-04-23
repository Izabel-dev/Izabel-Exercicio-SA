from django.contrib import admin
from .models import Categoria, Produto, Pedido

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'estoque')
    list_filter = ('categoria',)
    search_fields = ('nome',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'quantidade', 'status', 'data_pedido')
    list_filter = ('status', 'data_pedido')
