import os, json
from elasticsearch import Elasticsearch
es = Elasticsearch()

json_files = [pos_json for pos_json in os.listdir("./") if pos_json.startswith('mpd.slice')]

es.indices.delete(index='playlists')
mapping = "{ 'properties': { 'tracks.track_uri': { 'type': 'text','fielddata': true }}}"
es.indices.create(index='playlists', ignore=400)
for file in json_files:
    with open(file) as file:
        data = json.load(file)

    for playlist in data["playlists"]:
        # index name is playlists
        es.index(index='playlists', doc_type="playlist", body=playlist)

#es.indices.put_mapping(index='playlists', mapping=mapping)



