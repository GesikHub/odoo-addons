from odoo import models, api
from ..utils import BaseValidator, ValidateFieldException


class FieldValidatorMixin(models.AbstractModel):
    """
    FieldValidatorMixin is a mixin class to use if you want to add validators to fields of model.
    You may add new attributes 'validators' to fields. You can use implemented validators in
    utils module or create custom validators.
    You have to inherit by BaseValidator class for create custom validator.
    """

    _name = "field.validator.mixin"

    @api.multi
    def _validate_fields(self, field_names):
        super(FieldValidatorMixin, self)._validate_fields(field_names)
        for field, value in field_names.items():
            field_validators = getattr(self._fields[field], "validators", [])
            for validator in field_validators:
                if isinstance(validator, BaseValidator):
                    if value:
                        try:
                            validator(value)
                        except ValidateFieldException as e:
                            raise models.ValidationError(
                                "Field {} is invalid. {}".format(
                                    self._fields[field].string,
                                    str(e),
                                )
                            )
