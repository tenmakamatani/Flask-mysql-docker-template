from flask import make_response, jsonify

from flask_restful import Resource, reqparse

from models.Information import Information, InformationSchema

class InformationController(Resource):

    def get(self):
        results = Information.query.all()
        json_data = InformationSchema(many=True).dump(results)
        return jsonify({
            'informations': json_data
        })