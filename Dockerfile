FROM debian:jessie
RUN apt-get update && apt-get upgrade --no-install-recommends -y
RUN apt-get install -y --no-install-recommends \
    openssl ca-certificates ssh parted sudo net-tools ifupdown eject python python-pyasn1 python-rpm
COPY bin/ /usr/sbin/
COPY azurelinuxagent/ /usr/local/lib/python2.7/dist-packages/azurelinuxagent
COPY config/rancheros/waagent.conf /etc/waagent.conf
RUN chmod +x /usr/sbin/waagent && \
    chmod +x /usr/sbin/waagent2.0 && \
    rm -rf /etc/skel && \
    ln -sf /dev/stdout /var/log/waagent.log
ENTRYPOINT ["/usr/sbin/waagent"]
