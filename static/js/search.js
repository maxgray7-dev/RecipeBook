function searchFunction() {
    // Declare variables
    var input, filter, i, txtValue;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase();
    collection = document.getElementsByClassName("col-md-4");
  
    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < collection.length; i++) {
      cardtitle = collection[i].getElementsByClassName("card-title")[0];
      txtValue = cardtitle.textContent || cardtitle.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        collection[i].style.display = "";
      } else {
        collection[i].style.display = "none";
      }
    }
  }