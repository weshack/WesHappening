$(document).ready(function(){
  $(".event_search").chosen({no_results_text: "Nothing Happening :(",
                             placeholder_text_single: "Search for events by name."});

  $(".category_search").chosen({no_results_text: "No categories found :(",
                           placeholder_text_multiple: "Filter by event category"});
});
