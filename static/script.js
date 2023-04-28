function sayHello() {
    alert('Hello, World!');
}

function getTestData() {
    fetch('/data/message')
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        let temp_text = '';
        temp_text += 'data.appInfo.name : ' + data.appInfo.name + ' || ';
        temp_text += 'data.appInfo.age : ' + data.appInfo.age + ' || ';
        temp_text += 'data.appInfo.hobby : ' + data.appInfo.hobby;
        document.getElementById('console').innerText = temp_text;

        document.getElementById('app_name').value = data.appInfo.name;
        document.getElementById('app_age').value = data.appInfo.age;
        document.getElementById('app_hobby').value = data.appInfo.hobby;
    });
}