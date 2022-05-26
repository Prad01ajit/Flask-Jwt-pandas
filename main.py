from app import create_app



app = create_app()
   
if __name__=='__main__':
   app.run(debug=True)





   

# app = Flask(__name__)

# app.config['SECRET_KEY']='3ad98aac227663c9d34af919553d58e4'
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:pradeep@localhost/flask_1'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


# db = SQLAlchemy(app)

# class Users(db.Model):
#     __tablename__ = 'user-account'
#     id = db.Column(db.Integer, primary_key=True)
#     public_id = db.Column(db.String(50))
#     name = db.Column(db.String(50))
#     password = db.Column(db.String(100))

# auth_blueprint = Blueprint('auth_blueprint', __name__)

# def token_required(f):
#    @wraps(f)
#    def decorator(*args, **kwargs):
#        from app import app
#        token = None
#        if 'x-access-tokens' in request.headers:
#            token = request.headers['x-access-tokens']
 
#        if not token:
#            return jsonify({'message': 'a valid token is missing'})
#        try:
#            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
#            current_user = Users.query.filter_by(public_id=data['public_id']).first()
#        except:
#            return jsonify({'message': 'token is invalid'})
 
#        return f(current_user, *args, **kwargs)
#    return decorator


# # Register a new user 
# @auth_blueprint.route('/register' , methods=['POST'])
# def auth():
#    data = request.get_json() 
#    hashed_password = generate_password_hash(data['password'], method='sha256')
 
#    new_user = Users(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password)
#    db.session.add(new_user) 
#    db.session.commit()   
#    return jsonify({'message': 'registered successfully'})


# # Login user
# @auth_blueprint.route('/login', methods=['POST']) 
# def login_user():
#    auth = request.authorization  
#    if not auth or not auth.username or not auth.password: 
#        return make_response('could not verify', 401, {'Authentication': 'login required"'})   
 
#    user = Users.query.filter_by(name=auth.username).first()  
#    if check_password_hash(user.password, auth.password):
#        token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, app.config['SECRET_KEY'], "HS256")
 
#        return jsonify({'token' : token})
 
#    return make_response('could not verify',  401, {'Authentication': '"login required"'})

# # Get all
# @auth_blueprint.route('/users', methods=['GET'])
# def get_all_users(): 
 
#    users = Users.query.all()
#    result = []  
#    for user in users:  
#        user_data = {}  
#        user_data['public_id'] = user.public_id 
#        user_data['name'] = user.name
#        user_data['password'] = user.password
#        user_data['admin'] = user.admin
     
#        result.append(user_data)  
#    return jsonify({'users': result})


#Top-3 cities
# aqi_blueprint = Blueprint('aqi_blueprint', __name__)

# @aqi_blueprint.route('/top-3',methods = ['GET'])
# @token_required
# def top_cities(self):
#      df = pd.read_csv("/home/pradeep/Downloads/AQIDay.csv",usecols=["City","AQI"])
#      _sortdesc = df.sort_values(["AQI"], ascending= False)
#      _slicedesc = _sortdesc[0:3]
#      return jsonify({"cities" : _slicedesc.City.to_string(index=False)})


# app.register_blueprint(auth_blueprint) 
# app.register_blueprint(aqi_blueprint)


   

