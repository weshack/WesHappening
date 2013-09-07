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

  /*
   * Marks locations on the map. The input must be an array of 
   * objects with lat, lon, name attributes
   */
  console.log(locs);
  console.log(locs[0]);
  console.log(locs[0].lat);
  for (var i=0;i<locs.length;i++) {
    console.log('LATITUDE:'+locs[i].lat);
    console.log('LONGITUDE:'+locs[i].lon);
    console.log('NAME:'+locs[i].name);
    var marker = new google.maps.Marker({
      position: new google.maps.LatLng(locs[i].lat, locs[i].lon),
      map: map,
      title:locs[i].name,
    });
    marker.setMap(map);
  }
  

}
google.maps.event.addDomListener(window, 'load', initialize);



//search logic
