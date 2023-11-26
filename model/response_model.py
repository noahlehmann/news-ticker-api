from flask import current_app, jsonify, Response

from model.serializable import Serializable


class ResponseModel(Serializable):

    def __init__(self, response):
        self._response = response

    @property
    def response(self):
        return self._response

    def to_dict(self):
        return {
            "apiVersion": current_app.config["API_VERSION"],
            "response": self.response
        }

    def build(self) -> Response:
        return jsonify(self)
