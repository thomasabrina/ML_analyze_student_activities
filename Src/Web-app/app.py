from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import joblib
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 获取模型文件的路径
model_filename = 'forest_model_third.pkl'
classification_model_filename = 'classification_model.joblib'
model_path = os.path.join(script_dir, 'models', model_filename)
classification_model_path = os.path.join(script_dir, 'models', classification_model_filename)

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

    return jsonify('\n'.join(map(str, prediction.tolist())))  # 将预测结果返回到前端

@app.route('/classify', methods=['POST'])
def classify_route():
    file = request.files['file']  # 获取上传的文件
    print('Received file: ' + file.filename)  # 打印文件名

    data = pd.read_csv(file)  # 读取文件内容
    data = data[['attempts_sum', 'maxscore_sum', 'Score']]  # 只选择 'attempts_sum' 和 'maxscore_sum' 这两列
    print('Data: ' + str(data))  # 打印数据

    # 在这里加载模型
    classification_model = joblib.load(classification_model_path)

    clusters = classification_model.predict(data)  # 使用聚类模型进行分类
    print('Clusters: ' + str(clusters))  # 打印分类结果

    return jsonify('\n'.join(map(str, clusters.tolist())))  # 将分类结果返回到前端

if __name__ == '__main__':
    print("Starting Flask app")
    app.run(debug=True)