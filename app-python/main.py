from flask import Blueprint, render_template, current_app, request, redirect, url_for, flash
from flask_login import login_required, current_user
from flask_paginate import Pagination, get_page_parameter
from markupsafe import Markup
from models import Dog, Monkey, Animal
from forms import InventorySearchForm, AnimalEditForm
from database import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Authenticated users go to main inventory page
    if current_user.is_authenticated:
        return redirect(url_for('main.inventory_list'))
    # Unauthenticated are taken to login page
    return redirect(url_for('auth.login'))

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



def apply_filters(query, filters):
    if filters.get('name'):
        query = query.filter(Animal.name.contains(filters['name']))
    if filters.get('breed'):
        query = query.filter(Animal.breed.contains(filters['breed']))
    if filters.get('training_status'):
        query = query.filter(Animal.training_status.contains(filters['training_status']))
    if filters.get('gender'):
        query = query.filter(Animal.gender == filters['gender'])
    if filters.get('in_service_country'):
        query = query.filter(Animal.in_service_country == filters['in_service_country'])
    if filters.get('reserved'):
        query = query.filter(Animal.reserved == (filters['reserved'] == '1'))
    return query

@main.route('/inventory', methods=['GET', 'POST'])
@login_required
def inventory_list():
    form = InventorySearchForm(request.args)
    query = Animal.query

    filters = {
        'name': form.name.data,
        'breed': form.breed.data,
        'gender': form.gender.data,
        'training_status': form.training_status.data,
        'in_service_country': form.in_service_country.data,
        'reserved': form.reserved.data
    }

    query = apply_filters(query, filters)
    
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 6
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    items = pagination.items
    pagination_info = Pagination(page=page, total=pagination.total, per_page=per_page, record_name='items', css_framework='bulma')

    return render_template('inventory_list.html', items=items, pagination=pagination_info, form=form, filters=filters)


@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    item = Animal.query.get_or_404(id)
    form = AnimalEditForm(obj=item)
    page = request.args.get('page', 1)

    if request.method == 'GET':
        form.reserved.data = '1' if item.reserved else '0'

    if form.validate_on_submit():
        if form.submit.data:
            try:
                form.populate_obj(item)
                item.reserved = form.reserved.data == '1'
                db.session.commit()
                flash('Item updated successfully', 'success')
            except IntegrityError as e:
                db.session.rollback()
                flash('An integrity error occurred: {}'.format(e.orig), 'danger')
            except SQLAlchemyError as e:
                db.session.rollback()
                flash('An error occurred while updating the item: {}'.format(e), 'danger')
            return redirect(url_for('main.inventory_list', page=page))
        elif form.delete.data:
            try:
                db.session.delete(item)
                db.session.commit()
                flash('Item deleted successfully', 'danger')
            except SQLAlchemyError as e:
                db.session.rollback()
                flash('An error occurred while deleting the item: {}'.format(e), 'danger')
            return redirect(url_for('main.inventory_list', page=page))

    return render_template('edit.html', form=form, item=item, page=page)


@main.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    page = request.args.get('page', 1)
    try:
        item = Animal.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        flash('Item deleted successfully', 'danger')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'Error deleting item: {str(e)}', 'danger')
    return redirect(url_for('main.inventory_list', page=page))

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