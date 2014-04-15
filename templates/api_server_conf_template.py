import string

template = string.Template("""
[DEFAULT]
# auth=keystone
cassandra_server_list=$__contrail_cassandra_server_list__
# collectors= # Provided by discovery server
# http_server_port=8084
listen_ip_addr=$__contrail_listen_ip_addr__
listen_port=$__contrail_listen_port__
# log_category=''
# log_level=SYS_DEBUG
# log_local=False
log_file=$__contrail_log_file__
# logging_level=WARN
multi_tenancy=$__contrail_multi_tenancy__
# reset_config=False
# wipe_config=False
# worker_id=0
zk_server_ip=$__contrail_zookeeper_server_ip__

[DISCOVERY]
server=$__contrail_disc_server_ip__
port=$__contrail_disc_server_port__

[IFMAP]
server=$__contrail_ifmap_server_ip__
port=$__contrail_ifmap_server_port__
user=$__contrail_ifmap_username__
password=$__contrail_ifmap_password__
# server_url= # Provided by discovery server, e.g. https://127.0.0.1:8443

[RABBIT]
# password=guest
# server=localhost
# user=guest
# vhost=

[REDIS]
server=$__contrail_redis_ip__
# port=8443

[SECURITY]
use_certs=$__contrail_use_certs__
keyfile=$__contrail_keyfile_location__
certfile=$__contrail_certfile_location__
ca_certs=$__contrail_cacertfile_location__
# ifmap_certauth_port=8444

[KEYSTONE]
auth_host=$__contrail_keystone_ip__
# auth_port=35357
# auth_protocol=http
admin_user=$__contrail_admin_user__
admin_password=$__contrail_admin_password__
admin_token=$__contrail_admin_token__
admin_tenant_name=$__contrail_admin_tenant_name__
memcache_servers=$__contrail_memcached_server__
# token_cache_time=
""")
