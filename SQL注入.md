<!--
 * @Author: kok-s0s
 * @Date: 2021-05-10 20:07:07
 * @LastEditTime: 2021-05-17 00:34:56
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

