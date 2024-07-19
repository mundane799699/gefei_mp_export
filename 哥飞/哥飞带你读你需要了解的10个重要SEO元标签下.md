![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeicvE3RtPz97Ed6cGfC2jwdH4JwyNzDibcuW8jaoucOPpAZ4RptsjZdbSibKkWickicrzSsMlUxvYW8EdOA/0?wx_fmt=jpeg)

#  【哥飞带你读】你需要了解的10个重要SEO元标签（下）

原创  我是哥飞  [ 哥飞 ](javascript:void\(0\);)

__ _ _ _ _

大家好，我是哥飞。  

前天开始，哥飞带着大家读 SearchEngineJournal.com
上的文章：https://www.searchenginejournal.com/important-tags-seo/156440/

10个标签已经介绍了6个了：  

  1. 《 [ 【哥飞带你读】你需要了解的10个重要SEO元标签（上） ](http://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650082107&idx=1&sn=62f664473462228f5d03fb10d29ffa32&chksm=bf3f3a008848b3166bce42c86fdd070cead41af4df106fabd7f490ab6cbfcc38683f42183a05&scene=21#wechat_redirect) 》   

  2. 《 [ 【哥飞带你读】你需要了解的10个重要SEO元标签（中） ](http://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650082113&idx=1&sn=bedf2b5a87ac6cc0d4aee2b60febc61f&chksm=bf3f3a7a8848b36c90819dc236a7ee36eae6b00d0a4fa04e551ac5c171f42631e06ef1bd85cf&scene=21#wechat_redirect) 》   

  
今天继续介绍剩下的4个。

** 七  、  canonical  标  签  **

如果大家经常使用 Detailed SEO Extension 就会发现，会检测这个标签。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicvE3RtPz97Ed6cGfC2jwdH4jxMc1mr7ic2w3uHqh3krkQvoaJ8GgIc2iaEu1icLfDpT5LqELNqvEuGHQ/640?wx_fmt=png&from=appmsg)
插件地址：  https://detailed.com/extension/  
类似且更好用插件 https://aitdk.com/zh-CN/extension/

这个标签作用是什么呢？哥飞之前在《 [ 如何给一个已经上线的网站出SEO改造建议
](http://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650080016&idx=1&sn=dbd4c56dc47b6bb6cf3fd848950810ac&chksm=bf3f322b8848bb3d683e505bf266916c0fb6725039ea050557b146525f02266a15e5eda9795a&scene=21#wechat_redirect)
》和《 [ 【5800字长文】从网站站内优化到部署上线再到推广运营一篇文章让你学明白
](http://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650080101&idx=1&sn=477191907e388aff6df3f16c915056d8&chksm=bf3f325e8848bb48e682193cc0bef2c42e25900fb2ca02987b5a854892bb3cb88c540e9492b6&scene=21#wechat_redirect)
》文章中都提到过，是用来告诉搜索引擎，当前网页的规范网址是哪个的。

举个例子就好理解了，假设我的网址是 https://abc.com/ ，但是搜索引擎的爬虫可能会在 reddit 找到一个链接，网址是
https://abc.com/?r=reddit 。

在搜索引擎眼里，这是另一个网址了，但是网站返回的页面内容却跟  h  ttps://abc.com/
是一样的，搜索引擎就会疑惑，这个网站为什么有那么多重复网页呀。

为了不让搜索引擎有疑惑，我们在 abc.com 网站首页的 html head 里加上如下代码：

  * 

    
    
    <link rel="canonical" href="https://abc.com/">

这样不管爬虫从  h  ttps://abc.com/ 进入，还是从  h  ttps://abc.com/?r=reddit 进入，还是从  h
ttps://abc.com/?r=ph 进入，都知道你这个网页真实的规范的网址是  h  ttps://abc.com/ 。

这里特别注意的是，你的真实网址是什么，就应该返回什么，而不是整个网站所有页面都统一返回首页的地址，这里写错了后果会很严重。  

举例，网站博客的某篇介绍如何搞钱的文章应该返回如下代码：

  * 

    
    
    <link rel="canonical" href="https://abc.com/blog/how-to-make-money">

  
还有一点很重要，假设你在多个不同的外部网站上都有反向链接，但是链接里加了跟踪参数，如上面我们提到的 r=reddit 和 r=ph ，如果不设置
canonical 标签，那么谷歌会认为有多个网址得到了反向链接，权重就分散到各个带参数的网址里去了。

而如果  设置了  canonical 标签，  谷歌就会把所有这些外链的权重都汇聚到你设置的规范网址去。

举个例子，你写了一篇如何搞钱的文章，想拿下“How to make
money”这个关键词的排名，你把文章投稿到各个不同的平台，并且留下来原文链接，并且你的这篇文章还被很多别的博客转载了，他们转载时也给你加了原文链接，但是所有这些链接都加了跟踪参数，如果不设置
ca  nonical 标签，你的这些外链就浪费掉了，权重分散到各个带跟踪参数的链接里去了。而设置了  ca  nonical
标签，则全部权重会汇聚到你指定的唯一规范网址里，你的排名就更容易上升。  

  

** 八  、  Schema Markup 模式标记  **

这个其实就是哥飞之前在《 [ 10种谷歌结构化搜索结果样式介绍及实现方法，最骚的是第9种
](http://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650079358&idx=1&sn=8633a276dd94efc971cc2ca2239a34d6&chksm=bf3f31458848b853b74dfe41cebfc4da5c639a3519bf20bac7d3888bee99d27819c2cb95a999&scene=21#wechat_redirect)
》介绍过的一些效果，当时哥飞文章里说的是让谷歌自动去抓取结构化数据，但其实
要想呈现结构化的搜索结果，最好的办法是按照谷歌的帮助文档要求去主动给谷歌提供结构化的数据，具体可以看这里：

https://developers.google.com/search/docs/appearance/structured-data/intro-
structured-data?hl=zh-cn

谷歌官方也提供了一个结构化数据标记辅助工具：  

https://www.google.com/webmasters/markup-helper/?hl=zh

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicvE3RtPz97Ed6cGfC2jwdH4RYodjDjGu2pjicx3G1O6Zibs9QPeA3VnsdiaJHT6ttuCBAlgDccnvMrzg/640?wx_fmt=png&from=appmsg)

使用步骤很简单，输入要标记的网址，选择标记的数据类型，点击网页选择内容然后标记数据。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicvE3RtPz97Ed6cGfC2jwdH4AOnKvazNO5UzdFicIejFUKWtlP7YZj8HHzIPCchMXl08zECSNlUdXXA/640?wx_fmt=png&from=appmsg)

最后生成的 JSON-LD 数据代码如下，把这些代码添加到网页html 的 head 中即可：  

  *   *   *   *   *   *   *   *   *   * 

    
    
    <!-- 由 Google 结构化数据标记助手生成的 JSON-LD 标记。--><script type="application/ld+json">{  "@context": "http://schema.org",  "@type": "Product",  "name": "Listen Notes",  "image": "https://wxcdn.qabot.cn/plugin/img/1280.duck_3.png",  "description": "最好的播客搜索引擎和数据库，包含所有播客和剧集。"}</script>

**九、Social Media 社媒元标签**

社交媒体元标签可以控制你的网页被分享到各个社交平台之后展示的效果，主要用来控制标题、网址、配图等信息。  

Open Graph 最初是 Facebook 提出来的，并且在 FB 里进行了支持，后来 Linkedin 也开始支持，Twitter 搞特殊，搞了个
Twitter cards 。

最主要的  Open Gr  aph 标签有以下几个：  

  *   *   *   * 

    
    
    og:title - 控制显示的标题og:url - 控制网址，如可以增加跟踪参数og:description - 控制描述og:image - 控制图片

给大家看一下 Hix.ai 的  Open Gr  aph 代码：

  *   *   *   *   *   *   *   * 

    
    
    <meta property="og:title" content="HIX.AI: Your Most Powerful, All-In-One AI Writing Copilot"/><meta property="og:description" content="Generate high-quality copies for ads, emails, blogs, and more in seconds with HIX.AI, the most powerful, all-in-one AI writing copilot on the market."/><meta property="og:url" content="https://hix.ai"/><meta property="og:type" content="website"/><meta property="og:image" content="https://hix.ai/featured-images/hix-ai-the-most-powerful-all-in-one-ai-writing-copilot.jpg"/><meta property="og:image:alt" content="The Most Powerful, All-in-One AI Writing Copilot."/><meta property="og:image:width" content="800"/><meta property="og:image:height" content="600"/>

在  Detailed SEO Extension  可以检查是否配置正确：  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicvE3RtPz97Ed6cGfC2jwdH4otoPiaJwzME2emUzqdQwHMfD1NaUTU1A8DdOCkkJq08rUI30raEjR1A/640?wx_fmt=png&from=appmsg)

如果我在 Facebook 发帖时粘贴了 Hix.ai 的网址，就会显示如下效果：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicvE3RtPz97Ed6cGfC2jwdH4OdlL4Tu57O8Z7yoaOExR7mPhuTfiaOQmiayZaUSNGGmImqL3V6bWLz0g/640?wx_fmt=png&from=appmsg)

Tw  itter  cards 有些不太一样，具体看下面文档：  
https://developer.twitter.com/en/docs/  twitter-for-
websites/cards/guides/getting-started

**十、Viewport Meta Tag 视口元标签**

Viewport 元标签通常用来配置我们的网页在不同大小屏幕下的缩放和显示方式，简单说，就是可以用来适配不同大小屏幕的显示效果。

在《 [ 【哥飞解读】2024年谷歌算法排名因素变化
](http://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650081965&idx=1&sn=c011ca451d92007bbbdc6325c9ea018f&chksm=bf3f3b968848b280abf0a8d0311683fe5ffd7d5ede55b3cb9840e8fa073bd32a334de55703d8&scene=21#wechat_redirect)
》文章里我们说了，移动端友好占谷歌排名因素的5%权重，所以适配手机和平板电脑对于SEO也很重要。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicvafrBgBQa9ySp68Z72I4VOKlB0HK4JpNbFv7SbrPd2kwBRmUULCDkyOnndj4ibfB86n8UUDSAQKAw/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

通常代码如下：

  * 

    
    
    <meta name="viewport" content="width=device-width, initial-scale=1"/>

“width=device-width”将使页面与设备独立像素的屏幕宽度匹配，“initial
scale=1”将建立CSS像素和设备独立像素之间的1:1关系，考虑屏幕方向。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicvE3RtPz97Ed6cGfC2jwdH4AMFWJfhZD6nGFnIib9Xqal0tU6sdCh7CYv6icuBEjtr2GGuTk1XI1m0g/640?wx_fmt=png&from=appmsg)  

上面可以看到对比效果，左边是不设置  Viewport ，右边是设置，明显右边可以更好的适配手机端的显示效果。  

Viewport 标签虽然与排名没有直接关系，但是通过上面的分析，我们发现是会间接影响排名的，所以需要去配置好。  

到此为止，哥飞把原文介绍的10个标签都按照哥飞自己的理解给大家介绍了一遍了。  

很多时候做SEO并没有一击必杀的绝技，靠的就是在各种小细节上面不断优化，做得比别人好，最后所有的效果累积起来，你的排名就比别人更高。  

想要跟着哥飞学SEO，做网站赚美元吗？

  

欢迎加入哥飞的付费社群“哥飞的朋友们”。  

  

社群目前暂时是微信群形态，有一个配套的网站，已上线第一版，社群内朋友可见。

  

社群主要面向技术开发者、产品经理、设计师等人群，大家一起讨论独立开发、出海产品、流量获取、流量变现等话题。

  

社群讨论的话题主要是围绕着网站来的，用网站来承接流量，然后变现。

  

那么就要考虑做什么网站，所以需要去挖掘需求。

  

然后去搞流量，可以是SEO，也可以是发帖宣传推广，还可以是付费软文。

  

有了流量之后就得考虑如何变现，可以是广告变现，也可以是联盟导购，更可以直接向用户收费。

  

社群目前超过1000人，新的一期开始了，这期哥飞将带着大家实战，每个月都会安排任务，推着大家前进，让大家能够赚钱。

  

目前888元优惠价已经结束，前两天已经正式涨价为999元了。

  

社群按照365天计时，也就是你今天加入后，明年今日到期。

  

前两期讨论很活跃，行动很迅速，大家已经做了上百个产品了。

  

有的几人小团队已经用几个月时间从零开始做到了月收入4万美元以上，还有的单人实现了月收入几千美元。

  

这个社群7月2号开始运营的，到今天7个多月时间里，主要讨论了以下话题：

1、建站基础，如何快速做一个网站；

2、SEO基础，如何优化网站；

3、推广基础，如何宣传推广网站；

4、运营基础，如何运营好一个网站；

5、Adsense基础，如何靠谷歌Adsense赚广告费；

6、一些工具使用经验分享，如Semrush分析别的网站流量和出入站链接，Similarweb如何看流量；

7、基于Semrush、Similarweb等工具，如何去发掘新需求，发现新网站；

8、实战经验，如何去抓住新词热词做网站，从搜索引擎获取流量。

  

以上所有讨论都沉淀到了社群配套网站 web.cafe 上，所以第三期大家一进群就可以看到前两期的精华内容，以及其他更多相关话题。

  

欢迎加哥飞微信 qiayue 加入社群大家一起出海赚美元。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicv24nb20ZrM7niaIBxv5QynWqOtclGh4ApYjVM5exp1niaK9pOLIOswYu2jU0zczI2Hx2bdfAo1Fwow/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

微信扫一扫  
关注该公众号





****



****



  收藏

