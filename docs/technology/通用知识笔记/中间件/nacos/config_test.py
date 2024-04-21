import time

import nacos

# Both HTTP/HTTPS protocols are supported, if not set protocol prefix default is HTTP, and HTTPS with no ssl check(verify=False)
# "192.168.3.4:8848" or "https://192.168.3.4:443" or "http://192.168.3.4:8848,192.168.3.5:8848" or "https://192.168.3.4:443,https://192.168.3.5:443"


SERVER_ADDRESSES = "http://192.168.31.136:8848"
NAMESPACE = "test"
client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE)
data_id = "config.nacos"
group = "group"


def test_push_config():
    client.publish_config(data_id, group,
                          '''{"test":121213,"id":"12121","name":"hello"}''', app_name="test_app", config_type="json")
    client.publish_config(data_id + '_1', group,
                          '''
                          id:1
                          '''.strip(), app_name="test_app", config_type="yaml")

    # no auth mode
    # auth mode
    # client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE, ak="{ak}", sk="{sk}")

    # get config


def test_create_service():
    client.server_list


def test_get_config():
    print(client.get_config(data_id, group))


def test_get_servers():
    _ = client.server_list
    print(_)


def test_start_watch():
    def cb(*args,**kwargs):
        print(args,kwargs)
    client.add_config_watcher(data_id, group,cb)
    client.add_config_watcher(data_id+"_1", group,cb)


if __name__ == '__main__':
    test_push_config()
    test_get_config()
    test_get_servers()
    test_start_watch()
    while True:
        time.sleep(10)