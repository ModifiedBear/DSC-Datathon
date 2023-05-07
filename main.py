import pandas as pd

from resampling import resampling
from pipeline import pipeline

def main():
    '''
    Este es un ejemplo, dado los datos del hackathon
    Se preprocesan y se toma solo uno de los servidores para analizar.
    '''
    data = pd.read_csv("data.csv")
    data_sample = data.sample(n = 100000, random_state=2333)
    files = resampling(data_sample, 'resampled')

    server_data = pd.read_csv(files[0])
    anomalies = pipeline(server_data)

    return anomalies
    
if __name__ == '__main__':
    main()