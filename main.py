from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

names = {"Ayesha": {"roll": 19017, "dept": "CSE"},
         "Fatema": {"roll": 20010, "dept": "CSE"}}

put_args = reqparse.RequestParser()
put_args.add_argument("name", type=str, help="Name is required", required=True)
put_args.add_argument("dept", type=str, help="Dept is required", required=True)
data = {}

def abort_if_no_id(s_id):
    if s_id not in data:
        abort(404, message = "Not found")
def abort_if_id_already_exists(s_id):
    if s_id in data:
        abort(409, message = "Already exist")

class apiTest1(Resource):
    def get(self):
        return {"data":"Hello"}

class apiTest2(Resource):
    def get(self, name):
        return names[name]

class apiTest3(Resource):
    def get(self, s_id):
        return data[s_id]

    def post(self, s_id):
        abort_if_id_already_exists(s_id)
        args=put_args.parse_args()
        data[s_id]=args
        return data[s_id], 201

    def put(self, s_id):
        abort_if_no_id(s_id)
        args=put_args.parse_args()
        data[s_id]=args
        return data[s_id], 201

    def delete(self, s_id):
        abort_if_no_id(s_id)
        del data[s_id]
        return '', 204

api.add_resource(apiTest1, "/api1")
api.add_resource(apiTest2, "/api2/<string:name>")
api.add_resource(apiTest3, "/api3/<int:s_id>")

if __name__ == "__main__":
    app.run(debug=True)
