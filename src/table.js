var array = [
    ['Car', 'Top Speed', 'Price'],
    ['Chevrolet', '120mph', '$10,000'],
    ['Pontiac', '140pmh', '$20,000'],
    ['BMW', '160mph', '$30,000']
  ]

var stocks = [
    {"symbol": "NVDA", "price": 500},
    {"symbol": "MSFT", "price": 300},
    {"symbol": "AAPL", "price": 200},
    {"symbol": "GOOG", "price": 1500}
  ]

console.log("Array of arrays: ", array);

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

// async function fetchData() {
//     try {
//         const response = await fetch(`/api/message`);
//         if (!response.ok) {
//             throw new Error("API call was not ok");
//         }
//         const data = await response.json();
//         console.log("API call was successful.");
//         console.log(data);
//     } catch (error) {
//         console.error("Error:", error);
//     }
// }

// fetchData();


async function fetchAndDisplayMessage() {
    const { text } = await( await fetch(`/api/message`)).json();
    document.querySelector('#name').textContent = text;
};

function drawTable(tableData) {
    var table = document.createElement("table");
    document.body.appendChild(table); // Drew the main table node on the document

    tableData.forEach(function(row) {
      var tr = table.insertRow(); //Create a new row

      row.forEach(function(column) {
        var td = tr.insertCell();
        td.innerText = column; // Take string from placeholder variable and append it to <tr> node
      });
    });
}


async function fetchAndDisplayTable(apiUrl, containerId) {
    try {
        const response = await fetch(apiUrl);
        if (!response.ok) throw new Error("API call failed");
        
        const data = await response.json();
        drawTableFromData(data, containerId);
    } catch (error) {
        console.error("Error:", error);
    }
}

function drawTableFromData(tableData, containerId) {
    const container = document.querySelector(containerId);
    const table = document.createElement("table");
    const headerRow = table.insertRow();
    const headers = ["Symbol", "Name", "Price", "Curency"];
    
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


fetchAndDisplayMessage();
// drawTable(array);

// Usage:
fetchAndDisplayTable("/api/stocks?stock=top8", "main");
// drawTableFromData(stocks, "main");