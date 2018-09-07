// from data.js
var tableData = data;

// YOUR CODE HERE!
//function handleSubmit() {
  // Prevent the page from refreshing
  //d3.event.preventDefault();

  // Select the input value from the form
  //var inputValue = d3.select("#datetime").node().value;


  // clear the input value
  //d3.select("#datetime").node().value = "";

  // Get the value property of the input element
  var submit = d3.select("#filter-btn");

submit.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#datetime");
  var inputValue = inputElement.property("value");


  var filteredData = data.filter(ufo_data => ufo_data.datetime === inputValue);

  console.log(filteredData);


  var date = filteredData.map(ufo_data => ufo_data.datetime);
  var city = filteredData.map(ufo_data => ufo_data.city);
  var state = filteredData.map(ufo_data => ufo_data.state);
  var country = filteredData.map(ufo_data => ufo_data.country);
  var shape = filteredData.map(ufo_data => ufo_data.shape);
  var duration = filteredData.map(ufo_data => ufo_data.durationMinutes);
  var comment = filteredData.map(ufo_data => ufo_data.comments);
  buildTable(date,city, state, country, shape, duration, comment);
});


  function buildTable(date,city, state, country, shape, duration, comment) {
  var table = d3.select("#ufo-table");
  var tbody = table.select("tbody");
  var trow;
  for (var i = 0; i < data.length; i++) {
    trow = tbody.append("tr");
    trow.append("td").text(date[i]);
    trow.append("td").text(city[i]);
    trow.append("td").text(state[i]);
    trow.append("td").text(country[i]);
    trow.append("td").text(shape[i]);
    trow.append("td").text(duration[i]);
    trow.append("td").text(comment[i]);
  }
}

//d3.select(".filter-btn").on("click");
