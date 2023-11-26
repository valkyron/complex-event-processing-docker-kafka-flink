# import docker
# import docker.errors
# import psutil

# def get_container_info(container_id_or_name):
#     client = docker.from_env()

#     try:
#         container = client.containers.get(container_id_or_name)
#         container_info = container.attrs

#         # Get CPU percentage
#         cpu_percentage = container.stats(stream=False)['cpu_stats']['cpu_usage']['cpu_percent']

#         # Get memory percentage
#         memory_percentage = container.stats(stream=False)['memory_stats']['usage'] / container.stats(stream=False)['memory_stats']['limit'] * 100

#         # Get memory limit
#         memory_limit_bytes = container_info['HostConfig']['Memory']
#         memory_limit_mb = memory_limit_bytes / (1024 * 1024)

#         # Get network usage and limit
#         network_stats = container.stats(stream=False, network=True)
#         network_rx_bytes = network_stats['network']['rx_bytes']
#         network_tx_bytes = network_stats['network']['tx_bytes']
#         network_limit_bytes = container_info['HostConfig']['ShmSize']  # Assuming ShmSize is used as the network limit

#         # Convert network values to megabytes for easier readability
#         network_rx_mb = network_rx_bytes / (1024 * 1024)
#         network_tx_mb = network_tx_bytes / (1024 * 1024)
#         network_limit_mb = network_limit_bytes / (1024 * 1024)

#         return {
#             'CPU Percentage': cpu_percentage,
#             'Memory Percentage': memory_percentage,
#             'Memory Limit (MB)': memory_limit_mb,
#             'Network Usage (RX, TX) MB': (network_rx_mb, network_tx_mb),
#             'Network Limit (MB)': network_limit_mb
#         }

#     except docker.errors.NotFound:
#         return None

# if __name__ == "__main__":
#     container_id_or_name = "sensor1"
#     container_info = get_container_info(container_id_or_name)

#     if container_info:
#         for key, value in container_info.items():
#             print(f"{key}: {value}")
#     else:
#         print(f"Container '{container_id_or_name}' not found.")


#------------------------------
# import docker
# import time

# client = docker.DockerClient(base_url='unix:///var/run/docker.sock')
# for i in client.containers.list():
    #  print(i.stats(stream=False))
    #  time.sleep(10)

#-------------------------------------
# import docker

# def get_container_stats(container_name):
#     client = docker.from_env()
#     container = client.containers.get(container_name)
#     stats = container.stats(stream=False)
#     return stats

# container_name = "sensor1"
# stats = get_container_stats(container_name)
# print(stats)
#-------------------------------
import random

def generate_random_2d_array(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

n = 1
while n!=100000:
    random_array = generate_random_2d_array(n)
    print(random_array)
    n += 10
#------------------------------------
# import subprocess
# from confluent_kafka import Producer

# def get_docker_stats(container_name):
#     command = f"docker stats --format 'table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}' {container_name}"
#     result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
#     return result.stdout


# namee = subprocess.run("docker ps --format \"{{.Names}}\"", shell=True, stdout=subprocess.PIPE, text=True)
# container_name = namee
# docker_stats = get_docker_stats(container_name)

# print(docker_stats)

#---------------------------------------
# import psutil
# # import mysql.connector
# import random
# # import requests
# import time
# from datetime import datetime
# from kafka import KafkaProducer

# def generate_random_2d_array(n):
#     return [[random.random() for _ in range(n)] for _ in range(n)]


# def get_system_info():
#     # Get CPU usage
#     cpu_percent = psutil.cpu_percent(interval=1)

#     # Get memory usage
#     memory_info = psutil.virtual_memory()
#     memory_percent = memory_info.percent
#     # total_memory = memory_info.total / (1024 ** 3)

#     # Get network usage
#     network_info = psutil.net_io_counters()
#     bytes_sent = network_info.bytes_sent
#     bytes_received = network_info.bytes_recv

#     return {
#         'cpu_percent': cpu_percent,
#         'memory_percent': memory_percent,
#         'bytes_sent': bytes_sent,
#         'bytes_received': bytes_received,
#         # 'total_memory': total_memory
#     }

# if __name__ == "__main__":
#     producer = KafkaProducer(bootstrap_servers='localhost:9092')

#     for i in range(10):
#         print("Time: ",datetime.now(), "\t", end='')

#         system_info = get_system_info()
#         random_array = generate_random_2d_array(10000)
# #     print(random_array)
#         # network_limit = get_network_limit()
#         # memory_limit = get_memory_limit()

#         # cpu_perc = str(system_info['cpu_percent']).encode('utf-8')
#         # mem_perc = str(system_info['memory_percent'])
#         # net_perc = str(round((system_info['bytes_sent'] + system_info['bytes_received'])/network_limit['network_limit']*100, 1)).encode('utf-8')
#         # net_limit = str(network_limit['network_limit'])
#         # mem_limit = str(memory_limit['memory_limit'])

#         print(f"{system_info['cpu_percent']}%, {system_info['memory_percent']}%, {round(system_info['bytes_sent']+system_info['bytes_received'])}")
#         producer.send('my-topic', value=b'')
#         time.sleep(1)