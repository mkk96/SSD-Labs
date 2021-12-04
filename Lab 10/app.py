from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


class Student(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(80), nullable=False)
    stream = db.Column(db.String(80), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(int(user_id))


class Create(Resource):
    def post(self):
        posted_data = request.get_json()
        id = posted_data['id']
        name = posted_data['name']
        stream = posted_data['stream']
        check = Student.query.filter_by(id=id).first()
        if check is not None:

            return "id already exists."

        else:
            obj = Student(id=id, name=name, stream=stream)
            db.session.add(obj)
            db.session.commit()

            return "added successfully."


class Read(Resource):
    def get(self):
        data = Student.query.all()
        retMap = {}
        if len(data) == 0:
            return "No Entries have been added yet"
        for student in data:
            retMap[str(student.id)] = {
                "name": student.name, "stream": student.stream}
        return jsonify(retMap)


class Update(Resource):
    def put(self):
        posted_data = request.get_json()
        id = posted_data['id']
        name = posted_data['name']
        stream = posted_data['stream']

        # check if id already exist
        check = Student.query.filter_by(id=id).first()
        if check is not None:
            check.name = name
            check.stream = stream
            db.session.flush()
            db.session.commit()
            return 'Update Success'
        else:
            return 'id not found'


class Delete(Resource):
    def delete(self, id):
        check = Student.query.filter_by(id=id).first()
        if check is not None:
            db.session.delete(check)
            db.session.flush()
            db.session.commit()
            return 'Delete Success'
        else:
            return 'id not found'


api.add_resource(Create, '/create')
api.add_resource(Read, '/read')
api.add_resource(Update, '/update')
api.add_resource(Delete, '/delete/<id>')

if __name__ == '__main__':
    db.create_all()
    app.run(port=8000, debug=True)