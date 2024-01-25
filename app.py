from flask import Flask
from controllers.index_controller import index
from controllers.about_controller import about
from extensions import db

#
app = Flask(__name__, template_folder='views')

# Настройка подключения к базе данных MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Vintage38@localhost/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(index)
app.register_blueprint(about)

@app.errorhandler(500)
def internal_server_error(e):
    # Здесь вы можете залогировать ошибку или вернуть пользователю более информативное сообщение
    return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(debug=True)