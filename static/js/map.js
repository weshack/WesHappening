function initialize() {

  /*
   * Dynamically adds html options to a select menu with given id
   */
  function add_options(selector, options) {
    for (var i=0;i<options.length;i++) {
      $(selector).append("<option>"+options[i]+"</options>");    }
  };

  var mapOptions = {
    center: new google.maps.LatLng(41.5526833,-72.6612454),
    zoom: 15,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    minZoom: 12,
    streetViewControl: false,
  };
  var map = new google.maps.Map(document.getElementById("map-canvas"),
       mapOptions);

  /*a Adds markers for all events in 'events' to the map
   */
  var markers = [];

  /* Creates a marker with a listener
   */
  function markerize(pos, name, str) {
    var marker = new google.maps.Marker({
        position: pos,
        map: map,
        //title: name,
    });

    var infowindow = new google.maps.InfoWindow({
      content: content_str,
    });

    google.maps.event.addListener(marker,'mouseover',function() {
      infowindow.open(map,marker);
    });

    google.maps.event.addListener(marker,'mouseout',function() {
      infowindow.close();
    });

    return marker;
  }

  /* Adds events to map
   */
  for (var i=0;i<events.length;i++) {
    if (Math.floor(events[i].lat) == 41 && Math.ceil(events[i].lon) == -72) {

      var content_str = '<div id="content">'+
        '<div id="siteNotice">'+
        '</div>'+
        '<h1 id="firstHeading" class="firstHeading">' + events[i].name + '</h1>'+
        '<div id="bodyContent">'+
        '<p>' + events[i].desc + '</p>' +
        //'<p>' + events[i].cat + '</p>' + 
        '<a href="' + events[i].link + '">Link</a>' +
        '</div>'+
        '</div>';

      var pos = new google.maps.LatLng(events[i].lat,events[i].lon);
      var name = events[i].name;

      var m = markerize(pos, name, content_str);

      markers.push(m);
    }
  }

  //adds options to the three search bars

  //var loc_names = [];
  //for (var i=0;i<locs.length;i++) {
  //  loc_names.push(locs[i].name);
  //}
  //add_options('#location_search',loc_names);

  var event_names = [];
  for (var i=0;i<events.length;i++) {
    event_names.push(events[i].name);
  }
  add_options("#event_search",event_names);

  /*
   * Makes search bars pretty using the chosen framework
   */
  $("#event_search").chosen({no_results_text: "Nothing Happening :(", placeholder_text_multiple: "Search for events by name.", max_selected_options: 1});

  $("#category_search").chosen({no_results_text: "No categories found :(", placeholder_text_multiple: "Filter by event category", max_selected_options: 2});

  $("#location_search").chosen({no_results_text: ":(", placeholder_text_multiple: "Filter event by location", max_selected_options: 2});


google.maps.event.addListener(map,'center_changed',function() { 

    var sw = new google.maps.LatLng(41.54, -72.69);
    var ne = new google.maps.LatLng(41.565, -72.63);
    var allowedBounds = new google.maps.LatLngBounds(sw, ne);
    if(! allowedBounds.contains(map.getCenter())) {
      var C = map.getCenter();
      var X = C.lng();
      var Y = C.lat();

      var AmaxX = allowedBounds.getNorthEast().lng();
      var AmaxY = allowedBounds.getNorthEast().lat();
      var AminX = allowedBounds.getSouthWest().lng();
      var AminY = allowedBounds.getSouthWest().lat();

      if (X < AminX) {X = AminX;}
      if (X > AmaxX) {X = AmaxX;}
      if (Y < AminY) {Y = AminY;}
      if (Y > AmaxY) {Y = AmaxY;}

      map.setCenter(new google.maps.LatLng(Y,X));
    }
});
}
google.maps.event.addDomListener(window, 'load', initialize);




  /* locations
   * Marks locations on the map. The input must be an array of 
   * objects with lat, lon, name attributes
   *
  //console.log(locs);
  //console.log(locs[0]);
  //console.log(locs[0].lat);
  for (var i=0;i<locs.length;i++) {
    //console.log('LATITUDE:'+locs[i].lat);
    //console.log('LONGITUDE:'+locs[i].lon);
    //console.log('NAME:'+locs[i].name);
    var marker = new google.maps.Marker({
      position: new google.maps.LatLng(locs[i].lat, locs[i].lon),
      map: map,
      title:locs[i].name,
    });
    marker.setMap(map);
  }
  */

