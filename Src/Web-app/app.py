from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# 获取模型文件的路径
model_path = os.path.join(os.getcwd(), 'models', 'forest_model_third.pkl')

# 加载模型
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    file = request.files['file']  # 获取上传的文件
    print('Received file: ' + file.filename)  # 打印文件名

    data = pd.read_csv(file)  # 读取文件内容
    print('Data: ' + str(data))  # 打印数据

    prediction = model.predict(data)  # 使用模型进行预测
    print('Prediction: ' + str(prediction))  # 打印预测结果

    return jsonify(prediction.tolist())  # 将预测结果返回到前端

if __name__ == '__main__':
    app.run(debug=True)