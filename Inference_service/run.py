" Model inference app from flask "


from app.api.prediction import bp

from flask import Flask 

app = Flask(__name__)

app.register_blueprint(bp)



    
if __name__ == '__main__':
    app.run(debug=True)
