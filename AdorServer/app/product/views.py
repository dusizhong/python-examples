# from flask import Blueprint, request, flash
from .. import db
from . import product
from .models import Product

@product.route('/products', methods=['GET'])
def product_list():
	print(Product.query.all())
	return 'product list'

@product.route('/products/<id>', methods=['GET'])
def product_detail(id):
	return 'product detail {}'.format(id)