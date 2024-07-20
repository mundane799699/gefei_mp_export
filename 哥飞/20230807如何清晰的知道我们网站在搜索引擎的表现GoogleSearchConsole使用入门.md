![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeicticSN6t4uMNkeNxysOvdR0nmwNic2g2CMwZxKAkcgEKxPRqmUL7dyl4o44m8NsofGZBCRbSZL1o0KA/0?wx_fmt=jpeg)

#  如何清晰的知道我们网站在搜索引擎的表现：Google Search Console 使用入门讲解

原创  我是哥飞  [ 哥飞 ](javascript:void\(0\);)

__ _ _ _ _

网站做好之后，我们需要让搜索引擎尽快收录我们的网站，之前哥飞讲了一个办法：

> 答案是去V2EX发帖介绍自己产品，然后留下网站链接。这个方法10年前就有用，现在更有用了，因为V站在谷歌的权重更高了。
>
> 我是哥飞，公众号：哥飞 [ 新上线的网站，如何快速让谷歌收录？做网站为什么要生成几十万个页面？
> ](https://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650079215&idx=1&sn=62b363765e616d5f6511c20a5b78c4ab&chksm=bf3eced4884947c27c5822f518876d0a21bd9e3ca17879741d6f473db9da4686ffec4d60d8d2&token=1802903020&lang=zh_CN#rd)

这个方法其实就是让搜索引擎尽快知道有一个新网站，尽快派爬虫去爬。  

但是有些同学照着做了之后，问哥飞，为什么哥飞的网站最快可以一两个小时慢点半天也收录了，但是他的网站被收录却要一两天呢？

现在哥飞回答你，主要是两个原因：

第一个是，爬虫每天发现的新网站有很多，都会进入一个待爬列表。既然是列表就会有排序，如果你的网站平平无奇，那么自然就被排在后面了。

那么怎么能够插队呢？答案是多加几个外链。

所以我们不能只去 V2EX 一个地方发帖，最好多发几个地方，让爬虫能在多个网站都发现有你这个新网站，那么你的权重也会增加，爬出就会尽快来爬你的网站。

第二个是，你很有可能没有把网站提交给搜索引擎。不管百度还是谷歌，都有个站长后台，可以让站长提交新网站。

下面以谷歌为例，说明如何提交，如何使用。  

谷歌的站长后台叫做 Google Search Console ，记不住没关系，直接打开谷歌，用 site 语法查询，以哥飞做的 lk99wiki.com
为例，在谷歌搜索框输入 site:  l  k99wiki.c  om ，点击搜索，就能够打开下面这个页面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicticSN6t4uMNkeNxysOvdR0n2j307ESPeGPmV9tDG7slic9hHV1OmL3mfyapLbpKodic9l3YpLJJBOaA/640?wx_fmt=png)

这里我们关注两个地方，第一个是红色框地方，可以看到我们的网站是否被收录，以及收录了多少个页面，可以看到  l  k99wiki.c  om 被收录了 20
个页面。

第二个是蓝色框，就是  Google Sear  ch Console 的入口，点击后就会打开的网址如下，可以看到因为是 site:  l
k99wiki.c  om 进来的，并且这个域名在我的账号名下被验证了所有权，所以网址里有 sc-domain:lk99wiki.com 。

  * 

    
    
    https://search.google.com/search-console?resource_id=sc-domain:lk99wiki.com

如果你打开，那么就跟我这里不一样了，如果你添加好了你的网站，那么会自动跳转到你的网站的概述页面。

如果没有添加过，那么会自动显示添加资源页面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicticSN6t4uMNkeNxysOvdR0nYOL9mxic82FUFFEviaLjMiaxw2sNc4oiakYYR2lW0uXCtWSH8KaUic38zIA/640?wx_fmt=png)

我们选择左边的，按照网域验证，输入域名，点击继续按钮，如果你的域名按照哥飞之前教的方案，使用的是 CloudFlare
解析的，那么接下来可以通过授权方式，一键验证域名所有权。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicticSN6t4uMNkeNxysOvdR0nKN8pd67ibKnXk4bTiavfEqMfwfhdl8FE907V47cL6NYEQ250eFSRbcYQ/640?wx_fmt=png)

如果不是，则需要按照谷歌的要求，在域名解析中添加一条TXT记录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicticSN6t4uMNkeNxysOvdR0nymYvYAichU1UGLqfbG4MCEoLuZSAySEL9via0AFUic78nJepAA0p7BEUw/640?wx_fmt=png)

不管哪种方式，只要验证了域名所有权之后，下次就可以通过在谷歌里搜索 site:你的域名 形式来进入  Google Sear  ch Console 了。  

当然你也可以通过记住域名或者添加书签的方式来快速打开  Google Sear  ch Console 。

以 lk99wiki.com 为例，打开后会自动进入概述页面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicticSN6t4uMNkeNxysOvdR0nVpQOy84sv88cibbjW1iaG9ibx36ZSK9yfxdqCibA3iciaoBwsNkoexIsz3gQ/640?wx_fmt=png)

左侧是工具后台菜单栏，右侧是数据模块。

概述页面有效果模块，可以看到最近一段时间，网站在谷歌拿到的搜索点击数据折线图。

还有编制索引模块，可以看到我们网站有多少网页被索引，就是被收录的意思。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicticSN6t4uMNkeNxysOvdR0ncbV9x50ficHTdibiaJ3m4YVcZrC6x28fAdm623p6TuxE3saFP0aW9MGaQ/640?wx_fmt=png)

我们新站刚上线时，以上这些数据都没有，我们需要点击左侧菜单栏的站点地图页面，提交我们网站的站点地图。具体如何更好的编写我们网站的站点地图，请关注哥飞公众号，我们后面会推文专门讲解。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicticSN6t4uMNkeNxysOvdR0nfevseoZTDMnP6VWM7DUquI9E6I3p1Q197ibD5FT62T0FF9y4ECAg6Tw/640?wx_fmt=png)

如 lk99wiki 的站点地图地址为 https://lk99wiki.com/sitemap.xml
，提交上去后，谷歌爬虫就会去爬取我们提交上去的每一个页面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicticSN6t4uMNkeNxysOvdR0n9XCtMzQePpzmVkQmmZ8FlVClYKZloVlibS6OdjXN5s9KnmV9C1kTHlw/640?wx_fmt=png)

爬取完成后，就会建立索引，也就是说，我们的网页会进入谷歌搜索结果里了。

点击左侧菜单栏的效果，可以看到每天我们的网站在谷歌搜索里的表现效果。主要有点击数、曝光数、平均点击率、平均排名等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicticSN6t4uMNkeNxysOvdR0ncA7CdIOIN573j46sP0icmH1OYZTCib5YO6rbr6roShxtCcrFiazZsGF1A/640?wx_fmt=png)

这里既可以选择一段时间，查看总的数据，也可以按天选择，查看每一天的数据。通过观察每一天的数据，我们可以分析我们的网站在谷歌搜索结果的表现变化情况，有针对地进行优化。可以看这个例子
[ 群友新站上线9天拿到11030个独立访客，他是怎么做到的？
](http://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650079382&idx=1&sn=5a531d003bb4d9e2d7f52ab73e14665c&chksm=bf3f31ad8848b8bb8321721a3847dd8145c18c65367c86b9b1d22100033cc845af480594cdba&scene=21#wechat_redirect)

折线图下面还可以看到每一个搜索词的表现，根据这些表现情况，我们就可以有针对性的对这些关键字进行优化。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicticSN6t4uMNkeNxysOvdR0nXL1BZZBAPgWjdlrJnO5TzRSZib1ZOXic3YWQX9EbYGia9qibdnhRp1U9pA/640?wx_fmt=png)

当我们的网站从谷歌拿到的点击数量超过一定个数后，谷歌会给我们网站开通 Search Console Insights 权限，这个功能就很好用了。

如下图可以看到我们网站新拿到点击的都是哪些页面，点击来自于哪些关键字。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicticSN6t4uMNkeNxysOvdR0n00M9qk5WGloazrJUX9vdbFmJYPOUQCfvyIibw5ic6xTj8EtUbXl9F6aA/640?wx_fmt=png)

还可以看到最热门的网页是哪些，拿到了多少点击，都是来自于哪些关键字。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicticSN6t4uMNkeNxysOvdR0n4XaqM0dhSDBfez013iaxj2m7mK3TGmO3hVGOIQwgAokCSnZqq7vZY9A/640?wx_fmt=png)

还可以看到具体的每一个关键字的排名和拿到的点击数量。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicticSN6t4uMNkeNxysOvdR0n3iblXR5fg2mFv6e6MIY9XQG3waXHuCwDmxtJoXGWheonBHiaOj1NKBVw/640?wx_fmt=png)

开通了  S  earch  C  onsole  I  nsights
权限后，哥飞觉得最好用的就是下面这个用法了，直接在谷歌里搜索我们想优化的关键字，可以看到这个关键字最近7天在谷歌搜索结果的表现。如 lk99 wiki
这个词，哥飞的网站有2.01K也就是2000次曝光，有47次点击，平均排名是5.5。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicticSN6t4uMNkeNxysOvdR0n9IHLGKsdXbPwMqmuhNvvkPp7LaPVfUiaUglaROOAhRtqf5JBE6fMqlw/640?wx_fmt=png)

实际上这个词已经排到第二了，但上面显示的是最近7天的数据，所以被平均为5.5了。  

看下面，第一是维基百科，第二就是哥飞这个网站。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicticSN6t4uMNkeNxysOvdR0n52oJjF16BAaHCquwauxKQkBcVlqiagUXrwlVFdWuJ3AiaKkr3H50HQSA/640?wx_fmt=png)

在  Google Search Console
后台，我们需要每天关心一下右上角的通知，这些通知都很重要，谷歌在我们网站发现问题后，会发送通知，我们需要及时处理。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicticSN6t4uMNkeNxysOvdR0n8kuqH8o86jP3qYtxxsTgNoeUAGe4WvGw5b9QAwKicA7ibBjVw0MFFQrQ/640?wx_fmt=png)

如哥飞这个网站，第2条通知，就是因为哥飞修改网站内容时用了批量替换，导致某个网页的 url 写错了，没有及时发现，被谷歌收录之后，发现 404 页面了。  

针对这种页面，我们需要告诉谷歌，删除这个错误的网址，点击菜单栏，进入删除页面。点击新要求，可以提交要删除的网址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicticSN6t4uMNkeNxysOvdR0nJDlaSKu3MJg6WAyJSlZmvrWsdogUIq3jfpAyF2QS3G81icqAu0ribwog/640?wx_fmt=png)

好了今天的关于 Google Search Console 使用入门就讲到这里了，如果有任何不懂的，请加哥飞微信 qiayue ，哥飞会为你解答。  

另外，昨天关于外链建设技巧的文章 [ 分享一个容易实操且快速见效的给自己网站增加几十个外链的小技巧
](http://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650079656&idx=1&sn=4311d6953f9852ad7a9c6b38c5bfe85f&chksm=bf3f30938848b985c8fdc32b7d9ddd72a7a6d08b652b43aaffc3190f62c404446e45649dc74b&scene=21#wechat_redirect)
，还有没有领取的请尽快加哥飞微信领取小技巧。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeictmH6ZbzrmhFdgH55yNiarBAXwFK5njpE3j8ehd8M5CNnh5mX01ibDAls4gZvob7nUmwXnscEXNDm3g/640?wx_fmt=png)

  

预览时标签不可点

微信扫一扫  
关注该公众号





****



****



  收藏

