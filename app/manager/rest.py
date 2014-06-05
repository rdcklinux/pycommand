# -*- coding: utf-8 -*-

import flask

app = flask.Flask(__name__)

@app.route('/api/help', methods=['GET'])
def api_help():

    return flask.render_template('')


@app.errorhandler(405)
def method_not_allowed():

    return flask.jsonify({'message': 'Método no permitido', 'error': True})


@app.errorhandler(404)
def resource_not_found():

    return flask.jsonify({'message': 'Recurso no encontrado', 'error': True})


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
