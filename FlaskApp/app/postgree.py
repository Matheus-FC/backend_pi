from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
#Caminho do banco tro car sendo user:password, do jeito q está funciona default, banco user_api tem que estar criado
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/user_api"]
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def hello():
    return{"hello": "world"}
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

#Modelo pro banco

class Usuario(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __repr__(self):
        return f"User {self.name}>"

#CRUD
@app.route('/users', methods=['POST', 'GET'])
def handle_users():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_user = Usuario(name=data['name'], email=data['email'])
            db.session.add(new_user)
            db.session.commit()
            return{"message": f"usario {new_user.name} criado com sucesso."}
        else:
            return {"error": "Dados enviados não estão em formato JSON"}
    elif request.methods == 'GET':
        users = Usuario.query.all()
        results = [
            {
                "name": user.name,
                "email": user.email
            } for user in users]
        return {"count": len(results), "users": results}

@app.route('users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_users(user_id):
    user = Usuario.query.get_or_404(user_id)

    if request.method == 'GET':
        response = {
            "name": user.name,
            "email": user.email
        }
        return{"message": "sucess", "user": response}
    
    elif request.method == 'PUT':
        data = request.get_json()
        user.name = data['name']
        user.email = data['email']
        db.session.add(user)
        db.session.commit()
        return{"message": f"user {user.name} atualizado com sucesso"}
    elif request.method == 'DELETE':
        db.session delete(user)
        db.session.commit()
        return {"message": f"User {user.name} deletado com sucesso"}
