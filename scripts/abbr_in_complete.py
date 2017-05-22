#!/usr/bin/env python
# coding=utf-8
# File Name: abbr_in_complete.py
# Author: lxw
# Date: Fri 19 May 2017 10:35:48 AM CST

import pymongo

HOST = "192.168.1.36"
PORT = 27017
DATABASE = "scrapy"
COLLECTION_NAME = "cninfoCompanyName"


def main():
    client = pymongo.MongoClient(HOST, PORT)
    db = client[DATABASE]
    col = db[COLLECTION_NAME]
    count = 0
    duplicate_count = 0
    total_count = 0
    abbr_full_dict = {}
    for item in col.find():
        total_count += 1
        shortname = item["company_sortname"].strip().replace(" ", "").replace("B", "").replace("Ｂ", "").replace("A", "")
        fullname = item["company_fullname"].strip().replace(" ", "")
        if shortname not in fullname:
            if shortname in abbr_full_dict:
                print(shortname, abbr_full_dict[shortname], fullname)
                print(fullname==abbr_full_dict[shortname])
                duplicate_count += 1
            abbr_full_dict[shortname] = fullname
            count += 1
    # print(abbr_full_dict)
    print(count)
    print(duplicate_count)
    print(total_count)


if __name__ == "__main__":
    main()


"""
总结： 
1. 全文检索有很多干扰项：（工商银行为例） 
1). 冯光成与青海碱业有限公司一般损害公司权益纠纷审判监督民事裁定书
2). 金辉企业与湛江市巨通实业发展公司、湛江市华业房产公司确认合同无效纠纷申请再审民事裁定书
...
以当事人为检索条件 比全文检索结果要准确
2. 简称和全称使用哪个作为检索内容
1). 对于简称包含在全称内的，应使用简称进行检索
2). 对于简称不包含在全称内的情况：使用全称作为检索内容大多数都满足，但有特例(富奥汽车零部件股份有限公司)，所以应采用全称简称都抓取然后去重的方式（并集）

### "工商银行" in "中国工商银行":
1. 当事人:工商银行
查询结果案例数: 132446
Param:当事人:工商银行

2. 当事人:中国工商银行
查询结果案例数: 132302
Param:当事人:中国工商银行

3. 全文检索:工商银行
查询结果案例数: 798945
Param:全文检索:工商银行

4. 全文检索:中国工商银行
查询结果案例数: 482843
Param:全文检索:中国工商银行

全文检索有很多干扰项： 
1). 冯光成与青海碱业有限公司一般损害公司权益纠纷审判监督民事裁定书
2). 金辉企业与湛江市巨通实业发展公司、湛江市华业房产公司确认合同无效纠纷申请再审民事裁定书
...


### "中联重科" in "中联重科股份有限公司":
1. 当事人: 中联重科
查询结果案例数: 11143

2. 当事人: 中联重科股份有限公司
查询结果案例数: 4823

3. 全文检索: 中联重科
查询结果案例数: 9281

4. 全文检索: 中联重科股份有限公司
查询结果案例数: 6089

----------------------------------------------------------------------
----------------------------------------------------------------------

### "深房集团" not in "深圳经济特区房地产(集团)股份有限公司"
1. 当事人:深房集团
查询结果案例数: 1

2. 当事人:深圳经济特区房地产(集团)股份有限公司
查询结果案例数: 0

3. 全文检索:深房集团
查询结果案例数: 7

4. 全文检索:深圳经济特区房地产(集团)股份有限公司
查询结果案例数: 0


### "富奥股份" not in "富奥汽车零部件股份有限公司"
1. 当事人:富奥股份
查询结果案例数: 0

2. 当事人:富奥汽车零部件股份有限公司
查询结果案例数: 36

3. 全文检索:富奥股份
查询结果案例数: 3

4. 全文检索:富奥汽车零部件股份有限公司
查询结果案例数: 57


### "伊利股份" not in "内蒙古伊利实业集团股份有限公司"
1. 当事人:伊利股份
查询结果案例数: 0

2. 当事人:内蒙古伊利实业集团股份有限公司
查询结果案例数: 132

3. 全文检索:伊利股份
查询结果案例数: 5

4.  全文检索:内蒙古伊利实业集团股份有限公司
查询结果案例数: 244
"""




"""
MEANINGLESS:
1. 当事人:工商银行,全文检索:工商银行
查询结果案例数: 132405
Param:当事人:工商银行,全文检索:工商银行
"""
