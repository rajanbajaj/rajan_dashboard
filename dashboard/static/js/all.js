const API_BASE_URL = JSON.parse(document.getElementById('api-base-url').textContent);
let isAddEventSet = false;
function updateEventListeners() {
    if (isAddEventSet) {
        return
    }

    isAddEventSet = true;
	
    // Select all elements with the class name 'watchlist-add-button'
    let watchlistButtons = document.querySelectorAll('.watchlist-add-button');
    // Loop through each element and add an event listener
    watchlistButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Get the data-symbol attribute
            let symbol = this.getAttribute('data-symbol');
            // Call the addToWatchlist function with the symbol as the parameter
            addToWatchlist(symbol);
        });
    });
}
function createList(items) {
    const ul = document.createElement('ul');
    items.forEach((item) => {
        const li = document.createElement('li');
        li.innerHTML = `${item}<span type="button" class="watchlist-add-button" data-symbol=${item}>+</span>`;
        ul.appendChild(li);
    });
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

function loadBullishEngullfing() {
    try {
        fetch(`${API_BASE_URL}/bullish-engullfing`).then((response) => {
            response.json().then((value) => {
                const list = createList(value.data);
                document.getElementById('bullish-engullfing').innerHTML = '';
                document.getElementById('bullish-engullfing').appendChild(list);
            })
        });
    } catch {
        console.log("ERROR IN BULLISH ENGULLFING");
    }
}

function loadDoji() {
    try {
        fetch(`${API_BASE_URL}/doji`).then((response) => {
            response.json().then((value) => {
                const list = createList(value.data);
                document.getElementById('doji').innerHTML = '';
                document.getElementById('doji').appendChild(list);
            })
        });
    } catch {
        console.log("ERROR IN DOJI.");
    }
}

function loadFallingWedge() {
    try {
        fetch(`${API_BASE_URL}/falling-wedge`).then((response) => {
            response.json().then((value) => {
                const list = createList(value.data);
                document.getElementById('falling-wedge').innerHTML = '';
                document.getElementById('falling-wedge').appendChild(list);
            })
        });
    } catch {
        console.log("ERROR IN FALLING WEDGE.");
    }
}

function loadRisingWedge() {
    try {
        fetch(`${API_BASE_URL}/rising-wedge`).then((response) => {
            response.json().then((value) => {
                const list = createList(value.data);
                document.getElementById('rising-wedge').innerHTML = '';
                document.getElementById('rising-wedge').appendChild(list);
            })
        });
    } catch {
        console.log("ERROR IN RISING WEDGE.");
    }
}
function loadHammer() {
    try {
        fetch(`${API_BASE_URL}/hammer`).then((response) => {
            response.json().then((value) => {
                const list = createList(value.data);
                document.getElementById('hammer').innerHTML = '';
                document.getElementById('hammer').appendChild(list);
            })
        });
    } catch {
        console.log("ERROR IN HAMMER.");
    }
}

function loadNear52WeekHigh() {
    try {
        fetch(`${API_BASE_URL}/near-52week-high`).then((response) => {
            response.json().then((value) => {
                const list = createList(value.data);
                document.getElementById('near-52week-high').innerHTML = '';
                document.getElementById('near-52week-high').appendChild(list);
            })
        });
    } catch {
        console.log("ERROR IN NER 52 WEEKS HIGH.");
    }
}

function loadNear52WeekLow() {
    try {
        fetch(`${API_BASE_URL}/near-52week-low`).then((response) => {
            response.json().then((value) => {
                const list = createList(value.data);
                document.getElementById('near-52week-low').innerHTML = '';
                document.getElementById('near-52week-low').appendChild(list);
            })
        });
    } catch {
        console.log("ERROR IN NEAR 52 WEEKS LOW.");
    }
}



loadOIGainers()
loadOILosers()
loadBullishEngullfing()
loadDoji()
loadFallingWedge()
loadRisingWedge()
loadHammer()
loadNear52WeekHigh()
loadNear52WeekLow()
setInterval(loadOIGainers, 60000);
setInterval(loadOILosers, 60000);
setTimeout(updateEventListeners, 3000);
