# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class ProductCategory(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name='Pai')
    name = models.CharField(max_length=255, verbose_name='Nome')
    active = models.BooleanField(default=True, verbose_name=u'Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado Em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Alterado Em')

    class Meta:
        verbose_name = 'Categoria de Produto'
        verbose_name_plural = 'Categorias de Produto'
        
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, verbose_name='Categoria')
    name = models.CharField(max_length=255, verbose_name='Nome')
    short_description = models.TextField(verbose_name='Breve Descrição')
    cost = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Custo')
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    image = models.ImageField(upload_to='uploads/products/')
    menu = models.BooleanField(default=True, verbose_name=u'Menu')
    active = models.BooleanField(default=True, verbose_name=u'Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado Em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Alterado Em')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        
    def __str__(self):
        return self.name.encode('utf-8')

class Inventory(models.Model):
    product = models.ForeignKey(Product, verbose_name='Produto')
    quantity = models.SmallIntegerField(verbose_name='Quantidade')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado Em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Alterado Em')

    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoques'
        
class Table(models.Model):
    uid = models.CharField(max_length=255, verbose_name='Identificador')
    active = models.BooleanField(default=True, verbose_name=u'Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado Em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Alterado Em')
    
    class Meta:
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'
    
    def __str__(self):
        return self.uid.encode('utf-8')
        
class Order(models.Model):
    PAYMENT_CHOICES = (
        ("cash", "Dinheiro"),
        ("debit", "Débito"),
        ("credit", "Crébito"),
    )
    
    table = models.ForeignKey(Table, verbose_name='Mesa')
    obs = models.TextField(blank=True, null=True, verbose_name='Observação')
    payment = models.CharField(max_length=50, choices=PAYMENT_CHOICES, blank=True, null=True, verbose_name='Pagamento')
    finished = models.BooleanField(default=False, verbose_name=u'Finalizado')
    active = models.BooleanField(default=True, verbose_name=u'Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado Em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Alterado Em')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        
    def __str__(self):
        return '#' + str(self.id) + ': ' + self.table.uid
        
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, verbose_name='Pedido')
    product = models.ForeignKey(Product, related_name='products', verbose_name='Produto')
    quantity = models.IntegerField(verbose_name='Quantidade')
    served = models.BooleanField(default=False, verbose_name=u'Atendido?')
    
    class Meta:
        verbose_name = 'Produto de Pedido'
        verbose_name_plural = 'Produtos de Pedido'