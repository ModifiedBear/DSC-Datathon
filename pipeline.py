import numpy as np
from indicators import used_mem_cpu_indicator, free_mem_cpu_indicator, idle_swap_indicator, cores_cpu_usage_indicator

def pipeline(server_data):
    timestamps = np.array(server_data['@timestamp'])

    [_, _, used_mem_cpu] = used_mem_cpu_indicator(server_data, timestamps)
    [_, _, free_mem_cpu] = free_mem_cpu_indicator(server_data, timestamps)
    [_, _, idle_swap] = idle_swap_indicator(server_data, timestamps)
    [_, _, cores_cpu] = cores_cpu_usage_indicator(server_data, timestamps)

    anomaly_scores = []

    for time in timestamps:
        anomaly_score = 0

        if time in used_mem_cpu:
            anomaly_score+=1

        if time in free_mem_cpu:
            anomaly_score+=1

        if time in idle_swap:
            anomaly_score+=1

        if time in cores_cpu:
            anomaly_score+=1

        anomaly_scores.append(anomaly_score)

    return timestamps, anomaly_scores


