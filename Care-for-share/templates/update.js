function readFile(file, out) {
    var http = new XMLHttpRequest();
    http.open('get', file);
    http.onreadystatechange = function () {
        out.innerHTML = http.responseText.replace(/\n/g, '<br>');
    };
    http.send();
}

readFile('file.txt', document.getElementById('text-file'));