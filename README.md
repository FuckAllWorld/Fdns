# Fdns
## 概述
提取 https://opendata.rapid7.com/sonar.fdns_v2/ 中的A记录、MX记录、CNAME记录等，后续会慢慢增加

## 使用说明
-d --domain:域名
-r --record:记录
-f --file:gz文件
### 查询某域名A记录
python fdns.py -f xxx.gz -d google.com -r a

### 查询某域名mx
python fdns.py -f xxx.gz -d google.com -r mx

