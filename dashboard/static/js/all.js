const API_BASE_URL = JSON.parse(document.getElementById('api-base-url').textContent);

function createList(items) {
    const ul = document.createElement('ul');
    items.forEach((item) => {
        const li = document.createElement('li');
        li.textContent = item;
        ul.appendChild(li);
    })
    return ul;
}

function loadOIGainers() {
    try {
        fetch(`${API_BASE_URL}/oi-gainers`).then((response) => {
            response.json().then((value) => {
                const list = createList(value.data);
                document.getElementById('oi-gainers').innerHTML = '';
                document.getElementById('oi-gainers').appendChild(list);
            })
        });
    } catch {
        console.log("ERROR IN OI GAINSERS");
    }
}

function loadOILosers() {
    try {
        fetch(`${API_BASE_URL}/oi-losers`).then((response) => {
            response.json().then((value) => {
                const list = createList(value.data);
                document.getElementById('oi-losers').innerHTML = '';
                document.getElementById('oi-losers').appendChild(list);
            })
        });
    } catch {
        console.log("ERROR IN OI LOSERS.");
    }
}
loadOIGainers()
loadOILosers()
setInterval(loadOIGainers, 5000);
setInterval(loadOILosers, 5000);
