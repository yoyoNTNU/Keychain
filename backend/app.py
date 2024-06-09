from flask import Flask

# 创建Flask应用程序实例
app = Flask(__name__)

# 配置应用程序
app.config.from_pyfile('config.py')

# 导入路由
from routes.auth import auth_routes
from routes.password import password_routes

# 注册路由
app.register_blueprint(auth_routes)
app.register_blueprint(password_routes)

# 运行应用程序
if __name__ == '__main__':
    app.run(debug=True)
