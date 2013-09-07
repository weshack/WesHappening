function initialize() {
  var mapOptions = {
    center: new google.maps.LatLng(41.5526833,-72.6612454),
    zoom: 15,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    minZoom: 12,
    draggable: false,
  };
  var map = new google.maps.Map(document.getElementById("map-canvas"),
      mapOptions);

  var marker = new google.maps.Marker({
      position: new google.maps.LatLng(41.555690, -72.657589),
      map: map,
      title:"Hello",
  });
  marker.setMap(map);

}
google.maps.event.addDomListener(window, 'load', initialize);



//search logic
