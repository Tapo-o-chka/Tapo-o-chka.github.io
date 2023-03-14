const downloadedFunctions = {};

function loadJSXFunction(functionId) {
  const templateContainer = document.getElementById('jsx-container');
  const cacheBuster = Math.random().toString(36).substring(7);
  const url = '/get_jsx_function/' + functionId + '?cache=' + cacheBuster; // Append cache-buster parameter to URL
  if (localStorage.getItem(functionId)) {
    templateContainer.innerHTML = localStorage.getItem(functionId);
    evalScripts(templateContainer);
  } else {
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (this.readyState === 4 && this.status === 200) {
        const templateHTML = this.responseText;
        localStorage.setItem(functionId, templateHTML);
        templateContainer.innerHTML = templateHTML;
        evalScripts(templateContainer);
      }
    };
    xhr.open('GET', url); // Use the modified URL with cache-buster parameter
    xhr.setRequestHeader('Content-type', 'text/html');
    xhr.send();
  }
}

function evalScripts(container) {
  const scripts = container.querySelectorAll('script');
  scripts.forEach(script => {
    const newScript = document.createElement('script');
    newScript.textContent = script.textContent;
    script.replaceWith(newScript);
  });
}
