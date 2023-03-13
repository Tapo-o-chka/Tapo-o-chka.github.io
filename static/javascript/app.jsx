const downloadedFunctions = {};
    
function loadJSXFunction(functionId) {
    const jsxContainer = document.getElementById('jsx-container');
    if (downloadedFunctions[functionId]) {
        jsxContainer.innerHTML = downloadedFunctions[functionId];
    } else {
        const xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (this.readyState === 4 && this.status === 200) {
                const jsxFunction = this.response.jsx_function;
                downloadedFunctions[functionId] = jsxFunction;
                jsxContainer.innerHTML = jsxFunction;
            }
        };
        xhr.open('GET', '/get_jsx_function/' + functionId);
        xhr.responseType = 'json';
        xhr.send();
    }
}