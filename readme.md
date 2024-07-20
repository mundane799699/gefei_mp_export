### 本仓库目的

将哥飞公众号的文章导出，方便学习出海建站

### 导出方法

工具：fiddler + pc版微信 + [wechatDownload](https://github.com/qiye45/wechatDownload)

### 导出步骤

参考：

https://github.com/hzhu212/wechat-mp-crawler

https://cloud.tencent.com/developer/article/2236195

首先用 [wechatDownload](https://github.com/qiye45/wechatDownload)获得历史目录：

https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MjM5OTIzMzYyMA==&scene=124#wechat_redirect

用微信打开，记得在通用设置中取消勾选使用系统默认浏览器打开网页

然后往下滚动，接着导出sessions，使用python脚本extract_wechat_url.py转成url的txt文件。

复制txt文件中的所有内容，粘贴到[wechatDownload](https://github.com/qiye45/wechatDownload)，点击文章下载

### 为什么不直接用wechatDownload？

试过，在我电脑上批量下载的时候会闪退

### 可能存在的问题

有时候在pc微信上打开历史目录页面，滚动了几次之后就一直显示正在加载中了。这时候可以换成手机抓包，在手机模拟器打开历史目录。具体可参考[fiddler everywhere + 夜神模拟器抓包小红书](https://juejin.cn/post/7186501682396659749)。方法是差不多的，就是手机抓包会麻烦一点。

### 请随意打赏

<img src="https://cdn.mundane.ink/202406292004494.jpg" width="300px" /><img src="https://cdn.mundane.ink/202406292004272.png" width="300px" />