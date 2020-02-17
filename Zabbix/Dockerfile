FROM ubuntu:18.04
MAINTAINER SREProject

RUN docker run \
   -d \
   --name dockbix-db \
   -v /etc/localtime:/etc/localtime:ro \
   --env="MARIADB_USER=zabbix" \
   --env="MARIADB_PASS=zabbix" \
   monitoringartist/zabbix-db-mariadb && \
   docker run \
   -d \
   --name dockbix \
   -p 80:80 \
   -p 10051:10051 \
   -v /etc/localtime:/etc/localtime:ro \
   --link dockbix-db:dockbix.db \
   --env="ZS_DBHost=dockbix.db" \
   --env="ZS_DBUser=zabbix" \
   --env="ZS_DBPassword=zabbix" \
   --env="XXL_zapix=true" \
   --env="XXL_grapher=true" \
   monitoringartist/dockbix-xxl:latest