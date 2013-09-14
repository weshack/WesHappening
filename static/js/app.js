function parse_events(event_str) {
  var events = [];
  arr = event_str.split("}, {");
  for (var i=0;i<arr.length;i++) {
    var cat_re = /category&#34;: &#34;(.+?(?=&#34;))/;
    var link_re = /link&#34;: &#34;(.+?(?=&#34;))/;
    var name_re = /name&#34;: &#34;(.+?(?=&#34;))/;
    var desc_re = /description&#34;: &#34;(.+?(?=&#34;))/
    var lat_re = /lat&#34;: (\d+.\d+)/;
    var lon_re = /lon&#34;: (-?\d+.\d+)/;

    var cat_match = cat_re.exec(arr[i]);
    var link_match = link_re.exec(arr[i]);
    var name_match = name_re.exec(arr[i]);
    var desc_match = desc_re.exec(arr[i]);
    var lat_match = lat_re.exec(arr[i]);
    var lon_match = lon_re.exec(arr[i]);
    
    var obj = new Object();
    obj.cat = cat_match[1];
    obj.link = link_match[1];
    obj.name = name_match[1];
    if (desc_match) {
        obj.desc = desc_match[1];
    }
    else {
        obj.desc = ""
    }
    obj.lat = lat_match[1];
    obj.lon = lon_match[1];

    events.push(obj)
  }

  return events
}
