var stocks = [
    {"symbol": "NVDA", "name": "NVIDIA", "close": "100", "currency": "USD", "lowest": "90", "highest": "110"},
    {"symbol": "MSFT", "name": "Microsoft", "close": "200", "currency": "USD", "lowest": "190", "highest": "210"},
    {"symbol": "AAPL", "name": "Apple", "close": "300", "currency": "USD", "lowest": "290", "highest": "310"},
    {"symbol": "GOOG", "name": "Google", "close": "400", "currency": "USD", "lowest": "390", "highest": "410"},
    {"symbol": "AMZN", "name": "Amazon", "close": "500", "currency": "USD", "lowest":"490", "highest": "510"}
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


// function mergeObjects(object1, object2) {
//     const result = {...object1, ...object2};
//     console.log("Merged array: ", result);
// }


function mergeListOfObjects(list1, list2) {
    const mergedList = list1.map(obj1 => {
        const obj2 = list2.find(obj => obj.symbol === obj1.symbol);
        return obj2 ? {...obj1, ...obj2} : obj1;
    });
    // console.log("Merged list: ", mergedList);
    
    return mergedList;
}


async function displayMessage(apiCall) {
    try {
        const response = await fetch(apiCall);
        if (!response.ok) throw new Error("API call failed");
        
        const data = await response.json();
        // document.querySelector("#napi-message").textContent = data.text;
        document.getElementById("api-message").textContent = data.text;
    } catch (error) {
        console.error("Error fetching message:", error);
    }
}


// ===================== Single API call =====================
// async function fetchAndDisplayTable(apiCall, containerId) {
//     try {
//         const response = await fetch(apiCall);
//         if (!response.ok) throw new Error("API call failed");
        
//         const data = await response.json();
//         drawTable(data, containerId);
//     } catch (error) {
//         console.error("Error:", error);
//     }
// }


// ====================== Two API calls ======================
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// FIX DATA MERGE!

async function fetchAndDisplayTable(apiCall1, apiCall2, containerId) {
    try {
        const response1 = await fetch(apiCall1);
        // Due to API call limits, we can only make one call every 60 seconds, so we need to wait before making the second call
        console.log("60 sec pause before second set of API calls...");
        await sleep(60000);
        console.log("60 sec pause ended");
        const response2 = await fetch(apiCall2);
        if (!response1.ok || !response2.ok) throw new Error("API call failed");

        const data1 = await response1.json();
        const data2 = await response2.json();
        const merged = mergeListOfObjects(data1, data2)
        console.log("Merged array: ", merged);
        drawTable(merged, containerId);

    } catch (error) {
        console.error("Error:", error);
    }
}


function drawTable(tableData, containerId) {
    const container = document.getElementById(containerId);
    document.getElementById(containerId).textContent = ""; // Clear previous HTML content
    const table = document.createElement("table");
    const headerRow = table.insertRow();
    const headers = ["Symbol", "Name", "Current Price", "Currency", "Lowest Price", "Highest Price"];
    
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
        // Limit the price to 2 decimal places
        tdPrice.innerText = parseFloat(parseFloat(row["close"]).toFixed(2));
        const tdCurrency = tr.insertCell();
        tdCurrency.innerText = row["currency"];
        const tdLowest = tr.insertCell();
        tdLowest.innerText = row["lowest"];
        const tdHighest = tr.insertCell();
        tdHighest.innerText = row["highest"];
    });
    
    container.appendChild(table);
}


// Run the code
displayMessage("/api/message");
drawTable(stocks, "table-js-static");
fetchAndDisplayTable("/api/stocks?stock=top8", "/api/stocks?stock=top8extended", "table-js-api");
// mergeObjects(obj1, obj2);
// mergeListOfObjects(stocks2base, stocks2ext);