var stocks = [
    {"symbol": "NVDA", "name": "NVIDIA", "close": "100", "currency": "USD"},
    {"symbol": "MSFT", "name": "Microsoft", "close": "200", "currency": "USD"},
    {"symbol": "AAPL", "name": "Apple", "close": "300", "currency": "USD"},
    {"symbol": "GOOG", "name": "Google", "close": "400", "currency": "USD"},
    {"symbol": "AMZN", "name": "Amazon", "close": "500", "currency": "USD"}
  ]

// console.log("My stocks: ", stocks);

// fetch(url)
//   .then(response => response.json())  
//   .then(data => console.log(data))    
//   .catch(error => console.error(error))

// Async/await is just syntactic sugar for promises
// async function getText(file) {
//   let myObject = await fetch(file);
//   let myText = await myObject.text();
//   myDisplay(myText);
// }


async function displayMessage(apiCall) {
    try {
        const response = await fetch(apiCall);
        if (!response.ok) throw new Error("API call failed");
        
        const data = await response.json();
        document.querySelector("#name").textContent = data.text;
    } catch (error) {
        console.error("Error fetching message:", error);
    }
};


async function fetchAndDisplayTable(apiCall, containerId) {
    try {
        const response = await fetch(apiCall);
        if (!response.ok) throw new Error("API call failed");
        
        const data = await response.json();
        drawTable(data, containerId);
    } catch (error) {
        console.error("Error:", error);
    }
}


function drawTable(tableData, containerId) {
    // const container = document.querySelector(containerId);
    const container = document.getElementById(containerId);
    const table = document.createElement("table");
    const headerRow = table.insertRow();
    const headers = ["Symbol", "Name", "Price", "Currency"];
    
    headers.forEach(function(header) {
        const th = document.createElement("th");
        headerRow.appendChild(th);
        th.innerText = header;
    });

    tableData.forEach(function(row) {
        const tr = table.insertRow();
        const tdSymbol = tr.insertCell();
        tdSymbol.innerText = row["symbol"];
        const tdName = tr.insertCell();
        tdName.innerText = row["name"];
        const tdPrice = tr.insertCell();
        tdPrice.innerText = row["close"];
        const tdCurrency = tr.insertCell();
        tdCurrency.innerText = row["currency"];
    });
    
    container.appendChild(table);
}


// Run the code
displayMessage("/api/message");
fetchAndDisplayTable("/api/stocks?stock=top8", "table-js-api");
drawTable(stocks, "table-js-static");