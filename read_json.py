# reads json from the data 
import pandas as pd
import json

# other functions as well
import matplotlib.pyplot as plt

def read_json(obj):
  # replace quotes
  jdata = obj.replace("\'", "\"")
  return json.loads(jdata)

# nombre más bonito
def as_json(obj):
  # replace quotes
  jdata = obj.replace("\'", "\"")
  return json.loads(jdata)

def remove_name(obj):
  # removes "name" param in
  # hostnames
  
  return

def plot_histogram(dframe,bns: int, logscale: bool):
  
  # plot a histogram 
  fig, ax = plt.subplots(figsize=(7,3))
  plt.title(dframe.name + " histogram")
  ax.hist(x=dframe, bins=bns)
  if logscale:
    ax.set_yscale("log")

  ax.set_xlabel(dframe.name)
  ax.set_ylabel("freq")
  return fig