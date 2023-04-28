# 概要
這是個人學習與練習 [Flask](https://flask.palletsprojects.com/en/2.3.x/) 所使用的 Repo；由於仍在初學階段，可能包含諸多錯誤或疏漏。
- 這個 README.md 兼當了我的學習筆記，因此非常得長。
- 如果有特定想搜尋的段落，請透過 `Ctrl + F` 或查看目錄會比較快；但我想直接到搜尋引擎找會更快更完整 xD

# 建立與執行
## 安裝
透過 `pip` 安裝，於終端機中輸入 `pip install flask`。

## 基礎語法
創建 `app.py` 檔案，並於其中填入以下段落：
```
from flask import Flask

# 定位目前載入資料夾的位置
app = Flask(__name__)

# 使 Flask 監聽 URL 並 return 結果
@app.route('/')
def hello():
    return 'Hello, World!'
```

## 執行
於終端機中輸入 `flask run` 執行，但 `Flask` 有預設的執行檔案，沒有特別設置時會找尋目錄下的 `app.py` 或 `wsgi.py` 檔案，若不存在其中一者則會出現錯誤。若要指定 `flask run` 所執行的檔案，可以於終端機中調整（以下假設要執行的檔案為 `main.py`）：
- Bash
```
$ export FLASK_APP=main
$ flask run
```
- Windows CMD
```
> set FLASK_APP=main
> flask run
```
- Windows Powershell
```
> $env:FLASK_APP = "main"
> flask run
```
就我個人的狀況，是使用 `Windows 10` 系統的電腦，並以 `VS Code` 進行練習，使用了 `Windows Powershell` 這一段。

順利執行後就會出現類似以下的訊息，此時連上 `http://127.0.0.1:5000` 就能看見一句 `Hello, World!` 了。
```
 * Serving Flask app 'main'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

# 撰寫技巧整理
## 路由
### 基礎運用
在 `建立與執行` 的 `基礎語法` 中提到使用 `@app.route('/')` 來監聽 URL，而此功能也能夠使 URL 成為參數：
```
# 使用 <> 包覆起來的部分會成為參數
@app.route('/get/accData/<acc_id>', methods=['GET'])
def getAccData(acc_id):
    print('Execute getAccData({})'.format(acc_id))
    return 'Acc ID is {}'.format(acc_id)
```
以上述為例，連上 `http://127.0.0.1:5000/get/accData/123` 時，就能看見網頁顯示 `Acc ID is 123`；並且也能指定字元的構成，例如調整為：
```
@app.route('/get/accData/abc<acc_id>', methods=['GET'])
```
連上 `http://127.0.0.1:5000/get/accData/abc123` 時，同樣就能看見網頁顯示 `Acc ID is 123`；但如果沒有按照設置以 `abc` 起頭，則會顯示 `Not Found`。

### 指定參數型態
在透過 `<>` 包覆成為變數時，能夠同時指定傳入的參數的型態，例如 `int` 或 `float`：
```
@app.route('/plus/one/<int:input_value>', methods=['GET'])
def plusOne(input_value):
    print('Execute plusOne({})'.format(input_value))
    print('- input_value\'s type is {}'.format(type(input_value)))
    return 'Plus one\'s result is {}'.format(input_value + 1)
```
連上 `http://127.0.0.1:5000/plus/one/10` 時，就能看見網頁顯示 `Plus one's result is 11`；但如果將 `<int:input_value>` 的 `int:` 移除，則 input_value 會被視為 `str` 而無法進行後續的加減。

## 網頁頁面
### 基礎回傳
前面就能看出回傳時會顯示到網頁上，而回傳的同時也可以包含一些 `html` 的語法：
```
@app.route('/basicHTML')
def basicHTML():
    return '<html><body><h1>Hello World</h1></body></html>'
```

### 回傳模版
簡單的 html 語法還能用上述的方式處理，但稍微複雜一些就不太妥當；透過 `render_template`，可以將 html 檔案回傳給使用者：
```
from flask import Flask, render_template

@app.route('/home')
def home():
    return render_template('home.html')
```
接著，`render_template` 會找尋目錄下的 `templates` 資料夾中的檔案，因此在目錄下建立 `templates` 資料夾，並放入上面用到的 `home.html`：
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Home - Flask</title>
    </head>
    <body>
        <h1>Home - Flask</h1>
        <h2>{{ title }}</h2>

        {% if infoDetail != undefined %}
            <h3>{{ infoDetail.version }}</h3>

            <table border="1">
                <tr>
                    <td>暱稱</td>
                    <td>年齡</td>
                    <td>喜好</td>
                </tr>
                <tr>
                    <td>{{ infoDetail.user_1.nickname }}</td>
                    <td>{{ infoDetail.user_1.age }}</td>
                    <td>{{ infoDetail.user_1.hobby }}</td>
                </tr>
                <tr>
                    <td>{{ infoDetail.user_2.nickname }}</td>
                    <td>{{ infoDetail.user_2.age }}</td>
                    <td>{{ infoDetail.user_2.hobby }}</td>
                </tr>
            </table>
        {% endif %}
    </body>
</html>
```
上述包含了很多 `{ ... }` 結構的語法，這是稍後會提到的 `Jinja2 模版引擎`，在這邊請先無視他。此時連上 `http://127.0.0.1:5000/home` 時，就會出現一個簡單的表格網頁了。

### Jinja2 模版引擎
透過 `Jinja2`，可以將 Python 階段的資料或變數運用到網頁之中，再回傳給使用者。

#### 語法
此處簡短地介紹語法，後續都有實際的段落使用到。

`{{ 變數名稱 }}` : 顯示變數

`{% if ... %} ... {% endif %}` : if 判斷式

`{% for ... %} ... {% endfor %}` : for 迴圈

#### 直接指定
最基礎的用法，是在 `render_template` 直接指定名稱與代入的資料：
```
@app.route('/home/inlineInfo')
def homeInlineInfo():
    return render_template('home.html', title='Inline Info')
```
此時連上 `http://127.0.0.1:5000/home/inlineInfo`，原先缺少資料而不會顯示的 `{{ title }}` 就會得到 `Inline Info` 這筆資料並加以顯示。

#### 使用 dict
當資料筆數比較多的時候，就可以使用 dict：
```
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
```
此時連上 `http://127.0.0.1:5000/home/dictInfo`，就會列出更多的資料。

#### 運用 for 迴圈
延續上述的例子，在 `home.html` 的 `{% if infoDetail != undefined %}` 的段落內再追加：
```
<table border="1">
    {% for key, value in infoDetail.items() %}
        {% if key != 'version' %}
            <tr>
                <th> {{ key }} </th>
                <td> {{ value.nickname }} </td>
                <td> {{ value.age }} </td>
                <td> {{ value.hobby }} </td>
            </tr>
        {% endif %}
    {% endfor %}
</table>
```
如此一來，網頁就會透過 for 迴圈把 infoDetail 中的資料顯示出來。

### 使用 .js 與 .css
前端工程開發出的 `.js` 與 `.css` 檔案需要放置於 `static` 資料夾下。在建立完 `static` 資料夾後，於該資料夾下再建立 `script.js`：
```
function sayHello() {
    alert('Hello, World!');
}
```
接著，在 `templates` 資料夾下建立 `static.html`：
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Static Page - Flask</title>
        <script type = "text/javascript" src = "{{ url_for('static', filename = 'script.js') }}" ></script>
        <!-- <script src="../static/script.js"></script> -->
    </head>
    <body>
        <h1>Static Page - Flask</h1>
        <button id="btnHello" onClick="sayHello()">Say Hello</button>
    </body>
</html>
```
最後於 `main.py` 加入：
```
@app.route('/static')
def staticPage():
    return render_template('static.html')
```
如此一來連入 `http://127.0.0.1:5000/static` 時，當中的按鈕就會連動到 `static/script.js` 中的 `sayHello()` 了。

### 表單 Form
首先，於 `templates` 資料夾下建立 `form.html`：
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Form - Flask</title>
    </head>
    <body>
        <h1>Form - Flask</h1>

        <hr />

        <h1>POST Form</h1>
        <form action="/submit" method="post">
            <h2>Enter Name:</h2>
            <p><input type="text" name="user" /></p>
            <p><input type="submit" value="submit" /></p>
        </form>

        <hr />

        <h2>GET Form</h2>
        <form action="/submit" method="get">
            <h2>Enter Name:</h2>
            <p><input type="text" name="user" /></p>
            <p><input type="submit" value="submit" /></p>
        </form>

    </body>
</html>
```
當中包含了常見的 `POST` 與 `GET` 方法。接著，回到 `main.py` 新增：
```
from flask import Flask, render_template, request, redirect, url_for

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
```
1. 使用者連入 `http://127.0.0.1:5000/form` 會經由 `formPage()` 看見 `form.html`
2. 操作 `form.html` 的兩個 form，會經由 `action="/submit"` 進入 `submit()`
3. 在 `submit()` 中進行處理，之後轉址到 `success()` 呈現出來

## Ajax


# 參照資料
1. [Welcome to Flask — Flask Documentation (2.3.x)](https://flask.palletsprojects.com/en/2.3.x/)
2. [【Python Flask 入門指南】輕量級網頁框架教學 | 5 行程式碼 x 架設網站 - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天](https://ithelp.ithome.com.tw/articles/10258223)
3. [【Hello word】實作一個簡單的 Flask 入門 - Max行銷誌](https://www.maxlist.xyz/2020/04/30/flask-helloworld/)
4. [快速上手 — Flask中文文档(2.1.x)](https://dormousehole.readthedocs.io/en/latest/quickstart.html)

# 更新記錄
1. 2023-04-27 : 初步建立。
2. 2023-04-28 : 向後學習。
