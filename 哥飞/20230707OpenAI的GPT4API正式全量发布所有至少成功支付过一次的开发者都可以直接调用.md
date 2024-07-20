![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeicv7yia86iaNvV3FozYZvJFtKZho9iagFZkV3S2VlW316DniaQGiaI15k6vILez91tFSSZ9YCyxAEOTuJcw/0?wx_fmt=jpeg)

#  OpenAI 的 GPT4 API 正式全量发布，所有至少成功支付过一次的开发者都可以直接调用

原创  我是哥飞  [ 哥飞 ](javascript:void\(0\);)

__ _ _ _ _

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicv7yia86iaNvV3FozYZvJFtKZQKnNicUicK0VWOia8IDIVghIobMUDggZKbKPvRCcperhBWnzDaRialKyHw/640?wx_fmt=png)

激动人心的时刻来临了，刚刚 OpenAI 官方博客介绍，GPT4 API现已全量开放给开发者了。  

只要是绑定了信用卡，并且成功扣款过一次的开发者账号，都有权限调用 GPT4 API。

并且，月底之前，会向更多开发者开放。  

不过暂时开放的只是 8K 模型，更高的模型会评估算力之后陆续开放。  

价格方面，暂时没有变化。  

不管是暂时只开放 8K 模型，还是价格暂时不变，还是只开放给成功付款一次的开发者账户，目的都是在可控的范围内让真正有需要的开发者使用。

而不是被滥用，被过度使用。

* * *

  

另外，/v1/completions 将被弃用，OpenAI 推荐大家都转向 /v1/chat/completions
，并且后者已经有了97%的调用量了，也就是还剩3%的请求在调用前者。

这也是为了收回旧模型，集中算力到更多人需要的模型上。

* * *

  

同样被收回的模型还有老的潜入 embeddings 模型，如以下模型，都被建议替换为  text-embedding-ada-002 模型。

code-search-ada-code-001  
---  
code-search-ada-text-001  
code-search-babbage-code-001  
code-search-babbage-text-001  
text-search-ada-doc-001  
text-search-ada-query-001  
text-search-babbage-doc-001  
text-search-babbage-query-001  
text-search-curie-doc-001  
text-search-curie-query-001  
text-search-davinci-doc-001  ‍  
text-search-davinci-query-001  
text-similarity-ada-001  
text-similarity-babbage-001  
text-similarity-curie-001  
text-similarity-davinci-001  
  
* * *

\---------------先不要走开  \---------------

  

哥飞搞了一个付费微信群，有点贵，666元一年，目前有46个群友了，各有各的本事。  

以下是招募启事，如果感兴趣的话，请加我微信 qiayue 。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeicv7yia86iaNvV3FozYZvJFtKZEsia2c24CpF2mehKhEaxeH74T2YtXMmjStpyibddUsKNUwLEwcWpXBng/640?wx_fmt=jpeg)

  

预览时标签不可点

微信扫一扫  
关注该公众号





****



****



  收藏

