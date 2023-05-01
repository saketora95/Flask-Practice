function sayHello() {
    alert('Hello, World!');
}

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