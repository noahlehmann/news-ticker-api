from flask.json import JSONEncoder

from model.serializable import Serializable


class DictJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Serializable):
            return obj.to_dict()
        elif isinstance(obj, list) and all(isinstance(i, Serializable) for i in obj):
            return [i.to_dict() for i in obj]
        return super(DictJSONEncoder, self).default(obj)

