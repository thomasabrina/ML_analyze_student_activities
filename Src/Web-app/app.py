from flask import Flask, render_template, request, jsonify
from model1 import predict1
from model2 import predict2

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict1', methods=['POST'])
def predict_route1():
    data = request.get_json()  # 获取前端发送的数据
    prediction = predict1(data)  # 使用模型进行预测
    return jsonify(prediction)  # 将预测结果返回到前端

@app.route('/predict2', methods=['POST'])
def predict_route2():
    data = request.get_json()  # 获取前端发送的数据
    prediction = predict2(data)  # 使用模型进行预测
    return jsonify(prediction)  # 将预测结果返回到前端

if __name__ == '__main__':
    app.run(debug=True)