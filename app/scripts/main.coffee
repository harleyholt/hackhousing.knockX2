L.mapbox.accessToken = 'pk.eyJ1Ijoia25vY2siLCJhIjoiRVdjRFVjRSJ9.nIZeVnR6dJZ0hwNnKAiAlQ'

map = L.mapbox.map('map', 'knock.l5dpakki').
  setView([47.61, -122.33], 13)

featureLayer = L.mapbox.featureLayer().addTo(map)
featureLayer.loadURL('/data/school_sites.json')
