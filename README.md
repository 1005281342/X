项目图像参数 
    
    图像长宽比为4：3


加载NG手势数据集方法load_data

    https://github.com/PnYuan/Practice-of-Machine-Learning/tree/master/code/SIGNS_experiment
    
数字手势识别

    https://blog.csdn.net/Snoopy_Yuan/article/details/78159603
    
分类模型训练

    使用NG提供的手势识别数据集  datas/datasets
    
使用Redis缓存识别数据确认消息

    将手势标签存放在Redis
    if 两次手势一致:
        执行动作
    else:
        将缓存更新为最新的手势

一些工具

[Keras 网络可视化](https://jingyan.baidu.com/article/925f8cb8b65feac0dde056f1.html)

[Keras 微软MMDNN](https://blog.csdn.net/qq_38906523/article/details/80319990)
环境安装：
    
[HDFView](https://www.hdfgroup.org/downloads/hdfview/?https%3A%2F%2Fwww.hdfgroup.org%2Fdownloads%2Fhdfview%2F)

