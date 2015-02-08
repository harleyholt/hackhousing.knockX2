db.features.ensureIndex({geometry: '2dsphere'});

db.features.aggregate([{ $geoNear: {near: {'type': 'Point', 'coordinates': [ -122.011853004025269, 47.187382316240615 ]}, spherical: true, distanceField: 'dist', maxDistance: 1}}])
