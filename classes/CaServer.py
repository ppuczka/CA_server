from flask_restful import Resource


class CaServer(Resource):

    def get(self):
        return {'message' : 'this is ca server message'}

