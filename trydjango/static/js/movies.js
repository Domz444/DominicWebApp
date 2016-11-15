// On document ready:

$(function(){
    


// $('.movieLink').click(function(e) {
//   e.preventDefault();
//   var link = $(this).text();
//   console.log('movieLink click:', link);
//   search(link);
// });

  // $('#MixItUp1').mixItUp({
  //   selectors: {
  //     filter: '.filter-1',
  //     sort: '.sort-1'
  //   }
  // });

$("#searchButton").on("click", function(){
  var input = $("#search-by-id-form").val();
  search(input);
  // location.reload();
});

    setInterval(function () {
        $('#steam').fadeOut(3000).delay(1000).fadeIn(3000).delay(1000).fadeOut(3000);
    }, 5000);

  });


function search(val) {

  $.ajax({
      type: "GET",
      url: "http://www.omdbapi.com/?",
      data: { 
        s: val, 
        y: '', 
        plot: 'short', 
        r: 'json',
      },
      dataType: "jsonp",
      success: function (data) {
        console.log(data);
          var obj = data.Search; // get entry object (array) from JSON data
                                  // create a new ul element
          // iterate over the array and build the list
          for (var res in obj) {
            var ul = $('<div class="col-md-12" data-bg=>');
            ul.append('<h3> <a href="/posts/create/" class="movieLink" >'+ obj[res].Title +'</a> ( '+ obj[res].Year +') - '+ obj[res].Type +' </h3>');
            ul.append('<img src="'+ obj[res].Poster + '">');
            // ul.append('<li> '+ obj[res].Type +'</li>');
            // ul.append('<li> '+ obj[res].Year +'</li>');
            ul.append('</div>');
            $("#results").append(ul);    // add the list to the DOM
        }   
      }

  });

}
