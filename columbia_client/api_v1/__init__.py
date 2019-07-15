__all__ = ['api']

from quaerere_base_client.api import API

from .resources import (CCDataResource, CCIndexesResource, CCScansResource)

api = API('v1')
api.add_resource(CCDataResource)
api.add_resource(CCIndexesResource)
api.add_resource(CCScansResource)
