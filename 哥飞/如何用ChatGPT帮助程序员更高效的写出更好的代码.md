![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/LBrX00GQeictcibXFtyCyz4cbprgjicfsdEzrArCJgqGTEVudd15O76YibGxHQ9VokDkmpypoYolKgzCOia2ug6V7gg/0?wx_fmt=jpeg)

#  如何用 ChatGPT 帮助程序员更高效的写出更好的代码？

原创  我是哥飞  [ 哥飞 ](javascript:void\(0\);)

__ _ _ _ _

ChatGPT 是什么，以及如何使用 ChatGPT，本篇文章不介绍了，稍微搜索一下就能找到很多有用的信息。

今天这篇文章，我们来说说，如何用 ChatGPT 帮助程序员更高效的写出更好的代码。

ChatGPT很强大，有很多应用场景，相信这几天大家看得足够多了，这里不多做介绍。

让我们进入正题，一边看例子，一边看 ChatGPT 如何帮我我们编程。

十年前，哥飞做了一个在线扫描未注册域名的工具网站，名叫秋玉米，核心代码其实就是用 socket 连接域名的 whois
根服务器的43端口，发送域名，查询域名信息，如果有返回说明域名已被注册，返回找不到说明域名尚未被注册，或者是被保留域名。

当年很多人问哥飞，如何实现又快又稳定的查询域名是否注册，到底用的哪个接口，哥飞笑而不语。  

今天，哥飞问了 ChatGPT，AI 居然很快就给出来了正确答案，而且给出的示例代码是直接能运行的。  

![](https://mmbiz.qpic.cn/mmbiz_png/LBrX00GQeictcibXFtyCyz4cbprgjicfsdEVBDDwAMfJ8hRpVAPEUzclbT5ek3N0arVx0TxMoxlKDpCKdJ82kiaHTw/640?wx_fmt=png)

你看，我的提问里，故意没提 43 端口，也没提 .com 域名的 whois 根服务器到底是哪一个，也没有告诉 AI 要怎么判断域名是否被注册了，但是 AI
给出的示例代码把这些都考虑到了。  

![](https://mmbiz.qpic.cn/mmbiz_png/LBrX00GQeictcibXFtyCyz4cbprgjicfsdEAOFAh5joGibdxHlbgeX3mwa7v2hZuOlRJM3kYZhco8SClicmUBQYRdoQ/640?wx_fmt=png)

我把代码复制下来，没有任何其它改动，仅仅是增加了一行 var_dump 语句来打印返回结果，方便大家看清楚判断域名是否注册的原理。  

![](https://mmbiz.qpic.cn/mmbiz_png/LBrX00GQeictcibXFtyCyz4cbprgjicfsdEfHoc9BPCc7MoIJtCFCLSH8DowTHJ8ChZEerO4GUgt7o9BkxKfrTubA/640?wx_fmt=png)

执行代码，没有Bug，没有报错，直接给出来了我要的结果，域名 abc456.com 已经被注册了。

恐怖如斯！  

我当年可是通过多番搜索查各种资料，才搞清楚了查询未注册域名的原理，现在 AI 直接一问就给出答案来了。

穿越修仙小说里才有的住在戒指里的有问必答老爷爷，现在人人都可以拥有了。  

不需要穿越，不需要主角光环，只需要 ChatGPT 就足够了。

再来一个例子，下午，同事问哥飞，如何判断一批几万个手机号的运营商，我直接把问题扔给了ChatGPT ，得到了满意的回答。  

![](https://mmbiz.qpic.cn/mmbiz_png/LBrX00GQeictcibXFtyCyz4cbprgjicfsdEyg8abiaPBBEdhqM6ZMaL5AsDQWd0A1LsibupVQJ0iaHbwKa6QjysZYQFQ/640?wx_fmt=png)

我们还可以向 ChatGPT 问编程语法使用经验，如如何用JS实现获取数组最大值？

![](https://mmbiz.qpic.cn/mmbiz_png/LBrX00GQeictcibXFtyCyz4cbprgjicfsdEkIY1Qvx0jyY02IjXBmw5apv5CT3WY9oJwribhicopW5ecvzBMqQeD01g/640?wx_fmt=png)

用 ChatGPT 可以省去翻看查找文档的时间，请看下面几个例子。  

你可以简单的问 ChatGPT  某个  库  的用法，  如  moment.js 如何获取时间戳。

![](https://mmbiz.qpic.cn/mmbiz_jpg/LBrX00GQeictcibXFtyCyz4cbprgjicfsdEibyiav9nCsafqpFVw1v1hlUTCAJRL6rSKaDBZeiadibcbR0ZpAb3VXD3vQ/640?wx_fmt=jpeg)

如何用 moment.js 获取一个指定时间戳的6天前时间戳，ChatGPT
不仅给出例子来了，还一步一步讲解如何实现，甚至在最后告诉你可以用一句话连起来写。

![](https://mmbiz.qpic.cn/mmbiz_png/LBrX00GQeictcibXFtyCyz4cbprgjicfsdEp0meH4SJiccCxQ4QicRQxzjuyGQ148k8byJ6W9JNLduvBtQVglad4htQ/640?wx_fmt=png)

ChatGPT 不仅能理解6天前，也能理解一周前。

![](https://mmbiz.qpic.cn/mmbiz_png/LBrX00GQeictcibXFtyCyz4cbprgjicfsdEcG0F7rcv4ET8WsuibevZq1XINakROeMicn67VfZDXqfAOicibItEfYdic9g/640?wx_fmt=png)

你还可以直接提要求，让 ChatGPT 帮你写程序，如下面这个例子。  

![](https://mmbiz.qpic.cn/mmbiz_jpg/LBrX00GQeictcibXFtyCyz4cbprgjicfsdEjjTODClnG4anL4rqib3U5On5SCjgMBcamcFDWoL8cdHa8Xo1ibicE7c1Q/640?wx_fmt=jpeg)

还可以问 ChatGPT 如何调用 ChatGPT 的接口实现连续对话。

![](https://mmbiz.qpic.cn/mmbiz_png/LBrX00GQeictcibXFtyCyz4cbprgjicfsdEoWbINQp1DoiayhIRJVoqOusTUQuz87qm9LyH2ckmXX92o6Jv6r79mFQ/640?wx_fmt=png)

当你编程没思路时，还可以向 ChatGPT 问思路。

![](https://mmbiz.qpic.cn/mmbiz_png/LBrX00GQeictcibXFtyCyz4cbprgjicfsdEt0uRXC9qLC4sTR7Pdxr66vKwrvA4IRLJASKxFfsIm4S8iaH00zObEVA/640?wx_fmt=png)

如果你有取名困难症，你还可以让 ChatGPT 帮你取名和随机生成数据。  

![](https://mmbiz.qpic.cn/mmbiz_png/LBrX00GQeictcibXFtyCyz4cbprgjicfsdEwTKPOMEZtZlWIs4PZ1uFniajKDFsuwl75ELEvh6tjJib2MauJ1RAtegQ/640?wx_fmt=png)

当然，如果你突然忘记了冒泡排序应该怎么写，也可以问 ChatGPT。  

![](https://mmbiz.qpic.cn/mmbiz_png/LBrX00GQeictcibXFtyCyz4cbprgjicfsdEgXuLWOh0ERwymFotBacazOlLDucYLibaq5BmoAJqEia0c6XRmrdicvHhA/640?wx_fmt=png)

写代码遇到 Bug 怎么办？不要慌，问问 ChatGPT。  

![](https://mmbiz.qpic.cn/mmbiz_jpg/LBrX00GQeictcibXFtyCyz4cbprgjicfsdEFImWxyndZ7L8bTxh6xA3Fql8MCH7JSwHEV1icBicPYnGA9AVSx0ELibIw/640?wx_fmt=jpeg)

想要啥，都可以问 ChatGPT 要。  

![](https://mmbiz.qpic.cn/mmbiz_jpg/LBrX00GQeictcibXFtyCyz4cbprgjicfsdEH2O4S38QrneDA1mK5FkB175pyAVJwGRZYYB86icRibxHKI4dkPyDgYKQ/640?wx_fmt=jpeg)

好了，例子就先讲这些了，剩下的交给大家去探索了。

本篇文章用到的部分图片来自于我的好友千古壹号建的微信群，如感兴趣，可以扫码入群。

![](https://mmbiz.qpic.cn/mmbiz_jpg/LBrX00GQeictcibXFtyCyz4cbprgjicfsdENWlC8UdI4yhKmyjwYHSdAQ9NWzibQ4gHXyFkEgMVzBJBq3ibYYFAY8ibg/640?wx_fmt=jpeg)

如果觉得本篇文章对你有启发，请给我一个赞，谢谢您！  

预览时标签不可点

微信扫一扫  
关注该公众号





****



****



  收藏

