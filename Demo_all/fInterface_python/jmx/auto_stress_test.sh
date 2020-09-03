#!/usr/bin/env bash
# 压测脚本模板中设定的压测时间应为60秒
# 组建带有并发数的脚本
export jmx_template="iInterface"
export suffix=".jmx"
export jmx_template_filename="${jmx_template}${suffix}"
#mac linux环境区分
export os_type=`uname`

# 需要在系统变量中定义jmeter根目录的位置，如下
export jmeter_path="/Users/a/Documents/software/apache-jmeter-5.1.1"

echo "自动化压测开始"

# 压测并发数列表
thread_number_array=(10 20 30)
for num in "${thread_number_array[@]}"
do
    # 生成对应压测线程的jmx文件
    # jmx_filename:待运行的脚本名；
    export jmx_filename="${jmx_template}_${num}${suffix}"
    # jtl_filename: 生成的运行报告jtl名；
    export jtl_filename="test_${num}.jtl"
    # web_report_path_name：
    export web_report_path_name="web_${num}"

    rm -f ${jmx_filename} ${jtl_filename}
    rm -rf ${web_report_path_name}

    cp ${jmx_template_filename} ${jmx_filename}
    echo "生成jmx压测脚本 ${jmx_filename}"

    if [[ "${os_type}" == "Darwin" ]]; then
        #改变并发数  mac
        sed -i "" "s/thread_num/${num}/g" ${jmx_filename}
    else
        sed -i "s/thread_num/${num}/g" ${jmx_filename}
    fi

    # JMeter 静默压测
    ${jmeter_path}/bin/jmeter -n -t ${jmx_filename} -l ${jtl_filename}

    # 生成Web压测报告
    ${jmeter_path}/bin/jmeter -g ${jtl_filename} -e -o ${web_report_path_name}

    rm -f ${jmx_filename} ${jtl_filename}
done
echo "自动化压测全部结束"

