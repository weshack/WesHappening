function initialize() {
  var mapOptions = {
    center: new google.maps.LatLng(41.5526833,-72.6612454),
    zoom: 15,
    minzoom: 13,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  var map = new google.maps.Map(document.getElementById("map-canvas"),
      mapOptions);
}
google.maps.event.addDomListener(window, 'load', initialize);



//search logic
