from flask import Blueprint, render_template, current_app, request, redirect, url_for, flash
from flask_login import login_required, current_user
from flask_paginate import Pagination, get_page_parameter
#from markupsafe import Markup
from models import Animal
from forms import InventorySearchForm, AnimalEditForm
from database import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

main = Blueprint('main', __name__)

# Root sends authenticated users to inventory page
# and unauthenticated to login page
@main.route('/')
def index():
    # Authenticated users go to main inventory page
    if current_user.is_authenticated:
        return redirect(url_for('main.inventory_list'))
    # Unauthenticated are taken to login page
    return redirect(url_for('auth.login'))


# Add a new animal to inventory
# Returns new ID through flash message
@main.route('/intake', methods=['GET', 'POST'])
@login_required
def intake():
    form = AnimalEditForm()
    if form.validate_on_submit():
        reserved_value = form.reserved.data == '1'  # Convert to boolean
        new_animal = Animal(
            name=form.name.data,
            animal=form.animal.data,
            breed=form.breed.data,
            gender=form.gender.data,
            age=form.age.data,
            weight=form.weight.data,
            height=form.height.data,
            body_length=form.body_length.data,
            tail_length=form.tail_length.data,
            training_status=form.training_status.data,
            acquisition_date=form.acquisition_date.data,
            acquisition_country=form.acquisition_country.data,
            in_service_country=form.in_service_country.data,
            reserved=reserved_value  # Use the converted value from above
        )
        # Catch database errors
        try:
            db.session.add(new_animal)
            db.session.commit()
            flash(f'New animal has been added with ID {new_animal.id}!', 'success')
            return redirect(url_for('main.inventory_list'))
        except SQLAlchemyError as e:
            db.session.rollback()  # Rollback the session to revert changes
            flash(f'An error occurred while adding the animal: {str(e)}', 'danger')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
    return render_template('intake.html', form=form)


# Apply search filters to query
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


# Show the main inventory list (Home page)
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
    
    # Pagination information to generate page numbers
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 6
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    items = pagination.items
    pagination_info = Pagination(page=page, total=pagination.total, per_page=per_page, record_name='items', css_framework='bulma')

    return render_template('inventory_list.html', items=items, pagination=pagination_info, form=form, filters=filters)


# Display and process edit form for individual animal
# Accepts page number argument to return user to
# the inventory page they came from.
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
            # Catch database errors
            try:
                form.populate_obj(item)
                # Convert reserved value to boolean
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


# Delete a single animal. ID passed from edit page.
# Accepts page number to return user to inventory page they came from
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
