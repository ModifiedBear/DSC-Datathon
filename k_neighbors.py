import numpy as np
from sklearn.neighbors import NearestNeighbors

def outliers_from_n_neighbors(data_1, data_2, timestamps, n, desviaciones):
    # Filtros de nans e infs
    filter = ~np.isnan(data_1) *  ~np.isinf(data_1)
    data_1 = data_1[filter]
    data_2 = data_2[filter]
    timestamps = timestamps[filter]

    filter_2 = ~np.isnan(data_2) *  ~np.isinf(data_2)

    data_1 = data_1[filter_2]
    data_2 = data_2[filter_2]
    timestamps = timestamps[filter_2]

    # Agrupar
    X = np.vstack([data_1, data_2]).T

    # Nearest neighbors
    nbrs = NearestNeighbors(n_neighbors=n).fit(X)
    distances, _ = nbrs.kneighbors(X)

    # Promedio de distancias
    promedios = distances.mean(axis = 1)

    # Desv est
    desv_est = np.std(promedios)

    # Outliers
    outlier_index = np.where(promedios > desviaciones * desv_est)
    outlier_index = outlier_index[0].tolist()

    outlier_data_1 = data_1.iloc[outlier_index]
    outlier_data_2 = data_2.iloc[outlier_index] 
    outlier_times = timestamps[outlier_index]  

    # Return data
    return outlier_data_1, outlier_data_2, outlier_times
