![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCVrCN60ibia55lRq8qrsbXO79ESRRlv7R5yf1iaX5HnYrFFnSgxzfzdibauA/0?wx_fmt=jpeg)

#  AI时代的聚合搜索长什么样子？哥飞帮你做出来了

原创  我是哥飞  [ 哥飞 ](javascript:void\(0\);)

__ _ _ _ _

大家好，我是哥飞。

哥飞在4月中旬就想做这个产品了，于是在即刻发了招聘帖子，开始招兵买马。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCViarzPz7yH66RcHl346ibXW5vkfKmNqbMWBETkhdPTwpWOcsOI5U14nDA/640?wx_fmt=jpeg)

之后在24号确定了人选，新同事叫莫俊，那时他还在上一家公司没离职，所以哥飞先跟他说了大概的需求，让他去调研一下技术方案。  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCVgER0cdse4laaoKdfcqgmWDicgBLGXxZZlL3ichhZx9u3791kLKK4khgA/640?wx_fmt=jpeg)

4月28日，莫俊回复说，找到了一个类似产品 Chathub，哥飞说那是即刻内部孵化产品，我们两个产品类似但其实也不一样。  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCV3IibM8dw0Rx47TF5SickVoI1njJRGITXd60UeibhLTAFwUeFbUWdtzsEg/640?wx_fmt=jpeg)

4月29日，莫俊说实现了一个最简Demo，  当时做成点击浏览器的插件图标就显示一个输入框  ，和几个AI搜索产品让你勾选。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCV34DTA0bLib0W93c8w4xf8lLylDuA5FENpgIb2gKrfwbWwxMgwOgD9FA/640?wx_fmt=jpeg)

在输入框输入问题后，点击搜索按钮，就会打开多个新标签页，帮你自动把问题发给多个AI搜索。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCVSU40t2jTrQTXeicTCOVNn8BIsoShmaftzOhomD0ic1bg8nGJdqZXOBfg/640?wx_fmt=jpeg)

哥飞说技术走通了，但是多个标签页需要切换才能看到结果，不方便，是否可以做到同一个页面里去。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCVsHk4WaictlicibGsqLezz3wchIJicX6hjkvIzhh1062jCTbxRWPVCxluZA/640?wx_fmt=jpeg)

5月16日，莫俊正式入职了，当天下午，他就搞了个新的Demo出来，说可以用 iframe 打开多个不同的AI搜索了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCVHcr9bjiaQuRWXrqhDQyr44OFNib1gd7ZibribPxpGe2icN5HR5w9rCq6EkA/640?wx_fmt=jpeg)

之前都是远程沟通，所以还能找到一些聊天记录来还原我们的一些版本变化历史和开发过程。

自从莫俊入职后，有问题哥飞都是直接喊一嗓子，所以仅仅从聊天记录已经无法还原历史了，我们就略过中间的各种修改吧。

5月31日，哥飞觉得 iframe 方案始终不稳定，而且相当于偷了各个AI搜索的流量，所以跟莫俊说，改成用多窗口模式。  

当天下午莫俊就测试出来了，多窗口是可以的。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCVa0Nw7Iiat5KrbtIukem4W2xlqkiaKldkNPib4EWeKJnVc6KwbJKHK9SbA/640?wx_fmt=jpeg)

到了6月8日，其实已经出来了一个基本能用的版本了，但其实还有很多小细节没处理好，所以哥飞不断的在测试，找问题。  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCVCv4NDZFiaNj4r3oLBiaz6w5VlHX5Gov0wF9t5eZWDibsMKPHXHWdMNatg/640?wx_fmt=jpeg)

修改之后，又提交到谷歌插件开发者后台审核，不过因为各种原因，特别是用了比较多的权限，如修改新标签页等等，所以一直被谷歌打回。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCVGiag7BxO6Y45dojVrInc6l0Lma4HJhqic5EMyBOefGdYzdggfynt8JMQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCV3qEsg5pEc66WCbFNpHfSO4GPrVJ6JZkqlOBphL0L6DovibJcjiczZzMw/640?wx_fmt=png&from=appmsg)

终于在  前天，也就是7月9日，1.2.6版本审核通过了，就是现在大家看到的样子。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCVf2TVwpOY2XpEicv5cLCoV4AkhMaxKBofLB1uB3dxy0rXvmK5K4znGhA/640?wx_fmt=png&from=appmsg)  
---  
  
  
虽然依然还是有一些小Bug，但至少主体功能是能用的，所以就先分享给大家使用了。  

插件地址是：  
https://chromewebstore.google.com/detail/seekall/cmfgomdhmknhbgbdnagkijkdaifnecma  
  
官网是：  
https://seekall.ai/

插件页面看到的几张图片是哥飞直接用 Canva 制作的，有点丑。

于是哥飞又找设计师制作了几张图片，就在下面，大家可以看看，的确是比哥飞自己做的漂亮多了。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCVnE5GobY3PywSHJslB3nTUtf5nUSwrqenXsfQDLQWup3jqafws9BwYw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCViahpdEgzVmktuqicYJl6H091cYayqdLWrzgvo8XtvuWz9iaTq9RBJmgYA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCVz5zab6I5fiaRDIpdRvXic12rB2PX28rHiba29j2kkyEG2u42klkWWHGKQ/640?wx_fmt=png&from=appmsg)

那么 SeekAll 这个插件到底是干嘛的呢？

其实功能很简单，就是整合国内外的各个AI搜索和传统搜索和一些社交媒体搜索入口，让你可以在这个插件里一键打开多个搜索，在多个窗口里对比搜索结果。

One Click, Seek All Results for You.  

先有了上面这句 Slogan，后面才有了 SeekAll 这个名字，哥飞花费“  巨  资  ”购买了 SeekAll.ai 和 AllSeek.ai
两个域名。

为什么要同时打开多个窗口查看呢？  

大家都知道，AI会有幻觉问题，或者有一些搜索因为数据源问题暂时还没有答案，所以同时看多个AI搜索的回答就很有必要。

举例，哥飞想要问“SeekAll是什么”，只需要打开插件，在输入框里输入问题，敲击回车键或者点击搜索按钮，就可以打开上一次使用过的三个搜索。  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCVs7jjbB4KBjsZD4JMxr2u47sFtc9Zn9cYqd663ouNiaVjwZh6lpwjZYg/640?wx_fmt=jpeg)

瞬间，三个窗口就打开了，可以看到，谷歌的搜索结果最快显示出来，但是只是检索没有回答，而Perplexity就很好的帮助哥飞回答了问题，至于腾讯元宝，因为数据源主要是公众号，所以在我写文章时暂时回答都是错误的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCVs7eDxuWZNibrgklgvViaHDT7oJCGgW8oEquz7zKibkRoHzUDZ8vlerHHg/640?wx_fmt=png&from=appmsg)

相信等哥飞这篇文章写完了发布出去之后，再次使用腾讯元宝，就能够得到准确的回答了。

SeekAll 还有个隐藏能力，一键追问。

对于支持追问模式的AI搜索，直接在SeekAll的黑色浮窗里输入问题，就可以一键追问。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCVaktxtg6SLNmr13GL62sJXXCRBB7rhxBHEKlnGU9wBgxomZtje5uEmQ/640?wx_fmt=png&from=appmsg)

目前 SeekAll 支持的搜索引擎还是很多的，大家可以根据自己的使用习惯去选择。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicvvynJa2lDsT2DtwHs2lzCVZ8anLNRVibfDNEGTLoF0Y2499Mw0CLMOPfnV9fwQ6Yia0Js84uYNrmqg/640?wx_fmt=png&from=appmsg)  
---  
目前最多只支持同时选择3个搜索，原因是目前 SeekAll
使用平铺方式显示多个窗口，我们测试发现，超过3个窗口显示效果就没有那么好了，所以暂定最多只能选择3个搜索。  

后面我们的版本，我们准备改成让大家可以在设置界面自定义最多窗口数量。  

大概功能就是这些了，大家都可以试试，也许还能发现一些小功能。  

哥飞可以承诺，这个插件本身是永久免费的，因为对于哥飞来说，这个插件没有任何成本。

并且我们并没有偷各个AI搜索的流量，我们直接把流量还给AI搜索引擎。

我们虽然不提供AI搜索，但我们是AI搜索的入口，希望把流量带给各个AI搜索。

好了，以上就是今天的文章，希望大家能够喜欢 SeekAll ，有任何问题，欢迎找哥飞反馈。  

预览时标签不可点

微信扫一扫  
关注该公众号





****



****



  收藏

