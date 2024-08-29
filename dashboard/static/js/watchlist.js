function updateRemoveEventListeners() {

    // Select all elements with the class name 'watchlist-add-button'
    let watchlistButtons = document.querySelectorAll('.watchlist-remove-button');
    // Loop through each element and add an event listener
    watchlistButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Get the data-symbol attribute
            let symbol = this.getAttribute('data-symbol');
            // Call the addToWatchlist function with the symbol as the parameter
            removeFromWatchlist(symbol);
        });
    });
}

function createWatchList(items) {
    const ul = document.createElement('ul');
    items.forEach((item) => {
        const li = document.createElement('li');
        li.innerHTML = `${item}<span  type="button" class="watchlist-remove-button" data-symbol=${item}>-</span>`;;
        ul.appendChild(li);
    })
    return ul;
}

function refreshWatchlist() {
    fetch(`${API_BASE_URL}/watchlist/get`).then((response) => {
	if(response.ok) {
	    data = response.json().then((value) => {
		const list = createWatchList(value.data);
		let watchlistNode = document.getElementById('watchlist');
		watchlistNode.innerHTML = "";
		watchlistNode.appendChild(list);
                updateRemoveEventListeners();
	    }).catch((error) => console.log(error));
	} else {
	    console.log("responsse code not OK", response.status);
	}
    }).catch((error) => {
	console.log(error);
    })
}

function addToWatchlist(symbol) {
    fetch(`${API_BASE_URL}/watchlist/add/${symbol}`).then((response) => {
    	if(response.ok) {
	    refreshWatchlist();
	} else {
	    console.log("response code not OK", response.status);
	}
    }).catch((error) => {
	console.log(error);
    })
}

function removeFromWatchlist(symbol) {
    fetch(`${API_BASE_URL}/watchlist/remove/${symbol}`).then((response) => {
    	if(response.ok) {
	    refreshWatchlist();
	} else {
	    console.log("response code not OK", response.status);
	}
    }).catch((error) => {
	console.log(error);
    })
}

function clearWatchlist() {
    fetch(`${API_BASE_URL}/watchlist/clear`).then((response) => {
    	if(response.ok) {
	    refreshWatchlist();
	} else {
	    console.log("response code not OK", response.status);
	}
    }).catch((error) => {
	console.log(error);
    })
}

setTimeout(refreshWatchlist, 1000);
setTimeout(updateRemoveEventListeners, 3000);
