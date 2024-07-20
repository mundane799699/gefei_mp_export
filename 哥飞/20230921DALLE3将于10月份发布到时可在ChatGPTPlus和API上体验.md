![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeictib15GAhhBkjVhSVEiaXNVwgPgwjbQtMQCMXiafu8pbT1ZXxa6ouZOC5Nze3P4Dby1icFDH40hOpNOkA/0?wx_fmt=jpeg)

#  DALL·E 3 将于10月份发布，到时可在 ChatGPT Plus 和 API 上体验

原创  我是哥飞  [ 哥飞 ](javascript:void\(0\);)

__ _ _ _ _

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeictib15GAhhBkjVhSVEiaXNVwgykfZib03PDO6iaHnCduMRiczua6UOndrMDibvtevKicZEO19pyWBPVYd84Q/640?wx_fmt=png)

大家好，我是哥飞。

今天哥飞给大家介绍 OpenAI 的文生图服务 DALL·E 的最新版本 DALL·E 3 。

DALL·E 2是在 2022 年的 11 月 3 日对外发布API的，而 ChatGPT 是在 2022 年 11 月 30 日上线网页版的。  

我们大多数人了解 OpenAI 都是因为  Chat  GPT 的爆火。  

2022 年 11 月 30 日相当于是AI世界的命运齿轮转动时刻。  

好我们回到  DALL·E 2 ，先介绍一下  DALL·E 2 有哪些能力。  

  

** 一、DALL·E 2  **

1.1、DALL·E 2 基本信息

官网： https://openai.com/dall-e-2

在线体验： https://labs.openai.com/

模型介绍： https://platform.openai.com/docs/models/dall-e

API文档： https://platform.openai.com/docs/api-reference/images

  

1.2、创建图像  

接口：https://api.openai.com/v1/images/generations  

能力：文本生成图像  

主要请求参数有三个，prompt是画图提示词，n是一次生成的图片数量，size是图像大小，目前支持256x256、512x512和1024x1024三种规格，也就是
D  A  LL·E  2只支持正方形图片  ：  

  *   *   *   *   *   *   *   * 

    
    
    curl https://api.openai.com/v1/images/generations \  -H "Content-Type: application/json" \  -H "Authorization: Bearer $OPENAI_API_KEY" \  -d '{    "prompt": "A cute baby sea otter",    "n": 2,    "size": "1024x1024"  }'

返回数据中直接带了图片url数组：

  *   *   *   *   *   *   *   *   *   *   * 

    
    
    {  "created": 1589478378,  "data": [    {      "url": "https://..."    },    {      "url": "https://..."    }  ]}

举例，提示词“An astronaut riding a horse in photorealistic style.” 生成的图像为：  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeictc9epoicTeoMoPvEMhhE616W3xd0YMy5yrvDDPcMWmnIUCKUHj2K8uZ90tvlLK7dbdTnV8y47KLxQ/640?wx_fmt=jpeg) |  ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeictc9epoicTeoMoPvEMhhE616ewJdtTSNnHtGL0iak2gicJ4QeVzOUFIbVIvn4OcyahZicT6ib1aCnbRKzg/640?wx_fmt=jpeg) |  ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeictc9epoicTeoMoPvEMhhE616fr2Y5Fs496TFTrhwwPOaXzsNacuBXjn1HAU43pAFcHIZeheiasgmAXw/640?wx_fmt=jpeg) |  ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeictc9epoicTeoMoPvEMhhE616ej6zwIPVwbcCcjDIVkzbcmok6MP5qibdtLEXPiciaahEKbDcetIibVdxjg/640?wx_fmt=jpeg)  
---|---|---|---  
  
  

1.3、编辑修改图像  

接口：https://api.openai.com/v1/images/edits

能力：用提示词对上传的图像进行修改  

主要请求参数有五个，在创建图片的参数基础上增加了两个，一个是原图 image ，一个是遮罩 mask：  

  *   *   *   *   *   *   * 

    
    
    curl https://api.openai.com/v1/images/edits \  -H "Authorization: Bearer $OPENAI_API_KEY" \  -F image="@otter.png" \  -F mask="@mask.png" \  -F prompt="A cute baby sea otter wearing a beret" \  -F n=2 \  -F size="1024x1024"

原图必须是正方形的png图片，  遮罩 mask 也是一张png图片，mask 尺寸必须跟原图 image 尺寸一致。

mask 的透明区域就是模型会修改的区域，必须严格透明且支持不规则边界。

  

1.4、生成相似但有变化的图片

接口：https://api.openai.com/v1/images/variations

能力：上传一张图，生成几张相似但有变化的图片

主要参数有3个，image 是我们上传的原图，n是生成图片数量，size是图片尺寸：  

  *   *   *   *   * 

    
    
    curl https://api.openai.com/v1/images/variations \  -H "Authorization: Bearer $OPENAI_API_KEY" \  -F image="@otter.png" \  -F n=2 \  -F size="1024x1024"

返回值跟生成图像一样。

举例上传第一张图，生成后四张相似图片：  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeictib15GAhhBkjVhSVEiaXNVwgPsnyia8Z0GLiaibC0VaS1OEtkxEd1LU9JqKe10CibxIdWonF9YXIB9U3lw/640?wx_fmt=jpeg) |  ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeictib15GAhhBkjVhSVEiaXNVwgf2lE5ticq2uibYLbKgvXD9kTTFy04icc7JtkibuDcwibLHbg2TUIib2IOs6A/640?wx_fmt=jpeg) |  ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeictib15GAhhBkjVhSVEiaXNVwg6GaOuMv8zv61rSgdKAl6FOkGa5335iaelWHhpDp0KNQVtnWpqlImZuQ/640?wx_fmt=jpeg) |  ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeictib15GAhhBkjVhSVEiaXNVwguYxqdLoNUAFv74AyRWZJcgvMPOyDibTeDVAWLicSvrRozFn6dKaicmpEA/640?wx_fmt=jpeg) |  ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeictib15GAhhBkjVhSVEiaXNVwgJL5csrh8wIVlMEjWycH6xkuwdzbOFObUvn5JJRqLc6JrSR851KRMqg/640?wx_fmt=jpeg)  
---|---|---|---|---  
  
  

1.5、扩图 Outpainting

这个能力目前没有对外提供接口，不过可以在官网看到效果示例，下方上图是输入的图片，下图是扩出的图片。  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeictib15GAhhBkjVhSVEiaXNVwg1wuTuTDk2OYPmEgMVrEhanF0k6cOTia0TBjQU4EDZgaAJ4F6mB9w0Tg/640?wx_fmt=jpeg)  
---  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeictib15GAhhBkjVhSVEiaXNVwgqcd8AiaO0ibwdmaNmKufJ5tFhUqDicdAYOV0bW98HuufP5rdBHicDJa8pA/640?wx_fmt=jpeg)  
  
  

1.6、修图  Inpainting

这里哥飞不太清楚，是否跟1.3是同一个接口。

举例，输入图像是下方左图，用提示词“Add a flamingo beside the pool.”得到了下方右图。  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeictib15GAhhBkjVhSVEiaXNVwgPwvv41r5vtDyF9pdnDuxBicquh39F7zqkYdibjkmIDPruicBbUQicEGr8w/640?wx_fmt=jpeg) |  ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LBrX00GQeictib15GAhhBkjVhSVEiaXNVwgyKmib3BFtiav6wTOAceFxkMStsPnnqsJfV2yN6OKSqnTLUQx8BYOVmUQ/640?wx_fmt=jpeg)  
---|---  
  
  

好了，  D  A  LL·E  2 我们介绍完了，下面看看新发布的  D  A  LL·E 3 有什么不一样。  

** 二、DALL·E 3  **

2.1、DALL·E 3 基本信息

官网： https://openai.com/dall-e-3

2.2、DALL·E 3 细节控制  

支持  通过  prom  pt  对图像每一处细节  进行控制，如以下几句提示词，完全可以认为就是一段故事中的场景描述，拿来就能够生成合适的图片。

The sidewalks bustling with pedestrians enjoying the nightlife.

A bustling city street under the shine of a full moon.

At the corner stall, a young woman with fieryred hair, dressed in a signature
velvet cloak.s hagaling with the grumpv old vendor.

The grumpy vendor, a tall, sophisticated man, is wearing a sharp suitsports a
noteworthy moustache and is animatedly conversing on hissteamounk telephone.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeictib15GAhhBkjVhSVEiaXNVwgs5rwPSeXibC01ibL9nX6xPT8eTV7vdeGxDMVU9EovHNFhsuyRpk3XbLQ/640?wx_fmt=png)

2.3、画面更精美

即使是同一段提示词，相比于DALL·E 2，DALL·E 3画出的画面也会更精美。

如提示词“  An expressive oil painting of a basketball player dunkin  g, depicted
as an explosion of a nebula  ”，  下方左图是  DALL·E 2生成，右图是  DALL·E 3 生成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeictib15GAhhBkjVhSVEiaXNVwgGeibeRl5mhve6AZEEWFB2YgPgqwfDoZX8ekuD5Eft8Hu2qk7icJ1dic0Q/640?wx_fmt=png) |  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeictib15GAhhBkjVhSVEiaXNVwgSLaN6cuibKQ4C4Xs54CkvKQXwLcq7fEId3G8iaDjLMAQ38t6V4la5YAQ/640?wx_fmt=png)  
---|---  
  
  

2.4、DALL·E 3 集成 ChatGPT  

到时大家可以在 ChatGPT 中直接用对话来画图，哪里画得不满意，可以直接用自然语言和GPT沟通，让GPT去修改。

以下是官网给出的一些示例。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeictib15GAhhBkjVhSVEiaXNVwgiblbAnDgBsibyXJvMQI1DlfRSzjl91jXnjSbUhkk60eksmyQVDH0f7Zg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeictib15GAhhBkjVhSVEiaXNVwgdvef11wvSbfVZS4licibkgwlRBZcfiarYtl9Ne7cMCiaKJFe765uAVDpYA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeictib15GAhhBkjVhSVEiaXNVwgOjdJciaQb4OWdRc1tPzLh6osPgf4n0jneiaib9TRjDKJw0JVJicXxHeYPA/640?wx_fmt=png)

2.5、创意掌控

DALL·E 3将拒绝提供在世艺术家风格图像的生成请求，创作者也可以提交申请将自己的作品从模型训练数据集中删除。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeictib15GAhhBkjVhSVEiaXNVwgbsEh0mLncjnzm2vXejC0rysibvBksZ8YyVfn2BrbiaUYCyQ7PXUzMHbg/640?wx_fmt=png)

  

三、为什么哥飞介绍这个？

哥飞是吃饱了撑的，来介绍这个吗？  

当然不是了。

之前我们在这篇文章中说了《 [ 找新词：一个永远有效的建站策略，让你快速拿到搜索引擎流量
](http://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650079457&idx=1&sn=6a6b914a2685581ef26ef00cb8b19ee1&chksm=bf3f31da8848b8cc7e206419bcb2884415659dae3bd17fb77b9859adf106da494bd843f5d6f4&scene=21#wechat_redirect)
》。  

那么今天哥飞就给你介绍了一个新词“DALL·E 3”，围绕着这个新词，你能去做什么呢？  

这是哥飞留给你的今日作业，欢迎在评论中留言写作业。  

你也可以加入哥飞运营的付费社群“哥飞的朋友们”，一起来讨论到底如何基于这个新词去做网站，去搞流量，去赚钱。

这个社群从7月2日成立到现在两个半月的时间了，总共有335位朋友加入了。  

为什么一个定价666元一年的社群会有这么多朋友愿意加入呢？

因为哥飞一直坚持利他分享，让大家知道怎么找方向，知道怎么做网站，知道怎么获取流量，知道怎么流量变现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicstM5JvDTzRWcXRk4rv6J0z99hHZ9yIpq82NNlNGyxOialxksQUX9kHTIicdFickWe8sBYTdUrt9gIhw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

经常有朋友跟哥飞说，加入哥飞的这个社群，是今年做的最正确决定之一。

正在读文章的你，如果你决定加入哥飞的这个社群，哥飞敢保证，也绝对是你今年剩下的时间里做的最正确的决定之一。

不管加不加社群，都请加哥飞微信 qiayue ，欢迎交流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LBrX00GQeicsG8Pro6O9Hu75bIIiafZVPs3qlYeaNNJ1BpqNplEGgibL5m1bcq8a1N1rzoI5lia8aJjtHfgiaAADJJQ/640?wx_fmt=png)

预览时标签不可点

微信扫一扫  
关注该公众号





****



****



  收藏

