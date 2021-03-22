from flask import jsonify


def resp_success(data=None):
    resp = {
        "code": 0,
        "message": "success"
    }
    if data is not None:
        resp['data'] = data

    return jsonify(resp)


def resp_paginate(paginate_result, model_schema):
    return resp_success({
        "page": paginate_result.page,
        "list": model_schema.dump(paginate_result.items),
        "per_page": paginate_result.per_page,
        "total": paginate_result.total
    })


def resp_fail(message="request failed", data=None):
    resp = {
        "code": -1,
        "message": message,
    }
    if data is not None:
        resp['data'] = data

    return jsonify(resp)


def resp_access_denied(message="access permission denied"):
    resp = {
        "code": -2,
        "message": message,
    }
    return jsonify(resp)
