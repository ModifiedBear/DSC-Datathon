import pandas as pd
from read_json import as_json,format_time
import numpy as np

def resampling(data_sample, output_dir):
    # Remove nans
    id_nan = data_sample.system.isna()
    data_sample = data_sample.loc[~id_nan]

    # get hostnames
    # hostnames = data["host"].unique()            # get unique names
    hostnames = data_sample["host"].map(lambda x: as_json(x))
    hostnames = list(map(lambda x: x["name"], hostnames))
    data_sample["host"] = hostnames  # change to readable hostnames

    id_net = data_sample["event"].map(lambda x: "network" in x)
    id_mem = data_sample["event"].map(lambda x: "mem" in x)
    id_cpu = data_sample["event"].map(lambda x: "cpu" in x)

    ## CPU (implicitly, cpu_cores depends on the server)
    cpu_values     = data_sample.loc[id_cpu]["system"].map(lambda x: as_json(x))

    # normalize
    cpu_cores      = cpu_values.map(lambda x: x["cpu"]["cores"]        )
    cpu_user_pct   = cpu_values.map(lambda x: x["cpu"]["user"]["pct"]  ) / cpu_cores
    cpu_idle_pct   = cpu_values.map(lambda x: x["cpu"]["idle"]["pct"]  ) / cpu_cores
    cpu_system_pct = cpu_values.map(lambda x: x["cpu"]["system"]["pct"]) / cpu_cores

    ## NETWORK
    network_values = data_sample[id_net]["system"].map(lambda x: as_json(x))
    out_bytes = network_values.map(lambda x: x["network"]["out"]["bytes"])
    in_bytes  = network_values.map(lambda x: x["network"]["in"]["bytes"] )

    # normalize respectively
    for host in data_sample["host"].unique():
        max_out = np.max(out_bytes.loc[data_sample["host"] == host])
        max_in  = np.max(in_bytes.loc[data_sample["host"] == host])
        out_bytes.loc[data_sample["host"] == host] = out_bytes.loc[data_sample["host"] == host]/max_out
        in_bytes.loc[data_sample["host"] == host] = in_bytes.loc[data_sample["host"] == host]/max_in


    ## MEMORY

    mem_values     = data_sample.loc[id_mem]["system"].map(lambda x: as_json(x))

    actual_used_bytes = mem_values.map(lambda x: x["memory"]["actual"]["used"]["bytes"])
    actual_used_pct   = mem_values.map(lambda x: x["memory"]["actual"]["used"]["pct"])
    swap_free         = mem_values.map(lambda x: x["memory"]["swap"]["free"])
    swap_total        = mem_values.map(lambda x: x["memory"]["swap"]["total"])
    free              = mem_values.map(lambda x: x["memory"]["free"])

    swap              = 1- swap_free/swap_total
    bytes_total       = actual_used_bytes + free
    bytes_total_norm  = bytes_total/bytes_total.max()

    ## combine
    # mem_df = pd.DataFrame()
    # net_df = pd.DataFrame()
    cpu_df = pd.DataFrame({
        'cpu_cores': cpu_cores,
        'cpu_user_pct': cpu_user_pct,
        'cpu_idle_pct': cpu_idle_pct,
        'cpu_system_pct': cpu_system_pct
    })

    mem_df = pd.DataFrame({
        'actual_used_bytes' : actual_used_bytes,
        'actual_used_pct'   : actual_used_pct  ,
        'swap_free'         : swap_free        ,
        'swap_total'        : swap_total       ,
        'free'              : free             ,
        'swap'              : swap             ,
        'bytes_total'       : bytes_total      ,
        'bytes_total_norm'  : bytes_total_norm     
    })

    net_df = pd.DataFrame({
        'out_bytes': out_bytes,
        'in_bytes' : in_bytes
    })
    host_df = pd.DataFrame({'host': data_sample["host"]})
    sample_df = pd.concat([cpu_df, mem_df, net_df])

    sample_df["host"] = data_sample["host"]
    sample_df.index = pd.to_datetime(data_sample["@timestamp"].map(format_time))
    sample_df.sort_index(inplace=True)

    cpu_df.loc[data_sample["host"] == "PRUEBAS"].head(1).cpu_cores.values[0]

    cores_dict = {
        'PRUEBAS': cpu_df.loc[data_sample["host"] == "PRUEBAS"].head(1).cpu_cores.values[0] , 
        'PREPRODUCCION': cpu_df.loc[data_sample["host"] == "PRODUCCION"].head(1).cpu_cores.values[0] ,
        'DEVELOP': cpu_df.loc[data_sample["host"] == "DEVELOP"].head(1).cpu_cores.values[0] ,
        'QASERVER': cpu_df.loc[data_sample["host"] == "QASERVER"].head(1).cpu_cores.values[0],
        'PRODUCCION': cpu_df.loc[data_sample["host"] == "PRODUCCION"].head(1).cpu_cores.values[0],
    }   

    # save resampled data
    output_dirs = []
    for hostname in data_sample["host"].unique():
        host = sample_df.loc[sample_df["host"] == hostname]
        resampled = sample_df.loc[:,sample_df.columns != "host"].resample('10Min').mean()
        resampled.cpu_cores = cores_dict[hostname]
        out_dir = "resampled/" + hostname + ".csv"
        resampled.to_csv(out_dir)
        output_dirs.append(out_dir)
    
    return output_dirs