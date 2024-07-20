![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeicubcksMbFZopPx8Lok6XT9zfbecOkzG13YRoWtMuuCymxWmsnhz3FZ0vH73wNYInyk0UGBicLW8KDA/0?wx_fmt=jpeg)

#  【哥飞SEO教程】再聊 Canonical 标签，用好有好处，用错有坏处，需要小心用

原创  我是哥飞  [ 哥飞 ](javascript:void\(0\);)

__ _ _ _ _

大家好，我是哥飞。  

关于哥飞介绍可以看这里：  [ 哥飞是谁，哥飞在做什么事情，在哥飞公众号大家可以看到什么内容
](http://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650082843&idx=1&sn=50add036fed1ac78f2c71887bbedb990&chksm=bf3f3f208848b63647147b8c3328bfe12497d281c9c4257d548e83b095b6db33d29e2f6d03e6&scene=21#wechat_redirect)  
关于哥飞社群可以看这里：  [ 是时候给大家好好介绍一下哥飞的社群了，毕竟刚被二十年站长大佬夸过
](http://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650082450&idx=1&sn=b33f52d905edd76782d85eb06163f312&chksm=bf3f3da98848b4bf8214219c775293b397bdda48f14975f88e55a5bbe7efa75e4b11d93010a5&scene=21#wechat_redirect)

最近哥飞发现还是有很多朋友没有理解 Canonical 标签的正确用法，所以今天单独写一篇文章来详细讲讲。  

哥飞在以前的文章也讲过这个标签，感兴趣可以点进去看：  
1\.  [ 如何给一个已经上线的网站出SEO改造建议
](http://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650080016&idx=1&sn=dbd4c56dc47b6bb6cf3fd848950810ac&chksm=bf3f322b8848bb3d683e505bf266916c0fb6725039ea050557b146525f02266a15e5eda9795a&scene=21#wechat_redirect)  
  
2\.  [ 【5800字长文】从网站站内优化到部署上线再到推广运营一篇文章让你学明白
](http://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650080101&idx=1&sn=477191907e388aff6df3f16c915056d8&chksm=bf3f325e8848bb48e682193cc0bef2c42e25900fb2ca02987b5a854892bb3cb88c540e9492b6&scene=21#wechat_redirect)  
  
3\.  [ 【哥飞带你读】你需要了解的10个重要SEO元标签（下）
](http://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650082126&idx=1&sn=5a4d4b231eec5ac66ccb9ffa64382025&chksm=bf3f3a758848b363fc6a402e40840001f3bb8363c76be5658f3296d62fbb4d59dcd62d0ac063&scene=21#wechat_redirect)  
  
4\.  [ 推荐一款好用且免费的SEO插件，哥飞天天都在用
](http://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650082258&idx=1&sn=e5d0a8e9a89c3793013d97ba53496c9c&chksm=bf3f3ae98848b3ff9bbdd5270be5b0a44ef41df81a89307190ff927c22f5bfde00f97ff76dd1&scene=21#wechat_redirect)  
  
5\.  [ 【哥飞评站】AI贴纸生成网站 StickerBaker 的SEO评测报告和改进建议（4000字）
](http://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650082285&idx=1&sn=20faa4fbebc68bcc43d82a322bd86e6f&chksm=bf3f3ad68848b3c04f7ba8b55bb9568869788dfdf573458c85485577b343b10261a1c12c757e&scene=21#wechat_redirect)  
  

关于 Canonical 的教程文章，也可以看看下面这些：  
1\. 什么是规范化  
https://developers.google.com/search/docs/crawling-
indexing/canonicalization?hl=zh-cn  
  
2\. 如何使用 canonical 及其他方法指定规范网址  
https://developers.google.com/search/docs/crawling-indexing/consolidate-
duplicate-urls?hl=zh-cn  
  
3\. Semrush 的 Canonical 教程  
https://www.semrush.com/blog/canonical-url-guide/  
  
4\. Ahrefs 的 Canonical 教程  
https://ahrefs.com/blog/zh/canonical-tags/

下面，哥飞会基于自己的理解，给大家介绍  Canoni  cal 。  

**一、为什么要有 Canonical  **

先说结论，Canonical 目的是为了解决  重复网址  问题，注意，哥飞说的是重复网址，而不是  重复网页  哦。  

同一个网页，有可能多个域名都可以访问，最典型的就是 www 域名和裸域名都能够访问，这就导致一个网页有多个网址。

如果是子目录，有可能 /abc/ 和 /abc/index.html 或者 /abc/index.php 都能够访问，于是一个网页有更多网址。

这还不算完，这些网址后面又可以加各种各样的参数，还会导致更多的网址出现。

哥飞举例例子给大家更好理解。

假设域名是 gefei.vip ，同时解析了 www.gefei.vip 和 gefei.vip 。

注意，这里哥飞只是用来举例，实际更规范的做法是选定一个域名作为主域名，然后把另一个域名通过3  01跳转到这个主域名。  
如哥飞习惯选择 gefei.vip 为主域名，然后把 www.gefei.vip 301 跳转到 gefei.vip 。  
注意，如果是大网站，为了防止 cookie 泄漏，一般是把 www.gefei.vip 作为主域名，然后把 gefei.vip 用 301 跳转到
www.gefei.vip 。

假设目录是 /shequn/ ，后端用的 php 写的， 也就是 /shequn/ 和 /shequn/index.php 都能够访问。  

假设张三和李四都在自己网站上推荐了哥飞社群，都带了来源参数，参数名称还不一样，一个是 ref=zs ，一个是 via=ls 。  

那么总共可能会有以下这么多个网址被使用：  

https://gefei.vip/shequn/  
  
---  
https://www.gefei.vip  /shequn/  
https://gefei.vip  /shequn/index.php  
https://www.gefei.vip  /shequn/index.php  
https://gefei.vip  /shequn/index.php?  ref=zs  
https://www.gefei.vip  /shequn/?  v  ia  =ls  
还可能有更多……  
  
  
上面哥飞只列出了部分情况，实际可能会有更多。  

而这些看起来不一样的网址，其实都是社群首页，返回的 html 是一样的。

那么在搜索引擎的眼里就会很奇怪，为什么会有这么多的  重复网页  。  

注意，哥飞这里用了“  重复网页  ”，而在前文用了“  重复网址  ”，其实是视角不同。

在我们自己眼里，知道这些网址其实是同一个网页的不同网址，所以是“  重复网址  ”，而在搜索引擎眼里，这就是一些“  重复网页  ”。  

哥飞这里再展开一下，除了上面这个原因会造成重复网页，如果你的代码是前端渲染的，也会造成重复网页，具体可以看这篇文章《  [
【哥飞SEO教程】如果不想要谷歌给的免费流量，你就用前端渲染吧
](http://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650082690&idx=1&sn=5c053eecd24c0f0b156cd7fcb9869a02&chksm=bf3f3cb98848b5af08fc61244ffcda601fbf0cd3891c9da0624089b2408a68e2a0e840bf9bfb&scene=21#wechat_redirect)
》。  

为了让站长把最规范的一个网址告诉搜索引擎，谷歌等搜索引擎就开始使用 Canonical 标签。  

** 二、  Canonical 是什么，有什么用  **

还是拿上面哥飞举的这个例子来说，我想用的规范且唯一网址是：  
https://gefei.vip  /shequn/

那么就可以在网页 html 的 head 中增加如下一行代码：  

  * 

    
    
    <link rel="canonical" href="https://gefei.vip/shequn/">

这样不管别人用哪个网址访问社群首页，Canonical 都不变，都是：  
https://gefei.vip  /shequn/

所以 Canonical 的正确用法就是用来指定每一个网页的规范化URL到底是哪个。

** 三、多语言时 Canonical 怎么写  ** ** **

假设你的网站有多种语言，如同时支持中文和英文，网址分别是：

中文  
|  https://gefei.vip  /shequn/  
---|---  
英文  
|  https://gefei.vip  /en/shequn/  
  
  
这个时候就要注意了，在英文页面的 html 里， Canonical 就要这样写：  

  * 

    
    
    <link rel="canonical" href="https://gefei.vip/en/shequn/">

  
看到了吗？

Canonical 需要如实反映当前网页的真实网址。  

千万千万不要不管什么语言都写死成同一个网址。

哥飞还看见过有些人全站任何网址的 Canonical 都写成了首页，这也是不对的，是对 Canonical 没有理解到位才会导致的错误。

** 四、Canonical 有什么好处？  **

还是拿上面的例子来说，张三和李四都给了外链，虽然给出的链接地址不一样，但是如果我们在页面里设置了正确的 Canonical
，那么搜索引擎就能够把这些不同网址的权重都汇聚到 Canonical 指定的网址里去。

好了，以上就是今天的文章，欢迎加入哥飞的社群学习更多SEO相关知识，一起出海做网站赚美元。

如果你是程序员，那么这绝对是你不能错过的一个社群。  

2024年，哥飞想达到这个目标：  
帮助20000+程序员了解出海；  
帮助2000+程序员参与出海；  
帮助600+程序员能够月入1000+美金；  
帮助100+程序员能够不再上班养活自己；  
帮助10+程序员建立自己的AI工厂。

其实目前哥飞已经有好几个朋友建立自己的AI工厂了，如Gary、AUDI、Alaadin、二两等。也有好多个朋友可以不上班就养活自己了，如Banbri、BingNi等。  

现在，哥飞一边开着自己的AI工厂，一边  带着大家一起出海赚美元，《 [ 【养网站防老】每个人都要有自己的小果园，今天请为你的果园种下第一棵小树苗吧
](http://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650082415&idx=1&sn=8b725d7238143cdf7b0992b6f7835b57&chksm=bf3f3d548848b442dafc0a5fa379cf90be1749a82d62c2371d2140fed2cc5bbc86e3430e2d6f&scene=21#wechat_redirect)
》。

哥飞会用自己实践总结出来的最新的经验来教给大家，如何挖掘需求，如何实现需求，如何做好SEO，如何运营推广，如何变现赚美元。  

给  大家看看已经在社群里的其他朋友怎么评价的吧。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeictfJNjePhchkZYLuBwKPcJl2yZPhaRV7VWHg1Fe9tIs05v9QTFBq1oCZjVn9qB08LszWxrFibHHeMQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeicsc3DNibdfcSLWyEGZBZSXSUbPuaibAobt9LPMO3wygibBF21OuH0mCYZU6Hn3qgz5Zvxml98F9dKnrQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeicu0ohJ2AspibworASbayGLjNicts7f15fE789SLz4EI2yZgzHicU6KCsqDNVgkpOwdulS8sGWaSXSRVg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

  
那么这到底是一个什么样的社群呢？  

  

一句话介绍，这是一个教你  出海做网站赚美元  的社群。  

  

哥飞知道，肯定会有人说，教人赚钱最赚钱。  

  

但是，哥飞这个社群，你学了，是真的能够赚美元的。

  

因为哥飞不是教你做一个类似的社群去赚别人的钱。  

  

哥飞教你怎么挖掘需求，怎么搞SEO，怎么搞流量，怎么把流量变现。

  

或者说，哥飞其实是在给大家做微培训。

  

如果想更多了解社群，或者想加入社群，请加哥飞的微信 GeFeiSvip 。  

  

当然，即使你现在不加社群，也可以先关注哥飞的公众号，多看几篇文章，你会有收获的。  

  

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeictfJNjePhchkZYLuBwKPcJlnZQYrN8QibDK3jrvycyWs3MDicu1ibntWVBViahQBibHCN9DguLc15AicbBg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

  

预览时标签不可点

微信扫一扫  
关注该公众号





****



****



  收藏

