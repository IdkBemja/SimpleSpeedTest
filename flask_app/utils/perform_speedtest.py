import speedtest

def bits_to_megabits(bits):
    return bits / 1_000_000

def megabits_to_megabytes(megabits):
    return megabits / 8

def get_server_info():
    st = speedtest.Speedtest()
    server = st.get_best_server()
    server_name = server['name']
    server_isp = server['sponsor']
    return server_name, server_isp

def get_client_info():
    st = speedtest.Speedtest()
    client_info = st.results.client
    isp = st.results.client['isp']
    public_ip = client_info['ip']
    return public_ip, isp

# Start the speedtest 
def start_speed():
    st = speedtest.Speedtest()
    server = st.get_best_server()
    server_name = server['name']
    server_isp = server['sponsor']
    client_info = st.results.client
    user_public_ip = client_info['ip']
    user_isp = st.results.client['isp']
    down_speed = st.download()
    up_speed  = st.upload()
    user_ping = st.results.ping

    download_speed_mbps = bits_to_megabits(down_speed)
    upload_speed_mbps = bits_to_megabits(up_speed)

    return {
        'server_name': server_name,
        'server_isp': server_isp,
        'user_ip' : user_public_ip,
        'user_isp': user_isp,
        'download_speed_mbps': download_speed_mbps,
        'upload_speed_mbps': upload_speed_mbps,
        'user_ping': user_ping
    }


# This function convert the speedtest results of download and upload megabits per second to megabytes per second
def convert_speedtest_results(results_dict):
    new_results = results_dict.copy()
    new_results['download_speed_MBps'] = megabits_to_megabytes(results_dict['download_speed_mbps'])
    new_results['upload_speed_MBps'] = megabits_to_megabytes(results_dict['upload_speed_mbps'])


    # This Remove the old results (mbps) to use only MBps
    del new_results['download_speed_mbps']
    del new_results['upload_speed_mbps']

    return new_results