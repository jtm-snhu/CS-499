from flask import Blueprint, render_template, current_app, request, redirect, url_for, flash
from flask_login import login_required, current_user
from flask_paginate import Pagination, get_page_parameter
from markupsafe import Markup #Needed for paginate 


#from sqlalchemy_utils import database_exists, create_database

from models import Dog, Monkey, Animal
from database import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.inventory_list'))
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@main.route('/intake')
def intake():
    return render_template('intake.html')

@main.route('/reserve')
def reserve():
    return render_template('reserve.html')


#Animal Inventory Menu                          
#@main.route('/inventory')
#@login_required
#def inventory():
#    return render_template('inventory.html')

#Animal Inventory List
@main.route('/inventory')
@login_required
def inventory_list():
    query = Animal.query
    name = request.args.get('name', '')
    breed = request.args.get('breed', '')
    training_status = request.args.get('training_status', '')
    gender = request.args.get('gender', '')
    in_service_country = request.args.get('in_service_country', '')
    reserved = request.args.get('reserved', '')
    search_query = request.args.get('q', '')

    if name:
        query = query.filter(Animal.name.contains(name))
    if breed:
        query = query.filter(Animal.breed.contains(breed))
    if training_status:
        query = query.filter(Animal.training_status.contains(training_status))
    if gender:
        query = query.filter(Animal.gender == gender)
    if in_service_country:
        query = query.filter(Animal.in_service_country == in_service_country)
    if reserved:
        query = query.filter(Animal.reserved == (reserved == '1'))
    if search_query:
        query = query.filter(
            Animal.name.contains(search_query) |
            Animal.animal.contains(search_query) |
            Animal.in_service_country.contains(search_query) |
            Animal.training_status.contains(search_query) |
            Animal.breed.contains(search_query) |
            Animal.gender.contains(search_query)
        )

    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 6
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    items = pagination.items
    pagination_info = Pagination(page=page, total=pagination.total, per_page=per_page, record_name='items', css_framework='bulma')


    # Handle the ID parameter to ensure the correct page is displayed
#    item_id = request.args.get('id')
#    if item_id:
#        item = Animal.query.get(item_id)
#        if item:
#            item_page = (Animal.query.filter(Animal.id <= item_id).count() - 1) // per_page + 1
#            if item_page != page:
#                return redirect(url_for('main.inventory_list', page=item_page, id=item_id, message=request.args.get('message')))
  

    return render_template('inventory_list.html', items=items, pagination=pagination_info)



@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    item = Animal.query.get_or_404(id)
    if request.method == 'POST':
        item.animal = request.form['animal']
        item.name = request.form['name']
        item.gender = request.form['gender']
        item.age = request.form['age']
        item.weight = request.form['weight']
        item.acquisition_date = request.form['acquisition_date']
        item.acquisition_country = request.form['acquisition_country']
        item.training_status = request.form['training_status']
        item.reserved = 'reserved' in request.form
        item.in_service_country = request.form['in_service_country']
        item.breed = request.form['breed']
        item.height = request.form['height']
        item.tail_length = request.form['tail_length']
        item.body_length = request.form['body_length']

        db.session.commit()
        flash('Item updated successfully', 'success')
        return redirect(url_for('main.inventory_list', id=id))

    return render_template('edit.html', item=item)

@main.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    item = Animal.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted successfully', 'danger')
    return redirect(url_for('main.inventory_list'))


'''
#Dog Inventory List
@main.route('/inventory/dogs')
def dog_inventory_list():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 5
    pagination = Dog.query.paginate(page=page, per_page=per_page, error_out=False)
    items = pagination.items
    pagination_info = Pagination(page=page, total=pagination.total, per_page=per_page, record_name='items', css_framework='bulma')

    return render_template('inventory_list.html', items=items, pagination=pagination_info)

#Monkey Inventory List
@main.route('/inventory/monkeys')
def monkey_inventory_list():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 5
    pagination = Monkey.query.paginate(page=page, per_page=per_page, error_out=False)
    items = pagination.items
    pagination_info = Pagination(page=page, total=pagination.total, per_page=per_page, record_name='items', css_framework='bulma')

    return render_template('inventory_list.html', items=items, pagination=pagination_info)
'''