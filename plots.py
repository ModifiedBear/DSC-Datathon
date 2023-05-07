import matplotlib.pyplot as plt

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