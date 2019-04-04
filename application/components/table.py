from flask_login import current_user

from application import app, db
from flask import render_template, request, Response, abort


def render_table(rows, headers, table_type, anchors=False):
    return render_template("components/table.html", rows=rows, headers=headers, table_type=table_type, anchors=anchors)


def delete_row(row_id, db_model):
    row = get_row(row_id, db_model)
    db.session().delete(row)
    db.session().commit()
    return Response("", status=200, mimetype='text/plain')


def render_row(row_id, db_model, anchors=False):
    row = get_row(row_id, db_model)
    return render_template("components/row.html", row=row, anchors=anchors)


def render_input_row(row_id, db_model, form_class, anchors=False):
    row = get_row(row_id, db_model)
    if request.method == "GET":
        return render_template("components/input-row.html", id=row.id, form=form_class(obj=row))
    form = form_class(request.form)
    if not form.validate():
        return render_template("components/input-row.html", form=form), 422
    form.populate_obj(row)
    db.session().add(row)
    db.session().commit()
    return render_template("components/row.html", row=row, anchors=anchors)


def render_new_input_row(db_model, form_class, anchors=False):
    if request.method == "GET":
        return render_template("components/input-row.html", form=form_class(), row_id="")
    form = form_class(request.form)
    if not form.validate():
        return render_template("components/input-row.html", form=form), 422
    row = db_model()
    form.populate_obj(row)
    row.account_id = current_user.id
    db.session().add(row)
    db.session().commit()
    return render_template("components/row.html", row=row, anchors=anchors)


def get_row(row_id, db_model):
    row = db_model.query.get(row_id)
    if row is None:
        abort(404)
    if row.account_id is not current_user.id:
        abort(401)
    return row
