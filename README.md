# Anjuke_info
## 项目描述
    对安居客网站按小区进行小区详情信息，二手房详细信息，出租房详细信息爬取并保存到mongoDB
## 项目功能描述
    该项目以安居客网站中 城市>行政区>小区>二手房&出租房 为爬虫逻辑结构，可以添加不同的城市，
    行政区爬取，将小区详情、二手房详情、出租房详情分别放在同一数据库下的三个集合。小区详情
    采集数据项：小区id,小区名，建筑年代，物业费，开发商，小区地址，绿化，容积率，物业公司；
    二手房采集数据项：二手房链接，小区名，标题，房屋总价，建筑面积，单价；租房采集数据项：
    租房链接，小区名，月租，房屋类型，装修情况，面积，每平米租房价格，标题。
    项目需要使用代理ip，可以配合我另一个项目proxy_pool使用
## 项目使用指南
    项目从start.py文件启动，需要修改spider_anjuke.py文件中的host,xingzhengqu 两个变量以
    及header1 的参数(根据自身浏览器修改)。项目使用了mongoDB 和 Redis，也请在程序中根据自己
    电脑配置做相应修改。
## 效果展示
项目控制台输出
![1](https://github.com/studyisnotsimple/Anjuke_info/blob/master/anjuke/image/1.png)
<br>
![2](https://github.com/studyisnotsimple/Anjuke_info/blob/master/anjuke/image/4.png)
<br>
Redis去重request队列
<br>
![3](https://github.com/studyisnotsimple/Anjuke_info/blob/master/anjuke/image/3.png)
<br>
mongoDB 可视化工具Robo3T展示数据
<br>
小区详情信息
![4](https://github.com/studyisnotsimple/Anjuke_info/blob/master/anjuke/image/2.png)
<br>
出租房信息
![5](https://github.com/studyisnotsimple/Anjuke_info/blob/master/anjuke/image/5.png)
<br>
二手房信息
![6](https://github.com/studyisnotsimple/Anjuke_info/blob/master/anjuke/image/6.png)
<br>
## 版本
    python 3.7.3
    win10
## 鸣谢
    感谢 造数科技 爬虫教学视频 给予的知识(虽然是付费)，对我scrapy框架的使用更加熟练，同时也
    是我爬虫之路的启蒙指导。教学里是对58同城的爬取，学习了之后，就对类似的安居客进行了运用。
    安居客只有IP反爬，58同城还多了个字体反爬，之后也会把58同城的分享上来。感谢 所有给予我知
    识的人
## 写在最后
    同类型网站大体爬取思路类似，只要思路理顺了，破解了反爬机制，爬虫就会相对顺利。以后多爬不
    同类型的网站，积累经验。
    
    
    
    
