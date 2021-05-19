<!--
 * @Author: kok-s0s
 * @Date: 2021-05-10 20:07:07
 * @LastEditTime: 2021-05-19 23:03:58
 * @Description: file content
-->

结构化查询语言（Structured Query Language） [SQL](https://www.w3schools.com/sql/)

SQL 能让我们访问到数据库数据。

**SQL 注入**
用户提交的数据可以被数据库解析执行

前端的输入框可以输入 SQL 语句

eg：简单绕过

```sql
select * from student where name = "aa" and 1=1 -"";
```

小技巧：
`inurl:php?id=` php 页面匹配

**联合查询注入**
union

**绕过**
大小写尝试
and so on