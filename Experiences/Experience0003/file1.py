from flask import Blueprint

file1_api = Blueprint('file1_api', __name__)

@file1_api.route('/test1', methods=['GET'])
def test():
    return 'File1'