文章
177
标签
158
分类
37
首页
归档
标签
相关链接
留言板
关于
共赴良策
Apple小火箭跳过开屏广告
搜索
首页
归档
标签
相关链接
留言板
关于
Apple小火箭跳过开屏广告
发表于
2024-06-23
|
其他
|
总字数:
439
|
阅读时长:
1分钟
|
浏览量:
说明
之前发过一篇文章说明Apple跳过广告的方法，主要是讲了surge，小火箭一笔带过。结果下面很多人反馈规则不生效，所以今天我就使用小火箭来试一下并说明使用方法。
首先我要说的是，之前分享的规则并不是所有app都能生效！因为作者写的规则肯定不会覆盖到所有app的，如果需要不存在里面的需要自己去单独找或者自己写。我这边是建议用圈X，相对而言用的人较多，规则也较全。
使用方式
首先打开https解密
我是一开始就使用了https解密，并没有试验过是不是一定要https解密。实际上当我关闭https解密时跳过广告也能生效，但是留言有小伙伴提醒需要，那我就加上https解密的配置，作为保险手段。
打开方式：
配置->右上角+号，导入下列url
https://whatshub.top/config/shadowrocket_basic.conf
导入完成后，点击新增的本地配置
shadowrocket_basic.conf
点击
使用配置
按钮。
点击配置文件
https解密
按钮。
打开https解密按钮
安装证书
在iphone中的
设置
->
通用
->
VPN与设备管理
中安装证书
配置文件->模块->导入
通过url添加模块规则
url链接为:
https://whatshub.top/module/adultraplus.module
等到一会添加完成之后会有弹框提示，然后确保出现如下界面，APP启动页去广告ultra+旁边勾上。
启用规则
注意下方的全局路由选择
配置
,然后上方小火箭那开关要打开。
使用效果，以知乎app为例
文章作者:
programApe
文章链接:
https://blog.allbs.cn/posts/10392/
版权声明:
本博客所有文章除特别声明外，均采用
CC BY-NC-SA 4.0
许可协议。转载请注明来源
共赴良策
！
苹果
赞助
支付宝
微信
qq
上一篇
苹果手机跳过APP开屏广告的办法
...
下一篇
DNF私服
效果 注册         windows启动一个centerOS服务器作为服务端，有现成服务器的忽略这一步。 CenterOS下载地址 https://app.vagrantup.com/centos/boxes/7 windows中启动一个CenterOS虚拟机  虚拟机有线连接并ifconfig查看ip  前置操作（使用CenterOS服务器） 先升级yum源 1yum update -y  下载docker安装脚本 1curl -fsSL https://get.docker.com -o get-docker.sh 运行安装docker的脚本 1sudo sh get-docker.sh  启动docker 12systemctl enable dockersystemctl restart docker 关闭防火墙 12systemctl disable firewalldsystemctl stop firewalld  关闭selinux 1sudo sed -i 's/SELINUX=enforcing/SELINUX=disabled/'...
相关推荐
2024-07-11
苹果手机通过Loon跳过app开屏广告的教程
视频 直接看视频就够了，如果有不清楚的看下面的图文教程。b站视频被举报下架了，所以就直接放了，但是因为服务器带宽小，所以可能会卡😂 (function(){var player = new DPlayer({"container":document.getElementById("dplayer0"),"theme":"#FADFA3","loop":true,"video":{"url":"https://nas.allbs.cn:8888/cdn/video/loon跳广告.mp4","pic":"./img/loon.png"}});window.dplayers||(window.dplayers=[]);window.dplayers.push(player);})() 图文教程 下载 需要使用apple的外区账号，官网注册可以跳过绑定支付方式。需要5.99美刀。  生成并安装证书 在设置 -> MitM的证书管理点击生成新的证书  安装证书 在iphone的设置 -> 通用 ->VPN与设备管理  信任证书 在设置 -> 通用 ->...
2024-06-23
苹果手机跳过APP开屏广告的办法
...
2024-07-09
苹果手机通过圈X跳过app开屏广告的教程
之前做了小火箭和surge的跳过教程，有小伙伴提出想要看圈X的，反正不差这一个就顺带做了下。具体用法如下: 操作视频 这是录得操作视频，可以直接跟着操作即可，有不清楚得可以看下面文字说明。本来是放b站想白嫖带宽的，可是被举报下架了，关键给的理由还很奇怪，说是分享出来大家都没法用了，这玩意本来就没在国区上架啊😂 (function(){var player = new...
评论
programApe
为面向未来的通用的、广泛的知识共创而努力
For a Future-Focused Universal Knowledge
文章
177
标签
158
分类
37
Follow Me
公告
猿音 · iOS 音乐播放器
NAS 串流 / 刮削 / 歌词 / 无缝播放
公众号
目录
1.
说明
2.
使用方式
2.1.
首先打开https解密
2.2.
配置文件->模块->导入
2.3.
通过url添加模块规则
2.4.
启用规则
3.
使用效果，以知乎app为例
最新文章
spring boot项目excel导出功能封装——5.导入带进度以及忽略错误
2025-11-28
spring boot项目excel导出功能封装——4.导入
2025-11-27
spring boot项目excel导出功能封装——3.图表导出
2025-11-26
spring boot项目excel导出功能封装——2.高级导出
2025-11-25
spring boot项目excel导出功能封装——1.简单导出
2025-11-24
©2018 - 2026 By programApe
框架
Hexo 7.3.0
|
主题
Butterfly 5.4.0-b1
简
搜索
数据加载中
