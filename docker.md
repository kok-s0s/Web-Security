<!--
 * @Author: kok-s0s
 * @Date: 2021-05-10 00:43:13
 * @LastEditTime: 2021-05-21 13:03:03
 * @Description: how to use docker well?
-->

[Docker Guide Video](https://www.youtube.com/watch?v=pTFZFxd4hOI)

```bash
docker

docker ps

docker ps -a

docker images

docker rm $(docker ps -a -q)

dcoker rmi $(docker images -q)

docker stop id

docker start id

docker restart id

docker run -it images /bin/bash

docker run -itd images

docker search 'something you want to get'

docker pull 'something you want to get'

# 文件映射
# eg
docker run -it -p 127.0.0.1:8080:80 -v /Users/kok-s0s/Desktop/csrf/:/usr/local/apache2/htdocs/ httpd


```

`httpd` Apache 官方搭建网站镜像
