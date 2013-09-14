function initialize() {

  var styles_array = 
  [
    {
     "elementType": "geometry",
                    "stylers": [{ "hue": "#00e5ff" }]
    },
    {
      "featureType": "poi.school",
      "stylers": [{ "hue": "#ff0000" }]
    },
    {}
  ];

  var mapOptions = {
    center: new google.maps.LatLng(41.5526833,-72.6612454),
    zoom: 15,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    minZoom: 13,
  };
  var map = new google.maps.Map(document.getElementById("map-canvas"),
       mapOptions);
  map.setOptions({styles: styles_array});
    
  /* spreads out markers that are close */
  var oms = new OverlappingMarkerSpiderfier(map);

  /*a Adds markers for all events in 'events' to the map
   */
  var markers = [];

  function markerize(pos, name, str) {
    var marker = new google.maps.Marker({
        position: pos,
        map: map,
        //title: name,
    });
    marker.id = name;

    var infowindow = new google.maps.InfoWindow({
      content: content_str,
    });

    oms.addListener('spiderfy', function(markers) {
        infowindow.close();
    });

    
    google.maps.event.addListener(marker,'click',function() {
      infowindow.open(map,marker);
    });

    google.maps.event.addListener(map,'click',function() {
      infowindow.close();
    });

    oms.addMarker(marker);

    return marker;
  }

  /* Adds events to map
   */
  for (var i=0;i<events.length;i++) {
    if ((events[i].lat) != 0.0 && (events[i].lon) != 0.0) {

      var content_str = '<div id="content">'+
        '<h3 id="firstHeading" class="firstHeading">' + events[i].name + '</h1>'+
        '<div id="bodyContent">'+
        '<p>' + events[i].desc + '</p>' +
        '<a href="' + events[i].link + '">Link</a>' +
        '</div>'+
        '</div>';

      var pos = new google.maps.LatLng(events[i].lat,events[i].lon);
      var name = events[i].name;

      var m = markerize(pos, name, content_str);

      markers.push(m);
    }
  }


  // Adds a click listener to all the rows in the event table
  $(".event_name").each(function() {
    var m;
    var name = this.id;
    $(this).click(function(){
      for (var i=0;i<markers.length;i++) {
        if (name == markers[i].id) {
          m = markers[i];
        }
      }
      if (m != undefined && m != null) {
        google.maps.event.trigger(m,"click");
      }
    });
  });

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
