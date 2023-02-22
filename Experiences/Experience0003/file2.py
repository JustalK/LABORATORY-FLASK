from flask import Blueprint

file2_api = Blueprint('file2_api', __name__)

@file2_api.route('/test2', methods=['GET'])
def test():
    return 'File2'