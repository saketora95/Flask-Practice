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

@app.route('/data')
def webapi():
    return render_template('data.html')

@app.route('/data/message', methods=['GET'])
def getDataMessage():
    if request.method == "GET":
        with open('static/test_data.json', 'r') as f:
            data = json.load(f)
            print("text : ", data)
        f.close
        return jsonify(data)

@app.route('/data/message', methods=['POST'])
def setDataMessage():
    if request.method == "POST":
        data = {
            'appInfo': {
                'name': request.form['app_name'],
                'age': request.form['app_age'],
                'hobby': request.form['app_hobby'],
            }
        }
        print(type(data))
        with open('static/input.json', 'w') as f:
            json.dump(data, f)
        f.close
        return jsonify(result='OK')
