FROM ogrerun/base:ubuntu22.04-arm64
ENV TZ=America/Chicago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /opt/bert_global_model
COPY . .
RUN cp ./ogre_dir/bashrc /etc/bash.bashrc
RUN chmod a+rwx /etc/bash.bashrc
