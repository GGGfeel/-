# -
使用Python 调用百度识图，识取本地图片并得到结果
先自己手动完成百度识图的整个过程，#5为向百度上传图片，#10为一个不知道的响应过程，#14为一个关于注册的js响应，#16同样为一个json。通过观察可知，识图的相关响应只发生在#5和#10以及#16三步。

利用Fiddler观察#5的请求信息，是一个post形式的请求，除了一般的headers以外，还有一个文件传输

（具体内容不止图中这点）
这是一个multipart/form-data请求，能够用python的requests进行模拟。具体方法参照：
http://blog.csdn.net/j_akill/article/details/43560293和https://www.cnblogs.com/titan5750/p/6879114.html
返回的response中的内容如下所示

然后观察#10，#10的网页中已经有了guessword

该guessword应该就是结果了。那么只要获得#10的网址就可以获得识图的结果，也就不需要查看#16了。查看#10的request_url，

该网址可以用到#5中返回的querySign和queryImageUrl，推测fm、uptype、result应该是不变的字符串，只剩下最后一个vs未知。查找所有js文件，在http://imgn0.bdstatic.com/image/mobile/n/static/pcdutu/static/pkg/pcdutu_*****.js中找到

观察后可知fm、uptype、result的确为不变的字符串（不同情况下可能不同），而vs取值来自变量u，将该js反编译以后

u为window.bd，这个window有可能是JavaScript 层级中的顶层对象Window，代表一个浏览器窗口或一个框架。那么这个window应该第一次打开百度识图网页的时候就确定了，打开image.baidu.com/?fr=shitu的网页，查看源代码，果然里面有一个window，且该window有一个vsid。

将这个vsid保存下来结合#5中获得的数据，就可以构造#10的网页，进而获得#10网页中的guessword。

