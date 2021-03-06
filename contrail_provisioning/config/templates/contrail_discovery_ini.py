import string

template = string.Template("""
[program:contrail-discovery]
command=/usr/bin/contrail-discovery --conf_file /etc/contrail/contrail-discovery.conf --listen_port $__contrail_disc_port_base__%(process_num)01d --worker_id %(process_num)s
numprocs=$__contrail_disc_nworkers__
process_name=%(process_num)s
redirect_stderr=true
stdout_logfile= /var/log/contrail/contrail-discovery-%(process_num)s-stdout.log
stderr_logfile=/dev/null
priority=430
autostart=true
killasgroup=true
stopsignal=KILL
exitcodes=0
""")
