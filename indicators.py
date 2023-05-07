from k_neighbors import outliers_from_n_neighbors

def used_mem_cpu_indicator(data, timestamps):
    memory = data['actual_used_pct']  
    cpu = data['cpu_user_pct'] + data['cpu_system_pct']
    outlier_memory, outlier_cpu, out_times = outliers_from_n_neighbors(memory, cpu, timestamps, 7, 3)
    
    return outlier_memory, outlier_cpu, out_times

def free_mem_cpu_indicator(data, timestamps):
    mem_free = data['free']  / data['bytes_total']
    cpu = data['cpu_user_pct'] + data['cpu_system_pct']
    out_mem, out_cpu, out_times = outliers_from_n_neighbors(mem_free, cpu, timestamps, 7, 3)

    return out_mem, out_cpu, out_times

def idle_swap_indicator(data, timestamps):
    idle = data['cpu_idle_pct']  
    swap = data['swap']
    out_memory, out_cpu, out_times = outliers_from_n_neighbors(idle, swap, timestamps, 7, 3)

    return out_memory, out_cpu, out_times

def cores_cpu_usage_indicator(data, timestamps):
    cores = data['cores']  
    usage = (data['user_pct'] + data['idle_pct']) / data['system_pct']
    out_memory, out_cpu, out_times = outliers_from_n_neighbors(cores, usage, timestamps, 7, 3)

    return out_memory, out_cpu, out_times

   
    