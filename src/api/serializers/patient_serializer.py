from marshmallow import Schema, fields, validate

class PatientSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    age = fields.Int(required=True, validate=validate.Range(min=0))
    gender = fields.Str(required=True, validate=validate.OneOf(["male", "female", "other"]))
    medical_history = fields.List(fields.Str(), required=False)

    class Meta:
        ordered = True  # Maintain the order of fields
