#!/usr/bin/env coffee
#
# Loads data from a passed in file into the mongo database collection.
# Assumes that the data is geoJSON file with a features key in the root object.

fs = require('fs')
{Db, Server} = require('mongodb')

dbName = 'test_geospatial'
collectionName = 'features'
server = new Server('localhost', 27017)

openCollection = (cb) ->
  db = new Db(dbName, server, safe: false)
  db.open((err, db) ->
    features = db.collection(collectionName)
    cb(err, features)
  )

loadFeatures = (dbCollection, data, cb) ->
  dbCollection.insert(data.features, {w:1}, (err, result)->
    cb(err, result)
  )

file = fs.readFile(process.argv[2], 'utf8', (err, data) ->
  throw err if (err)
  data = JSON.parse(data)
  openCollection( (err, collection) ->
    throw err if err?
    loadFeatures(collection, data, (err, result) ->
      throw err if err?
      console.log data.features.length + ' records inserted.'
      console.log 'Close the connection with cmd-D'
    )
  )
)

