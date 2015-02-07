#!/usr/local/bin python3

from argparse import ArgumentParser
import os
import json


def main(src, target, conv_func):
    if target is None:
        f_name, _ = os.path.splitext(src)
        target = '{}_geo.json'.format(f_name)
    # not an option yet
    conv_func = convert_police_data
    data = json.load(open(src))
    geo_data = conv_func(data)
    with open(target, 'w+') as f:
        f.write(json.dumps(geo_data))


def convert_police_data(data):
    geo_data = {
                "type": "FeatureCollection",
                "crs": {
                    "type": "name",
                    "properties": {
                        "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                        }
                    },
                "features": []
                }
    for x in data:
        loc = x.get('location')
        latitude = loc.get('latitude') if loc else x.get('latitude')
        longitude = loc.get('longitude') if loc else x.get('longitude')
        if latitude and longitude:
            geo_feature = {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Point",
                    "coordinates": [ float(longitude), float(latitude) ]
                    }
                }
            geo_feature['properties'] = x
            geo_data['features'].append(geo_feature)
    return geo_data


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('--target', default=None)
    parser.add_argument('-f', '--conv_func', default=0, help='no options yet')
    args = parser.parse_args()
    main(args.source, args.target, args.conv_func)
