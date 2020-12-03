FROM python:3.7-alpine
LABEL maintainer='fanpl'

ADD . /code
#工作路径设定
WORKDIR /Users/a/Documents/2020study/mytestenv/docker/code

#创建环境变量给 FLASK使用
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

#复制 app.py到容器内 工作路径 /code 目录
COPY app.py .

#安装gcc工具 Python 依赖
RUN pip install flask && pip install redis

#映射端口
EXPOSE 5000

STOPSIGNAL SIGTERM

#为容器设置默认启动命令
CMD ["flask"，"run"]