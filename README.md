## Summary

**[goky](https://github.com/gkhan496/goky) separate provided urls for every single path and fuzz them with provided wordlist.**


## Installation

```
pip install -r requirements.txt
```


```
python goky.py --help
usage: goky.py [-h] [--threads THREADS] [--pure PURE] [--timeout TIMEOUT] [--wordlist WORDLIST] [--list LIST]

options:
  -h, --help           show this help message and exit
  --threads THREADS    Number of threads (Default: 50)
  --pure PURE          Pure Response URL (Default: False)
  --timeout TIMEOUT    Timeout For Requests (Default: 4)
  --wordlist WORDLIST  Wordlist for fuzzing (Default: wordlist/wordlist.txt)
  --list LIST          List of URLs (Default: input.txt)
```

**Input**

```
https://www-api.ibm.com/cookie-sync/dbdm-data?rnd=1682106145634&utm_content=SRCWW&p1=Search&p4=43700071226857376&p5=e&=undefined&msclkid=1aa18b67e210155795b6ef250327489b&gclid=CLS0xJTYu_4CFTUGrQYdFQAFyg&gclsrc=ds&ida_ts=1682104659934&callback=_dl.fn.dataSync.callback&domain=ibm.com
https://www-api.ibm.com/cookie-sync/dbdm-data?rnd=1682115239621&utm_content=SRCWW&p1=Search&p4=43700071226857376&p5=e&=undefined&msclkid=2f1dd1b57a5114ed824db5f79b660e9e&gclid=CMrwuJXYu_4CFfI0rQYd2uUFfA&gclsrc=ds&ida_ts=1682104660080&callback=_dl.fn.dataSync.callback&domain=ibm.com
https://www-api.ibm.com/cookie-sync/dbdm-data?rnd=1682112051010&utm_content=SRCWW&p1=Search&p4=43700071226857376&p5=e&=undefined&msclkid=0f18d3128d3c141d9478b7506c0b54e2&gclid=CNv465DYu_4CFSUD5wodp6EFQQ&gclsrc=ds&ida_ts=1682104653704&callback=_dl.fn.dataSync.callback&domain=ibm.com
https://www-api.ibm.com/cookie-sync/dbdm-data?rnd=1682104861680&utm_content=SRCWW&p1=Search&p4=43700071226857376&p5=e&=undefined&msclkid=7340a04283b9119df96bc400628e56a4&gclid=CPqU0ZLYu_4CFV7DwgQdQEMGNg&gclsrc=ds&ida_ts=1682104654801&callback=_dl.fn.dataSync.callback&domain=ibm.com
https://www-api.ibm.com/cookie-sync/dbdm-data?callback=_dl.fn.dataSync.callback
https://www-api.ibm.com/cookie-sync/dbdm-data?rnd=1682261152040&cm_mmc=&cm_mmc_vendor=OSearch_Google&cm_mmc_category=-&cm_mmc_placement=-&cm_mmc_item=-&utm_source=Google&p1=Osearch&ida_ts=1682252411234&callback=_dl.fn.dataSync.callback&domain=ibm.com
https://www-api.ibm.com/cookie-sync/dbdm-data?rnd=1681992940918&p1=Search&p4=43700074866468861&p5=p&ida_ts=1681985691517&callback=_dl.fn.dataSync.callback&domain=ibm.com
https://www-api.ibm.com/cookie-sync/dbdm-data?rnd=1682214524171&p1=Search&p4=43700074866465702&p5=e&ida_ts=1682206174002&callback=_dl.fn.dataSync.callback&domain=ibm.com
https://www-api.ibm.com/search/api/v1-1/ibmcom/appid/dw/responseFormat/json?scope=dw&rmdt=ALL&appid=dw&sortby=&appid=dw&cachebust=1632256257523&dict=spelling&facet=%7B%22id%22%3A%22DW.ContentType%22%2C%22hierarchy%22%3A%22no%22%2C%22sortBy%22%3A%22weight%22%2C%20%22sortOrder%22%3A%22DESC%22%2C%22count%22%3A%22ALL%22%7D&facet=%7B%22id%22%3A%22DW.Technology%22%2C%22hierarchy%22%3A%22no%22%2C%22sortBy%22%3A%22weight%22%2C%20%22sortOrder%22%3A%22DESC%22%2C%22count%22%3A%22ALL%22%7D&facet=%7B%22id%22%3A%22DW.Component%22%2C%22hierarchy%22%3A%22no%22%2C%22sortBy%22%3A%22weight%22%2C%20%22sortOrder%22%3A%22DESC%22%2C%22count%22%3A%22ALL%22%7D&facet=%7B%22id%22%3A%22DW.Solution%22%2C%22hierarchy%22%3A%22no%22%2C%22sortBy%22%3A%22weight%22%2C%20%22sortOrder%22%3A%22DESC%22%2C%22count%22%3A%22ALL%22%7D&facet=%7B%22id%22%3A%22DW.Language%22%2C%22hierarchy%22%3A%22no%22%2C%22sortBy%22%3A%22weight%22%2C%20%22sortOrder%22%3A%22DESC%22%2C%22count%22%3A%22ALL%22%7D&facet=%7B%22id%22%3A%22DW.Practice%22%2C%22hierarchy%22%3A%22no%22%2C%22sortBy%22%3A%22weight%22%2C%20%22sortOrder%22%3A%22DESC%22%2C%22count%22%3A%22ALL%22%7D&facet=%7B%22id%22%3A%22DW.Industry%22%2C%22hierarchy%22%3A%22no%22%2C%22sortBy%22%3A%22weight%22%2C%20%22sortOrder%22%3A%22DESC%22%2C%22count%22%3A%22ALL%22%7D&filter=language%3Aen&fr=0&nr=10&page=1&ql=en&query=%20&rc=us&refinement=&rmdt=dc_subject_original%2Cdc_type_original%2Cwpid%2Cdwcontenttype%2Cdwcontentarea%2Cdwcontentareaid%2Cdwtopic%2Cdwtopicid%2Cdwboostedurl%2Cdwtechnology%2Cdwindustry%2Cdwcomponent%2Cdwdeploymodel%2Cdwsolution%2Cdwpractice%2Cdwlanguage%2Cdwcity%2Cdwmodeltechnology%2Cdwdatatechnology&scope=dw&sm=true&smnr=20&variant=pvboost%3A3
https://www-api.ibm.com/search/api/v1-1/ibmcom/appid/dw/responseFormat/json?scope=dw&rmdt=ALL&appid=dw&sortby=&appid=dw&cachebust=1632256257647&dict=spelling&facet=%7B%22id%22%3A%22DW.ContentType%22%2C%22hierarchy%22%3A%22no%22%2C%22sortBy%22%3A%22weight%22%2C%20%22sortOrder%22%3A%22DESC%22%2C%22count%22%3A%22ALL%22%7D&facet=%7B%22id%22%3A%22DW.Technology%22%2C%22hierarchy%22%3A%22no%22%2C%22sortBy%22%3A%22weight%22%2C%20%22sortOrder%22%3A%22DESC%22%2C%22count%22%3A%22ALL%22%7D&facet=%7B%22id%22%3A%22DW.Component%22%2C%22hierarchy%22%3A%22no%22%2C%22sortBy%22%3A%22weight%22%2C%20%22sortOrder%22%3A%22DESC%22%2C%22count%22%3A%22ALL%22%7D&facet=%7B%22id%22%3A%22DW.Solution%22%2C%22hierarchy%22%3A%22no%22%2C%22sortBy%22%3A%22weight%22%2C%20%22sortOrder%22%3A%22DESC%22%2C%22count%22%3A%22ALL%22%7D&facet=%7B%22id%22%3A%22DW.Language%22%2C%22hierarchy%22%3A%22no%22%2C%22sortBy%22%3A%22weight%22%2C%20%22sortOrder%22%3A%22DESC%22%2C%22count%22%3A%22ALL%22%7D&facet=%7B%22id%22%3A%22DW.Practice%22%2C%22hierarchy%22%3A%22no%22%2C%22sortBy%22%3A%22weight%22%2C%20%22sortOrder%22%3A%22DESC%22%2C%22count%22%3A%22ALL%22%7D&facet=%7B%22id%22%3A%22DW.Industry%22%2C%22hierarchy%22%3A%22no%22%2C%22sortBy%22%3A%22weight%22%2C%20%22sortOrder%22%3A%22DESC%22%2C%22count%22%3A%22ALL%22%7D&filter=%28%28DWContentType%3A%22Tutorials%22%29%20AND%20%28DWTechnology%3A%22Artificial%20intelligence%22%29%29%20AND%20%28language%3Aen%29&fr=0&nr=20&page=1&query=%20&refinement=&rmdt=dc_subject_original%2Cdc_type_original%2Cwpid%2Cdwcontenttype%2Cdwcontentarea%2Cdwcontentareaid%2Cdwtopic%2Cdwtopicid%2Cdwboostedurl%2Cdwtechnology%2Cdwindustry%2Cdwcomponent%2Cdwdeploymodel%2Cdwsolution%2Cdwpractice%2Cdwlanguage%2Cdwcity%2Cdwmodeltechnology%2Cdwdatatechnology&scope=dw&sm=true&smnr=20&variant=pvboost%3A3
https://www-api.ibm.com/search/typeahead/v1?lang=en&cc=us&query=l&callback=jQuery22407975008573388203_1555336266902&_=1555336266907
https://www-api.ibm.com/search/typeahead/v1?lang=en&cc=us&query=lo&callback=jQuery22407975008573388203_1555336266904&_=1555336266908
https://www-api.ibm.com/search/typeahead/v1?lang=en&cc=us&query=lot&callback=jQuery22407975008573388203_1555336266909&_=1555336266910
https://www-api.ibm.com/search/typeahead/v1?lang=en&cc=us&query=lotu&callback=jQuery22407975008573388203_1555336266911&_=1555336266912
```

**Separated**

```
https://www-api.ibm.com/
https://www-api.ibm.com/cookie-sync/
https://www-api.ibm.com/search/
https://www-api.ibm.com/search/api/
https://www-api.ibm.com/search/api/v1-1/
https://www-api.ibm.com/search/api/v1-1/ibmcom/
https://www-api.ibm.com/search/api/v1-1/ibmcom/appid/
https://www-api.ibm.com/search/api/v1-1/ibmcom/appid/dw/
https://www-api.ibm.com/search/api/v1-1/ibmcom/appid/dw/responseFormat/
https://www-api.ibm.com/search/typeahead/
```

**Wordlist**

```
send.php
actuator
api
api/v1
heapdump
env
robots.txt
curl.php
get.aspx
```

**Fuzzing with wordlist for each url for example**

```
https://www-api.ibm.com/send.php
https://www-api.ibm.com/cookie-sync/send.php
https://www-api.ibm.com/search/send.php
https://www-api.ibm.com/search/api/send.php
https://www-api.ibm.com/search/api/v1-1/send.php
https://www-api.ibm.com/search/api/v1-1/ibmcom/send.php
https://www-api.ibm.com/search/api/v1-1/ibmcom/appid/send.php
https://www-api.ibm.com/search/api/v1-1/ibmcom/appid/dw/send.php
https://www-api.ibm.com/search/api/v1-1/ibmcom/appid/dw/responseFormat/send.php
https://www-api.ibm.com/search/typeahead/send.php
```

[![asciicast](https://asciinema.org/a/wuF9iuCQCNg5COnmlVJT9e1fN.svg)](https://asciinema.org/a/wuF9iuCQCNg5COnmlVJT9e1fN)





