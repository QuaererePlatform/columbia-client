__all__ = ['CCDataResource', 'CCIndexesResource', 'CCScansResource']

from quaerere_base_client.resource import Resource
from columbia_common.schemas.api_v1 import (
    CCDataSchema, CCIndexesSchema, CCScansSchema)


class CCDataResource(Resource):
    resource_schema = CCDataSchema
    model_class = None


class CCIndexesResource(Resource):
    resource_schema = CCIndexesSchema
    model_class = None


class CCScansResource(Resource):
    resource_schema = CCScansSchema
    model_class = None
