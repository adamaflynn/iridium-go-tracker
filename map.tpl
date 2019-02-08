<!DOCTYPE html>
<html>
<head>
	<title>$boat_name Map</title>

	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.4.0/dist/leaflet.css" integrity="sha512-puBpdR0798OZvTTbP4A8Ix/l+A4dHDD0DGqYW6RQ+9jxkRFclaxxQb/SJAWZfWAkuyeQUytO7+7N4QKrDh+drA==" crossorigin=""/>
    <script src="https://unpkg.com/leaflet@1.4.0/dist/leaflet.js" integrity="sha512-QVftwZFqvtRNi0ZyCtsznlKSWOStnDORoefr1enyq5mVL4tmKB3S/EnC3rRJcxCPavG10IcrVGSmPh6Qw5lwrg==" crossorigin=""></script>
</head>
<body>

<div id="mapid" style="width: 95%; height: 95%; position: absolute;"></div>
<script>
    var positions = $position_json;

	var map = L.map('mapid').setView(positions[0], 7);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png?{foo}', {foo: 'bar', attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'}).addTo(map);

    var polyline = L.polyline(positions, {color: '#ff6633', weight: 2, opacity: 0.75 }).addTo(map);

	L.marker(positions[0]).addTo(map)
		.bindPopup("<b>$boat_name</b> is at $formatted_position" +
                   "<br /><br />" +
                   "Last position reported: $last_report_time").openPopup();

</script>
</body>
</html>
