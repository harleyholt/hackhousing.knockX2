L.mapbox.accessToken = 'pk.eyJ1Ijoia25vY2siLCJhIjoiRVdjRFVjRSJ9.nIZeVnR6dJZ0hwNnKAiAlQ'

map = L.mapbox.map('map', 'knock.l5dpakki').
  setView([47.61, -122.33], 13)

featureLayer = L.mapbox.featureLayer().addTo(map)
featureLayer.loadURL('http://zillowhack.hud.opendata.arcgis.com/datasets/2a462f6b548e4ab8bfd9b2523a3db4e2_0.geojson?where=FORMAL_PARTICIPANT_NAME%20like%20\'%25Seattle%20Housing%20Authority%25\'&geometry={"xmin":-13644455.898275688,"ymin":6030489.247026406,"xmax":-13589421.237910435,"ymax":6053382.136997785,"spatialReference":{"wkid":102100}}')
