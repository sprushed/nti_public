FROM containerssh/agent AS agent

FROM debian
COPY --from=agent /usr/bin/containerssh-agent /usr/bin/containerssh-agent

RUN apt update && apt -y install gcc build-essential vim openssh-client curl libcap2-bin

RUN useradd -m user

RUN chown root:user /usr/bin/ssh-keygen
RUN chmod ug+s /usr/bin/ssh-keygen

COPY flag.txt /flag.txt
RUN chmod 600 /flag.txt

RUN echo "export TERM=xterm-256color" >> /home/user/.bashrc

USER user
WORKDIR /home/user
