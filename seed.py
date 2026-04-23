import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'izabellaestilo.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import Categoria, Produto, Pedido

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superusuário 'admin' criado com senha 'admin123'")

# Seed data
cat_feminina, _ = Categoria.objects.get_or_create(nome='Moda Feminina', descricao='Roupas e acessórios femininos')
cat_masculina, _ = Categoria.objects.get_or_create(nome='Moda Masculina', descricao='Roupas e acessórios masculinos')

p1, _ = Produto.objects.get_or_create(
    nome='Vestido Floral',
    categoria=cat_feminina,
    preco=159.90,
    estoque=10,
    descricao='Vestido leve para o verão'
)

p2, _ = Produto.objects.get_or_create(
    nome='Camisa Polo',
    categoria=cat_masculina,
    preco=89.00,
    estoque=25,
    descricao='Camisa polo 100% algodão'
)

Pedido.objects.get_or_create(produto=p1, quantidade=1, status='P')

print("Dados iniciais inseridos com sucesso!")
