### 本仓库目的

将哥飞公众号的文章导出，方便学习出海建站

### 导出工具

fiddler + pc端微信 + [wechatDownload](https://github.com/qiye45/wechatDownload)


### 导出步骤

#### 1. 设置微信

在通用设置中取消勾选使用系统默认浏览器打开网页

#### 2. 获得历史目录

打开 [wechatDownload](https://github.com/qiye45/wechatDownload)(github上有)，复制一个公众号文章链接粘贴到软件，点击获取公众号id，从而获得历史目录，粘贴到文件传输助手

#### 3. 下载安装fiddler

打开fiddler，设置Tools -> options，然后是HTTPS和Connections

设置filter，设置Hosts和URL contains，Hosts 设为 `mp.weixin.qq.com`，URL contains 设为 `/mp/profile_ext?action=getmsg`

#### 4. 抓取数据

在微信中点击历史目录

然后往下滚动直到数据尽头

File -> Export Sessions，导出sessions

最后关闭Fiddler（重要，不要忘记，不然后面wechatDownload会使用不了）

#### 5. 解析url

使用python脚本extract_wechat_url.py转成url的txt文件。

#### 6. 批量下载

复制txt文件中的所有内容，粘贴到[wechatDownload](https://github.com/qiye45/wechatDownload)，点击文章下载

#### 参考资料

> https://github.com/hzhu212/wechat-mp-crawler
>
> [Python Fiddler抓包工具教学，获取公众号（pc客户端）数据](https://cloud.tencent.com/developer/article/2236195)

### 为什么不直接用wechatDownload？

试过，在我电脑上批量下载的时候会闪退

### 可能存在的问题

有时候在pc端微信上打开历史目录页面，滚动了几次之后就一直显示正在加载中了。这时候可以换成手机抓包，在手机模拟器打开历史目录。具体可参考[fiddler everywhere + 夜神模拟器抓包小红书](https://juejin.cn/post/7186501682396659749)。方法是差不多的，就是手机抓包会麻烦一点。

### 请随意打赏

<img src="https://cdn.mundane.ink/202406292004494.jpg" width="300px" /><img src="https://cdn.mundane.ink/202406292004272.png" width="300px" />
