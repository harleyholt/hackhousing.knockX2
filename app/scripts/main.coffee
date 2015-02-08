L.mapbox.accessToken = 'pk.eyJ1Ijoia25vY2siLCJhIjoiRVdjRFVjRSJ9.nIZeVnR6dJZ0hwNnKAiAlQ'

map = L.mapbox.map('map', 'knock.l5dpakki').
  setView([47.61, -122.33], 13)

grid = L.mapbox.gridLayer('knock.l5dpakki').addTo(map)
gridControl = L.mapbox.gridControl(grid).addTo(map);

layers = {}

layers.schools = L.mapbox.featureLayer().addTo(map)
layers.schools.setStyle(color: 'red')
layers.schools.loadURL('/data/school_sites.json')
layers.housing = L.mapbox.featureLayer().addTo(map)
layers.housing.setStyle(color: 'blue')
layers.housing.loadURL('/data/seattle_public_housing_buildings.json')
