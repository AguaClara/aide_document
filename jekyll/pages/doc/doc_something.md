---
title: A sample documentation
tags: [getting_started]
keywords: documentation theme, demo
last_updated: Feb 1, 2018
summary: "A sample from /AguaClara/aide_document/ExploringCode/data.json"
permalink: doc_something.html
sidebar: doc_sidebar
---

The link of the page is {{site.url}}{{site.baseurl}}{{page.url}}

{% highlight javascript %}
{
"width": "100",
 "list": [{"sublist":["1","2","3"]},{"sublist":["4","5","6"]},{"sublist":["5","6","7"]},{"sublist":["3","4","5"]}],
 "image_path": "images/jekyll.png"
}
{% endhighlight %}

1.  Sublist 1
    * "1"
    * "2"
    * "3"
2.  Sublist 2
    * "4"
    * "5"
    * "6"

{% include image.html file="jekyll.png" url="./images/jekyll.png" alt="fun"
caption="This is a picture with maximum width 100px" max-width="100"	%}
