# reads json from the data 
import json

def read_json(obj):
  # replace quotes
  jdata = obj.replace("\'", "\"")
  return json.loads(jdata)

def remove_name(obj):
  # removes "name" param in
  # hostnames
  
  return