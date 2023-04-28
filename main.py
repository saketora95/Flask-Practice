from flask import Flask, render_template

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