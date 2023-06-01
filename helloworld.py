from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, supports_credentials=True)


# 模拟用户身份验证
def authenticate_user(username, password):
  # 在这里进行实际的用户身份验证逻辑
  if username == "admin" and password == "password":
    return True
  return False


@app.route('/login', methods=['POST'])
@cross_origin(supports_credentials=True)
def login():
  username = request.form.get('username')
  password = request.form.get('password')
  t1 = request.form.get('unionId')
  t2 = request.form.get('uidtok')
  print(t1, t2)
  if authenticate_user(username, password):
    # 在这里创建和返回用户的身份验证令牌
    token = "example_token"
    print(token)
    return jsonify({'token': token})
  else:
    print('身份验证失败')
    return jsonify({'error': '身份验证失败'}), 401


@app.route('/restricted', methods=['GET'])
@cross_origin(supports_credentials=True)
def restricted():
  # 验证请求中的身份验证令牌
  token = request.headers.get('Authorization')

  # 在这里进行身份验证令牌的验证逻辑
  if token == "example_token":
    # 只有验证通过的用户才能访问受限资源
    print('访问受限资源成功')
    return jsonify({'message': '你是尊贵的vip用户'})
  else:
    print('无权访问')
    return jsonify({'error': '无权访问'}), 403


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
