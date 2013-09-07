//returns an array of locations. The array is filled with objects
// where the first element is latitude, second element is longitude
// , and third element is the name.
function parse_locations(loc_str) {
  var locs = [];
  loc_str.replace(/&#34;/g,"'");
  arr = loc_str.split("}, {");
  for (var i=0;i<arr.length;i++) {
    //console.log(arr[i]);
    var lat_re = /lat&#34;: (\d+.\d+)/;
    var lon_re = /lon&#34;: (-\d+.\d+)/;
    var name_re = /name&#34;: &#34;([\w\s]+)/;

    var lat_match = lat_re.exec(arr[i]);
    //console.log(lat_match[1]);
    var lon_match = lon_re.exec(arr[i]);
    //console.log(lon_match[1]);
    var name_match = name_re.exec(arr[i]);
    //console.log(name_match[1]);

    var obj = new Object();
    obj.lat = lat_match[1];
    obj.lon = lat_match[1];
    obj.name = lat_match[1];

    locs.push(obj);
  }
  return locs
}
