from flask_login import current_user

from application import app, db
from flask import render_template, request, Response, abort


def render_table(**kwargs):
    return render_template("components/table.html", **kwargs)


def delete_row(row_id, db_model):
    row = get_row(row_id, db_model)
    db.session().delete(row)
    db.session().commit()
    return Response("", status=200, mimetype='text/plain')


def render_row(row_id, db_model, form_class, **kwargs):
    row = get_row(row_id, db_model)
    return render_template("components/row.html", row=row, form=form_class(), **kwargs)


def edit_row(row_id, db_model, form_class, **kwargs):
    if request.method == "GET":
        row = get_row(row_id, db_model)
        return render_template("components/input-row.html", id=row.id, form=form_class(obj=row))
    form = form_class(request.form)
    if not form.validate():
        return render_template("components/input-row.html", form=form), 422
    row = get_row(row_id, db_model)
    form.populate_obj(row)
    db.session().add(row)
    db.session().commit()
    return render_template("components/row.html", row=row, form=form_class(), **kwargs)


def new_row(db_model, form_class, **kwargs):
    if request.method == "GET":
        form = kwargs['initial_form'] if 'initial_form' in kwargs else form_class()
        return render_template("components/input-row.html", form=form, row_id="")
    form = form_class(request.form)
    if not form.validate():
        return render_template("components/input-row.html", form=form), 422
    row = db_model()
    form.populate_obj(row)
    if hasattr(db_model, 'account_id'):
            row.account_id = current_user.id
    db.session().add(row)
    db.session().commit()
    return render_template("components/row.html", row=row, form=form_class(), **kwargs)


def get_row(row_id, db_model):
    row = db_model.query.get(row_id)
    if row is None:
        abort(422)
    if row.account_id is not current_user.id:
        abort(401)
    return row
