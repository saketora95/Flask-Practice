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


# 參照資料
1. [Welcome to Flask — Flask Documentation (2.3.x)](https://flask.palletsprojects.com/en/2.3.x/)
2. [【Python Flask 入門指南】輕量級網頁框架教學 | 5 行程式碼 x 架設網站 - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天](https://ithelp.ithome.com.tw/articles/10258223) 以及後續相同主題之文章
3. [【Hello word】實作一個簡單的 Flask 入門 - Max行銷誌](https://www.maxlist.xyz/2020/04/30/flask-helloworld/)
4. [快速上手 — Flask中文文档(2.1.x)](https://dormousehole.readthedocs.io/en/latest/quickstart.html)

# 更新記錄
1. 2023-04-27 : 初步建立。
