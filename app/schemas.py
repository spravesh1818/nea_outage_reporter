from app import marshmallow
from .models import User,Province,District,LocalBody
from marshmallow_sqlalchemy import ModelSchema

class UserSchema(ModelSchema):
    class Meta:
        model=User

class ProvinceSchema(ModelSchema):
    class Meta:
        model=Province

class DistrictSchema(ModelSchema):
    class Meta:
        model=District

class LocalBodySchema(ModelSchema):
    class Meta:
        model=LocalBody