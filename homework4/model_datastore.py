from google.cloud import datastore
import logging

# Create a client to access the datastore
client = datastore.Client()

# Define the kind for the new datastore entities
KIND = "hw4"

def list_entities():
    query = client.query(kind=KIND)
    return list(query.fetch())

def create_entity(data):
    key = client.key(KIND)
    entity = datastore.Entity(key=key)
    entity.update(data)
    client.put(entity)
    return entity.key

def read_entity(entity_id):
    key = client.key(KIND, entity_id)
    return client.get(key)

def update_entity(entity_id, data):
    key = client.key(KIND, entity_id)
    entity = datastore.Entity(key=key)
    entity.update(data)
    client.put(entity)

def delete_entity(entity_id):
    key = client.key(KIND, entity_id)
    client.delete(key)
