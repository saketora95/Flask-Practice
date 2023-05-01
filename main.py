from flask import Flask, render_template, request, redirect, url_for, jsonify, json

# 定位目前載入資料夾的位置
app = Flask(__name__)

# 使 Flask 監聽 URL 並 return 結果
@app.route('/')
def hello():
    return 'Hello, World!'

# ---- ---- ---- ---- ----
# Routing
# ---- ---- ---- ---- ----

@app.route('/get/accData/<acc_id>', methods=['GET'])
def getAccData(acc_id):
    print('Execute getAccData({})'.format(acc_id))
    return 'Acc ID is {}'.format(acc_id)

@app.route('/plus/one/<int:input_value>', methods=['GET'])
def plusOne(input_value):
    print('Execute plusOne({})'.format(input_value))
    print('- input_value\'s type is {}'.format(type(input_value)))
    return 'Plus one\'s result is {}'.format(input_value + 1)

# ---- ---- ---- ---- ----
# Render
# ---- ---- ---- ---- ----

@app.route('/basicHTML')
def basicHTML():
    return '<html><body><h1>Hello World</h1></body></html>'

@app.route('/home')
def home():
    return render_template('home.html')

# ---- ---- ---- ---- ----
# Jinja2
# ---- ---- ---- ---- ----

@app.route('/home/inlineInfo')
def homeInlineInfo():
    return render_template('home.html', title='Inline Info')

@app.route('/home/dictInfo')
def homeDictInfo():
    infoDetail = {
        'version': 'v1.0',
        'user_1': {
            'nickname': 'Hong',
            'age': 28,
            'hobby': 'Reading'
        },
        'user_2': {
            'nickname': 'Tora',
            'age': 30,
            'hobby': 'Cooking'
        },
    }
    return render_template('home.html', title='Inline Info', infoDetail=infoDetail)

# ---- ---- ---- ---- ----
# .js & .css
# ---- ---- ---- ---- ----

@app.route('/static')
def staticPage():
    return render_template('static.html')

# ---- ---- ---- ---- ----
# Form
# ---- ---- ---- ---- ----

# 監聽 URL
@app.route('/form')
def formPage():
    return render_template('form.html')

# 監聽並接收 POST 與 GET 方法
@app.route('/submit', methods=['POST', 'GET'])
def submit():

    # 判斷是否為 POST 方法
    if request.method == 'POST':

        # POST 方法中，取得輸入的參數要以 request.form 進行
        user = request.form['user']
        print('Execute submit (POST), user is {}'.format(user))

        # 透過 redirect 與 url_for 進行轉址到 success
        return redirect(url_for('success', name=user, action='POST'))

    # 不是 POST 方法，為 GET
    else:

        # GET 方法中，取得輸入的參數要以 request.args 進行
        user = request.args.get('user')
        print('Execute submit (GET), user is {}'.format(user))

        # 透過 redirect 與 url_for 進行轉址到 success
        return redirect(url_for('success', name=user, action='GET'))

# 接收轉址
@app.route('/success/<action>/<name>')
def success(name, action):
    return '{} : Welcome {} ~ !!!'.format(action, name)

# ---- ---- ---- ---- ----
# Ajax
# ---- ---- ---- ---- ----

# 連入時，回傳模版
@app.route('/data')
def webapi():
    return render_template('data.html')

# 讓網頁的 GET 按鈕會使用 GET 連入 /data/message
# 透過 GET 連入 /data/message 時，將 static/test_data.json 回傳
@app.route('/data/message', methods=['GET'])
def getDataMessage():
    if request.method == "GET":
        with open('static/test_data.json', 'r') as f:
            data = json.load(f)
        f.close
        return jsonify(data)

# 讓網頁的 POST 按鈕會使用 POST 連入 /data/message
# 透過 POST 連入 /data/message 時，將傳來的資料記錄到 static/input.json 中
@app.route('/data/message', methods=['POST'])
def setDataMessage():
    if request.method == "POST":
        # 取得傳入資料
        receive_data = request.get_json()

        # 將資料記錄到 static/input.json 中
        with open('static/input.json', 'w') as f:
            json.dump({
                'appInfo': {
                    'name': receive_data['app_name'],
                    'age': receive_data['app_age'],
                    'hobby': receive_data['app_hobby'],
                }
            }, f)
        f.close

        # 回傳結果
        return jsonify(result='OK')
