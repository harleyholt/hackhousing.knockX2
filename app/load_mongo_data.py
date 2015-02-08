#!/usr/local/bin python3

from argparse import ArgumentParser
import json
import pymongo
from bson.son import SON
from pprint import pprint


def main(data_file, weight, label):
    collection = get_db_collection()
    if data_file is not None:
        geo_data = json.load(open(data_file))
        count = add_mongo_data(collection, geo_data, weight, label)
        print('total features: {}'.format(count))
    address = [-122.3331, 47.6097]
    nearby = get_points_near(collection, address)
    print('nearby features: {}'.format(len(nearby)))
    #pprint(nearby)


def get_points_near(coll, addr):
    query = {
            "geometry": {
                "$near": {
                    "$geometry": {
                        "type": "Point",
                        "coordinates": addr,
                        },
                    "$maxDistance": 1600,
                    }
                }
            }
    return [x for x in coll.find(query)]


def add_mongo_data(collection, data, weight, label):
    count = 0
    for f in data['features']:
        # create a new one b/c mongo will know
        small_data = {
                      'weight': weight,
                      'label': label,
                      'geometry': f.get('geometry')
                     }
        # don't care about the id
        _ = collection.insert(small_data)
        count += 1
    print('attempted to insert {} features'.format(count))
    return collection.count()


def get_db_collection(name=None):
    db = get_db()
    if name is None:
        name = 'map_data'
    existing = name in db.collection_names()

    # get/create the collection
    collection = db[name]
    if not existing:
        collection.create_index([('geometry', '2dsphere')])
    return collection

def get_db(name=None):
    c = pymongo.MongoClient('localhost', 27017)
    if name is None:
        name = 'map_database'
    # get/create the db
    db = c[name]
    return db

def clear_collection():
    if ask('Are you sure you want to clear the collection?'):
        print('clearing collection')
        coll = get_db_collection()
        coll.drop()
    else:
        print('clear aborted')

def clear_db():
    if ask('Are you sure you want to drop the database?'):
        print('dropping the db')
        c = pymongo.MongoClient('localhost', 27017)
        # get the db
        db = c.map_database
        db.drop
    else:
        print('drop aborted')

def ask(msg):
    res = raw_input('{} (y/n) >> '.format(msg))
    return res.lower() in ['y','yes']


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f', '--data_file')
    parser.add_argument('-w', '--weight', type=int)
    parser.add_argument('-l', '--label')
    parser.add_argument('-d', '--drop', action='store_true')
    args = parser.parse_args()

    if args.drop:
        clear_collection()
    else:
        main(args.data_file, args.weight, args.label)
