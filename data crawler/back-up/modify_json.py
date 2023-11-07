import re

item =  {
            "product_name": "\n\t\t\t\t\t\t\tCPU Intel Core i5 11400F (2.60 Up to 4.40GHz, 12M, 6 Cores 12 Threads) Box Ch\u00ednh H\u00e3ng (Kh\u00f4ng GPU)\n\t\t\t\t\t\t",
            "product_price": "3,590,000\u20ab",
            "product_img_urls": "[<img alt=\"CPU Intel Core i5 11400F (2.60 Up to 4.40GHz, 12M, 6 Cores 12 Threads) Box Ch\u00ednh H\u00e3ng (Kh\u00f4ng GPU)\" src=\"//product.hstatic.net/200000420363/product/cpu-i5-11400f-600x600_9035ba693e094acbbc610fbfb9a9ff1d_master.jpg\"/>]",
            "product_description": "<div class=\"hrvproduct-tabs ch\">\n<ul>\n<li>B\u00f4\u0323 x\u01b0\u0309 ly\u0301: I5 11400F \u2013 Rocket Lake</li>\n<li>B\u1ed9 nh\u1edb \u0111\u1ec7m: 12 MB Cache</li>\n<li>T\u1ea7n s\u1ed1 c\u01a1 s\u1edf c\u1ee7a b\u1ed9 x\u1eed l\u00fd: 2.60 GHz</li>\n<li>T\u1ea7n s\u1ed1 turbo t\u1ed1i \u0111a: 4.40 GHz</li>\n<li>H\u1ed7 tr\u1ee3 socket: FCLGA1200</li>\n<li>S\u1ed1 l\u00f5i: 6, S\u1ed1 lu\u1ed3ng: 12</li>\n<li>TDP: 65 W</li>\n<li>\u0110\u1ed3 h\u1ecda t\u00edch h\u1ee3p: Kh\u00f4ng</li>\n</ul>\n</div>"
        }

item["product_name"] = item["product_name"].strip("\n \t")
item["product_price"] = item["product_price"].strip("\n \t")
item["product_img_urls"] = item["product_img_urls"].strip("\n \t")
item["product_description"] = item["product_description"].strip("\n \t")
# item["product_name"] = item["product_name"].strip("\t")

print(item)