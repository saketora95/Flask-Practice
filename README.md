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
### 預設的執行檔案
`Flask` 有預設的執行檔案，沒有特別設置時會找尋目錄下的 `app.py` 或 `wsgi.py` 檔案，若不存在其中一者則會出現錯誤。

### 以參數執行
在[官方文件](https://flask.palletsprojects.com/en/2.3.x/quickstart/)（[參照資料 [1]](https://flask.palletsprojects.com/en/2.3.x/) 的 Quickstart）中，使用的方法是透過終端機輸入指令並附上參數執行：
```
flask --app [file name] run
```
假設建立的並不是 `app.py` 而是 `main.py` 的話，則是：
```
flask --app main run
```
透過這樣的指令執行時，Flask 就會找尋 `main.py` 而不會從預設的名稱下去找尋。

### 以環境設定執行
在「[參照資料 [3]](https://www.maxlist.xyz/2020/04/30/flask-helloworld/)」中有另一種方式可以指定執行的檔案，同樣假設要執行的檔案為 `main.py`，透過以下指令同樣可以執行：
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

### 在檔案內部設定 (不推薦)
還有一種方法是在 `main.py` 中進行設定：
```
if __name__ == '__main__':
    app.run()
```
在檔案中填入此段後，只要直接透過 `Python` 執行此檔案即可，雖然很便捷但[官方文件](https://flask.palletsprojects.com/en/1.1.x/server/#in-code)中有指出此方式具有一些問題：
> This works well for the common case but it does not work well for development which is why from Flask 0.11 onwards the flask method is recommended. The reason for this is that due to how the reload mechanism works there are some bizarre side-effects (like executing certain code twice, sometimes crashing without message or dying when a syntax or import error happens).

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
在這邊，嘗試建立一個網頁可以透過 Flask 接收資料並回傳；為此，需要以下項目：
- `main.py` : 處理監聽、回傳與接收資料的過程。
```
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
```
- `test_data.json` : 儲存一組固定的資料，供網頁 GET 時使用。
```
{
    "appInfo" : {
        "name" : "Hong" ,
        "age" : "28" ,
        "hobby" : "Reading"
    }
}
```
- `input.json` : 預設為空白的檔案，用於網頁 POST 資料到伺服器時填入。
```
就是空的檔案，在這邊有填寫什麼東西也無妨，最終都會因為 main.py 中的 setDataMessage 設置為覆蓋而被蓋過。
```
- `data.html` : 網頁頁面的回傳模版。
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ajax - Flask</title>

        <!-- 引入準備好的 script.js -->
        <script type = "text/javascript" src = "{{ url_for('static', filename = 'script.js') }}" ></script>
    </head>
    <body>
        <!-- GET : 使用者按下按鈕後會索取資料並將資料放入 POST 區域中的欄位 -->
        <h2>API : GET</h2>
        <button onclick="getTestData()">GET</button>

        <hr />

        <!-- POST : 使用者按下按鈕後會將欄位中的資料傳送給伺服器，並將結果顯示 -->
        <h2>API : POST</h2>
        <p>Name : <input id="app_name" name="app_name" type="text" /></p>
        <p>Age : <input id="app_age" name="app_age" type="text" /></p>
        <p>Hobby : <input id="app_hobby" name="app_hobby" type="text" /></p>
        <button onclick="postData()">POST</button>
        <p id="post_result"></p>

        <hr />

        <!-- Console : 使用者透過 GET 按鈕得到的資料會顯示於此 -->
        <h3>Console : </h3>
        <div id="console"></div>
    </body>
</html>
```
- `script.js` : 透過 JavaScript 處理網頁 GET 與 POST 的部分。
```
// GET 按鈕觸發
function getTestData() {
    // 向 /data/message 發送 GET
    fetch('/data/message', {method: 'GET'})
    // 將取得的資料轉為 Json
    .then(function(response) {
        return response.json();
    })
    // 將資料填入欄位與 console 中
    .then(function(data) {
        document.getElementById('app_name').value = data.appInfo.name;
        document.getElementById('app_age').value = data.appInfo.age;
        document.getElementById('app_hobby').value = data.appInfo.hobby;

        document.getElementById('console').innerText = JSON.stringify(data);
    });
}

// POST 按鈕觸發
function postData() {
    // 整理欄位中的輸入值
    let post_data = {
        'app_name': document.getElementById('app_name').value,
        'app_age': document.getElementById('app_age').value,
        'app_hobby': document.getElementById('app_hobby').value,
    };

    // 向 /data/message 發送 POST
    fetch('/data/message', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(post_data),
    })
    // 將取得的資料轉為 Json
    .then(function(response) {
        return response.json();
    })
    // 將結果填入 post_result 中
    .then(function(data) {
        document.getElementById('post_result').innerText = data['result'];
    });
}
```
上述完成後，在 `http://127.0.0.1:5000/data` 中的 GET 區域按下按鈕，POST 區域的三個欄位就會自動被取得的資料填入，Console 區域中也會記錄 GET 所取得的資料；而按下 POST 區域的按鈕時，會將區域內三個欄位的資料傳遞給伺服器，並記錄至 input.json 中。

# 其他設定
此部分會以前述「建立與執行 - 執行 - 以參數執行」提到的方式進行。

## 外部訪問
Flask 預設上不允許外部訪問，因此若無設定，執行後無法透過 `127.0.0.1` 與 `localhost` 之外的方式連入。透過在 `run` 之後添加參數 `--host=0.0.0.0` 可以開放外部的訪問：
```
flask --app main run --host=0.0.0.0
```
透過此行執行後，原先執行後出現的訊息 `* Running on http://127.0.0.1:5000` 一行會增多，表示連入的途徑增加了：
```
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://[你電腦目前的區域網路 IP]:5000
```

## Debug 模式
Flask 在執行時，即便任何檔案有所修改，都不會在當下生效，而必須要重新執行 Flask 才會有所變化，啟動 Debug 模式後，檔案如果有所修改，就會立刻自動 reload，減少開發時期中間開開關關的過程；使用上，同樣在 `run` 之後添加參數 ` --debug` 就可以啟動 Debug 模式：
```
flask --app main run --debug
```

# 參照資料
1. [Welcome to Flask — Flask Documentation (2.3.x)](https://flask.palletsprojects.com/en/2.3.x/)
2. [【Python Flask 入門指南】輕量級網頁框架教學 | 5 行程式碼 x 架設網站 - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天](https://ithelp.ithome.com.tw/articles/10258223)
3. [【Hello word】實作一個簡單的 Flask 入門 - Max行銷誌](https://www.maxlist.xyz/2020/04/30/flask-helloworld/)
4. [快速上手 — Flask中文文档(2.1.x)](https://dormousehole.readthedocs.io/en/latest/quickstart.html)
5. [How do I send a POST request using JavaScript?](https://reqbin.com/code/javascript/wzp2hxwh/javascript-post-request-example)
6. [jquery - how to get data from 'ImmutableMultiDict' in flask - Stack Overflow](https://stackoverflow.com/questions/29091070/how-to-get-data-from-immutablemultidict-in-flask)

# 更新記錄
1. 2023-04-27 : 初步建立。
    - 前言 : 五行程式碼
    - Python Flask - Hello World
2. 2023-04-28 : 向後學習。
    - 網頁模版 - Html 回傳
3. 2023-05-01 : 向後學習。
    - 資料交換 - Form 表單提交 與 Ajax 資料交換
4. 2023-05-02 : 補上缺少的參照資料與向後學習。
    - 開發配置 - 外網訪問與熱部署
5. 2023-05-02 17:00 結束。