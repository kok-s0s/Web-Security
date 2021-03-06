<!--
 * @Author: kok-s0s
 * @Date: 2021-05-10 00:43:13
 * @LastEditTime: 2021-06-13 12:53:26
 * @Description: how to use docker well?
-->

[Docker Guide Video](https://www.youtube.com/watch?v=pTFZFxd4hOI)

```bash
docker

docker ps

docker ps -a

docker images

docker rm $(docker ps -a -q)

docker rmi $(docker images -q)

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

---

docker 开启 vulhub

1. 下载靶场

```bash
git clone git://github.com/vulhub/vulhub.git
```

2. 查看有什么靶场

```bash
cd vulhub
ls
```

3. 选择靶场开启,eg:struts2 的系列漏洞

```bash
cd vulhub/struts2/s2-057/
```

4. 启动靶场

```bash
sudo docker-compose up -d
```

5. 关闭靶场

```bash
sudo docker-compose down
```

6. 清理环境

```bash
sudo docker rm $(docker ps -a -q)
```

---

docker---WebGoat

```bash
docker search webgoat
docker pull webgoat/webgoat-8.0
```

VSCode---docker 插件
选择 `open in brower`

登录网页： `http://localhost:8080/WebGoat/login`

账号：kok-s0s
密码：kok-s0s

--- 

`exec` 命令

输入 `docker exec --help` 查看用法。

```
Usage:  docker exec [OPTIONS] CONTAINER COMMAND [ARG...]

Run a command in a running container

Options:
  -d, --detach               Detached mode: run command in the background
      --detach-keys string   Override the key sequence for detaching a container
  -e, --env list             Set environment variables
      --env-file list        Read in a file of environment variables
  -i, --interactive          Keep STDIN open even if not attached
      --privileged           Give extended privileges to the command
  -t, --tty                  Allocate a pseudo-TTY
  -u, --user string          Username or UID (format: <name|uid>[:<group|gid>])
  -w, --workdir string       Working directory inside the container
```

使用 `docker exec -it 69d1 bash` 能够直接使用终端模式进入到容器中。
