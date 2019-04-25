from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets import HiddenInput

from application import app
from application.auth.models import User


class IdField(IntegerField):
    widget = HiddenInput()


class ModelForm(FlaskForm):
    id = IdField(None, [DataRequired()])

    def validate_id(form, field=None):
        app.logger.info("validating id")
        row = form.db_model.from_cache(form.id.data)
        if row is None:
            return ValidationError("Invalid identifier for %s" % form.db_model.__table__.name)
        if row.account_id is not current_user.id:
            return ValidationError("Unauthorized access")
        return True

    def validate_id_fields(form):
        if form.id and form.id.data:
            return form.validate_id()
        return True

    class Meta:
        @staticmethod
        def bind_field(form, unbound_field, options):
            filters = unbound_field.kwargs.get('filters', [])
            if strip_filter not in filters:
                filters.append(strip_filter)
            return unbound_field.bind(form=form, filters=filters, **options)
        csrf = False


def strip_filter(value):
    if value is not None and hasattr(value, 'strip'):
        return value.strip()
    return value
