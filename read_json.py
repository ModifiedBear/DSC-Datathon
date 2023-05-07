import json
import matplotlib.pyplot as plt
from datetime import datetime

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

def format_time(time):
  # convert dframe of time values
  format = "%Y-%m-%dT%H:%M:%S.%fZ"
  time_formatted = datetime.strptime(time, format)
  return time_formatted
