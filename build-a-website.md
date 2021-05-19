<!--
 * @Author: kok-s0s
 * @Date: 2021-05-18 02:29:30
 * @LastEditTime: 2021-05-20 00:41:24
 * @Description: website
-->

# 建站过程

## HTTP 网站的搭建

**Key Words**
docker vps wordPress

**准备工作**
一个云服务器，推荐在 vultr 上购买个，建议选择 Ubuntu 系统，简单易上手！

利用你选择的工具(xshell，VSCode，and so on)远程连接你的云服务器；

连接 update 过后，下载 docker.io 和 docker-compose；

**配置**
编写一个脚本 yml 格式，便于安装所有必须软件，我这里提供一个简易的脚本：

```yml
version: "2.0"

services:
  db:
    image: mysql:5.7
    volumes:
      - /root/db/:/var/lib/mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: **********（自定义）
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: **********（自定义）

  wordpress:
    depends_on:
      - db
    image: wordpress
    ports:
      - "80:80"
    restart: always
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: **********（自定义）
    volumes:
      - /root/www/:/var/www/html
```

运行脚本命令：docker-compose -f docker-compose.yml up -d

此时，在浏览器访问你的网站 IP 地址，你会看到 WordPress 的安装引导，根据提示进行就行了。

之后便可自定义出你自己专属的网站了！

想要备份，只要把你服务器里的 www，docker-compose.yml，db 三个东西拷贝下来就行了，想要再次使用，只需要在有和上述大致差不多配置的服务器也可以再次运行起来。

关闭很简单，执行命令：docker-compose -f docker-compose down

## 测试 HTTP 网站

1. 使用`wireshark`抓包，浏览器与搭建的网站做交互，但却无法抓取到数据包；
2. 使用工具（WebPathBrute）扫描自己搭建的网站站点，此时，`wireshark`能够抓取到[数据包](./files/WireShark-Files/TestWordPress.pcapng);

对抓取的数据包做分析，的确包含网站的信息，实测出 HTTP 网站的不安全。HTTP 传输的数据包无加密，明文信息直接暴露，直接导致关键信息泄露，会造成很多方面的影响（隐私最为关键！）。
