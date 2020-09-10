#!/usr/bin/env bash

## 需要在Jenkins任务中配置以下参数
#export mysql_ip=127.0.0.1
#export mysql_port=3306
#export mysql_user=root
#export mysql_pwd=123456
#export TOMCAT_PATH=/Users/a/Documents/software/apache-tomcat-9.0.37/
#export PROJ_PATH=${WORKSPACE}/Demo_all/myJeeSite4

## 检查系统类型
export os_type=`uname`

## 停止tomcat的函数, 参数$1带入tomcat的路径$TOMCAT_PATH
killTomcat()
{
  pid=`ps -ef|grep $1|grep java|awk '{print $2}'`
  echo "tomcat Id list :$pid"
  if [ "$pid" = "" ]
  then
    echo "no tomcat pid alive"
  else
    kill -9 $pid
  fi
}

## 配置数据库参数
cd $PROJ_PATH/web/src/main/resources/config
if [[ "${os_type}" == "Darwin" ]]; then
	sed -i "" "s/mysql_ip/${mysql_ip}/g" application.yml
  sed -i "" "s/mysql_port/${mysql_port}/g" application.yml
  sed -i "" "s/mysql_user/${mysql_user}/g" application.yml
  sed -i "" "s/mysql_pwd/${mysql_pwd}/g" application.yml
else
  sed -i "s/mysql_ip/${mysql_ip}/g" application.yml
  sed -i "s/mysql_port/${mysql_port}/g" application.yml
  sed -i "s/mysql_user/${mysql_user}/g" application.yml
  sed -i "s/mysql_pwd/${mysql_pwd}/g" application.yml
fi
## Maven 编译
cd $PROJ_PATH/root
mvn clean install -Dmaven.test.skip=true

## Maven 打包
cd $PROJ_PATH/web
mvn clean package spring-boot:repackage -Dmaven.test.skip=true -U

## 停止Tomcat
killTomcat $TOMCAT_PATH

## 删除tomcat中原有的工程
rm -f $TOMCAT_PATH/webapps/ROOT.war
rm -rf $TOMCAT_PATH/webapps/ROOT

## 复制/粘贴新web.war包到tomcat web 应用部署路径
cp $PROJ_PATH/web/target/web.war $TOMCAT_PATH/webapps/
cd $TOMCAT_PATH/webapps/
mv web.war ROOT.war

## 启动tomcat
cd $TOMCAT_PATH/bin
sh startup.sh