from functools import wraps
from flask import jsonify, request


def required_params(required):
    def decorator(fn):

        @wraps(fn)
        def wrapper(*args, **kwargs):
            _json = request.get_json()
            missing = [r + ' is required' for r in required.keys()
                       if r not in _json]

            if missing:
                response = {
                    "status": False,
                    "message": "Please, Enter required fields",
                    "missing": missing
                }
                return jsonify(response), 400
            wrong_types = [f'Enter {r} in valid format' for r in required.keys()
                           if not isinstance(_json[r], required[r])]
            print(wrong_types);
            if wrong_types:
                response = {
                    "status": False,
                    "message": "Please, Enter value in valid format type",
                    "param_types": wrong_types
                }
                return jsonify(response), 400
            return fn(*args, **kwargs)
        return wrapper
    return decorator
