FROM ubuntu

RUN apt-get update && apt-get install -y openssh-server curl libcap2-bin
RUN mkdir /var/run/sshd
RUN sed -i 's/#*PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
RUN sed -i 's/#HostKey/HostKey/g' /etc/ssh/sshd_config
RUN chmod -x /etc/update-motd.d/*
RUN echo "" > /etc/motd
RUN touch /root/.hushlogin
RUN echo "export TERM=xterm-256color" >> /root/.bashrc

RUN useradd -ms /bin/bash user
RUN echo "user:plznohackme" | chpasswd
RUN touch /home/user/.hushlogin
RUN echo "export TERM=xterm-256color" >> /home/user/.bashrc

RUN setcap cap_dac_read_search+ep /usr/bin/curl

COPY flag.txt /flag.txt
RUN chmod 600 /flag.txt

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
