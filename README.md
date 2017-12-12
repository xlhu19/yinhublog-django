## 安装
使用pip安装：  
`pip install -Ur requirements.txt`

    ./manage.py makemigrations
    ./manage.py migrate  


    ./manage.py createsuperuser
### 创建测试数据
终端下执行:  

    ./manage.py create_testdata
### 收集静态文件
终端下执行:  

    ./manage.py collectstatic --noinput
    ./manage.py compress --force
### 开始运行：
 执行：  
 `./manage.py runserver`





 浏览器打开: http://127.0.0.1:8000/  就可以看到效果了。  

 ## 问题相关

 有任何问题欢迎提Issue,或者将问题描述发送至我邮箱 `liangliangyy#gmail.com`.我会尽快解答.推荐提交Issue方式.
