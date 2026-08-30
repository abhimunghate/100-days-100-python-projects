const HISTORY_KEY = "weatherSearchHistory";
const MAX_HISTORY = 10;

function getHistory() {
    const history = localStorage.getItem(HISTORY_KEY);
    if (!history) {
        return [];
    }

    try {
        return JSON.parse(history);
    } catch (error) {
        return [];
    }
}

function saveSearch(city) {
    if (!city || !city.trim()) {
        return;
    }

    city = city.trim();
    let history = getHistory();

    history = history.filter(item => item.toLowerCase() !== city.toLowerCase());
    history.unshift(city);

    history = history.slice(0, MAX_HISTORY);
    localStorage.setItem(HISTORY_KEY, JSON.stringify(history));
    displayHistory();
}

function displayHistory() {
    const historyList = document.getElementById("history-list");

    if (!historyList) {
        return;
    }

    const history = getHistory();
    historyList.innerHTML = "";

    if (history.length === 0) {
        const emptyMessage = document.createElement("p");
        emptyMessage.className = "empty-history";
        emptyMessage.textContent = "No recent searches.";
        historyList.appendChild(emptyMessage);
        return;
    }

    history.forEach(city => {
        const item = document.createElement("div");
        item.className = "history-item";
        item.textContent = `📍 ${city}`;

        item.addEventListener("click", () => {
                searchCity(city);
            }
        );
        historyList.appendChild(item);
    });
}

function searchCity(city) {
    const form = document.createElement("form");
    form.method = "POST";
    form.action = "/";

    const input = document.createElement("input");
    input.type = "hidden";
    input.name = "city";
    input.value = city;
    form.appendChild(input);
    document.body.appendChild(form);
    form.submit();
}

function clearHistory() {
    localStorage.removeItem(HISTORY_KEY);
    displayHistory();
}

document.addEventListener("DOMContentLoaded", () => {
        displayHistory();
        const clearButton = document.getElementById("clear-history");

        if (clearButton) {
            clearButton.addEventListener("click", clearHistory);
        }
    }
);

// Done