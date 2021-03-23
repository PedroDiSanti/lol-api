import json
from bottle import HTTPResponse
from app.utils.constants import HEADERS_RESPONSE


class ReturnMessages:
    @classmethod
    def error_payload(cls):
        return HTTPResponse(json.dumps({"Error": "Invalid Payload."}), 422, HEADERS_RESPONSE)

    @classmethod
    def error_get_response(cls):
        raise HTTPResponse(json.dumps({"Error": "There was no response."}), 404, HEADERS_RESPONSE)

    @classmethod
    def error_field(cls, error_validate_schema):
        return HTTPResponse(json.dumps({"Error": error_validate_schema.args}), 422, HEADERS_RESPONSE)
