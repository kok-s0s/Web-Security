<!--
 * @Author: kok-s0s
 * @Date: 2021-05-26 23:13:18
 * @LastEditTime: 2021-05-30 14:54:44
 * @Description: file content
-->

XEE 漏洞---XML External Entity Injection---外部实体注入漏洞

XEE 漏洞发生在应用程序解析 XML 输入时，没有禁止外部实体的加载，导致可加载恶意外部文件，造成文件读取，命令执行，内网端口扫描，攻击内网网站，发起 dos 攻击等危害。

keyWords:

- XML
- DTD---Document Type Definition 文档类型定义
