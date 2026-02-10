var array = [
    ['Car', 'Top Speed', 'Price'],
    ['Chevrolet', '120mph', '$10,000'],
    ['Pontiac', '140pmh', '$20,000'],
    ['BMW', '160mph', '$30,000']
  ]

console.log("Array of arrays: ", array);

// (async function() {
//     const { text } = await( await fetch(`/api/message`)).json();
//     document.querySelector('#name').textContent = text;
// }());

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

async function fetchData() {
    try {
        const response = await fetch(`/api/message`);
        if (!response.ok) {
            throw new Error("API call was not ok");
        }
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error("Error:", error);
    }
}

console.log(fetchData());

console.log("Before car's TABLE");

var table = document.createElement('table');
document.body.appendChild(table); // Drew the main table node on the document

array.forEach(function(row) {
  var tr = table.insertRow(); //Create a new row

  row.forEach(function(column) {
    var td = tr.insertCell();
    td.innerText = column; // Take string from placeholder variable and append it to <tr> node
  });
});

console.log("After car's TABLE");