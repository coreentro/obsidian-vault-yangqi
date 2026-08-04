---
title: "加餐｜常见的Linux命令"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/NurXwByqwif1ivk6cl3cpokSnnd
node_token: NurXwByqwif1ivk6cl3cpokSnnd
obj_token: GtYMdqw0uoo6LExMidzcrWNBnVh
obj_type: docx
space_id: 7375763230725046276
space_name: "成为Agent工程师"
depth: 4
breadcrumb:
  - "成为Agent工程师"
  - "Coze实战课项目"
  - "加餐文档"
  - "编程思维体系"
  - "加餐｜常见的Linux命令"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 119
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 成为Agent工程师
---

# 加餐｜常见的Linux命令

> [!info] 位置
> 成为Agent工程师 › Coze实战课项目 › 加餐文档 › 编程思维体系

# 加餐｜常见的Linux命令

大家好，这里是《成为Agent工程师之Coze实战》的加餐文档。

这篇文档我们来学习下最常见的一些Liunx命令，我会为每个命令提供输出示例，让你更直观地了解命令的效果。

## 写在前面

在开始之前，我想说明几点：

1. 本教程面向Linux新手，只涵盖最基础、最常用的命令。
2. 所有命令都会配有简单解释、实际例子和输出示例。
3. 建议你一边阅读，一边在自己的Linux系统上实践。
4. 这篇文档我没有特别详细的介绍每个命令的作用，因为我想让你充分利用你的Kimi Chat

好了，让我们开始吧！

## 一、文件和目录操作命令

### 1. ls - 列出目录内容

`ls`命令用于列出当前目录下的文件和文件夹。

用法：

```Shell
ls [选项] [目录]
```

常用选项：

- `-l`：以长格式显示文件详细信息
- `-a`：显示所有文件，包括隐藏文件

例子和输出：

```Shell
$ ls
Documents  Downloads  Pictures  Videos

$ ls -l
total 16
drwxr-xr-x 2 user user 4096 Jul 20 10:00 Documents
drwxr-xr-x 2 user user 4096 Jul 20 10:01 Downloads
drwxr-xr-x 2 user user 4096 Jul 20 10:02 Pictures
drwxr-xr-x 2 user user 4096 Jul 20 10:03 Videos

$ ls -a
.  ..  .bashrc  Documents  Downloads  Pictures  Videos
```

### 2. cd - 切换目录

`cd`命令用于切换当前工作目录。

用法：

```Plain Text
cd [目录]
```

例子和输出：

```Shell
$ pwd
/home/user

$ cd Documents
$ pwd
/home/user/Documents

$ cd ..
$ pwd
/home/user

$ cd ~
$ pwd
/home/user
```

### 3. mkdir - 创建新目录

`mkdir`命令用于创建新的目录。

用法：

```Plain Text
mkdir [选项] 目录名
```

例子和输出：

```Shell
$ ls
Documents  Downloads  Pictures  Videos

$ mkdir NewFolder
$ ls
Documents  Downloads  NewFolder  Pictures  Videos

$ mkdir -p Projects/WebDev
$ ls Projects
WebDev
```

### 4. rm - 删除文件或目录

`rm`命令用于删除文件或目录。

用法：

```Shell
rm [选项] 文件名
```

例子和输出：

```Shell
$ ls
file1.txt  file2.txt  folder1

$ rm file1.txt
$ ls
file2.txt  folder1

$ rm -r folder1
$ ls
file2.txt

$ rm -rf non_existent_file
$ echo $?
0  # 即使文件不存在，使用 -f 选项也不会报错
```

### 5. touch - 创建空文件或更新文件时间戳

`touch`命令用于创建空文件，或者更新已存在文件的访问和修改时间。

用法：

```Shell
touch [选项] 文件名
```

常用选项：

- `-a`：只更改访问时间
- `-m`：只更改修改时间
- `-c`：如果文件不存在，不创建新文件

例子和输出：

1. 创建新文件：

```Shell
$ ls
Documents  Downloads

$ touch newfile.txt
$ ls
Documents  Downloads  newfile.txt

$ ls -l newfile.txt
-rw-r--r-- 1 user user 0 Jul 21 10:00 newfile.txt
```

1. 更新已存在文件的时间戳：

```Shell
$ ls -l existingfile.txt
-rw-r--r-- 1 user user 0 Jul 20 09:00 existingfile.txt

$ touch existingfile.txt
$ ls -l existingfile.txt
-rw-r--r-- 1 user user 0 Jul 21 10:05 existingfile.txt
```

1. 使用`-c`选项避免创建新文件：

```Shell
$ touch -c non_existent_file.txt
$ ls
Documents  Downloads  existingfile.txt  newfile.txt
```

`touch`命令的常见用途：

1. 创建空文件：当你需要一个占位符文件或者准备稍后编辑的文件时，可以使用`touch`快速创建。

1. 更新文件时间戳：在某些情况下，你可能需要更新文件的访问或修改时间，而不改变其内容。

1. 作为文件存在性检查的一部分：在脚本中，`touch`命令常用于确保某个文件存在，如果不存在则创建它。

记住，`touch`命令不会改变文件的内容。如果文件已经存在，它只会更新文件的时间戳；如果文件不存在，它会创建一个空文件。

## 二、文件内容操作命令

### 1. cat - 查看文件内容

`cat`命令用于查看文件内容。

用法：

```Plain Text
cat [选项] 文件名
```

例子和输出：

```Plain Text
$ cat hello.txt
Hello, World!
This is a sample text file.
It has multiple lines.

$ cat -n hello.txt
     1        Hello, World!
     2        This is a sample text file.
     3        It has multiple lines.
```

### 2. head/tail - 查看文件头/尾部

`head`和`tail`命令分别用于查看文件的开头和结尾部分。

用法：

```Plain Text
head [选项] 文件名
tail [选项] 文件名
```

例子和输出：

```Plain Text
$ cat numbers.txt
1
2
3
4
5
6
7
8
9
10

$ head -n 3 numbers.txt
1
2
3

$ tail -n 2 numbers.txt
9
10
```

## 三、系统信息和进程管理命令

### 1. ps - 显示进程状态

`ps`命令用于显示当前系统的进程状态。

用法：

```Plain Text
ps [选项]
```

例子和输出：

```Plain Text
$ ps
  PID TTY          TIME CMD
 1234 pts/0    00:00:00 bash
 5678 pts/0    00:00:00 ps

$ ps -ef | head -n 5
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 Jul19 ?        00:00:03 /sbin/init
root         2     0  0 Jul19 ?        00:00:00 [kthreadd]
root         3     2  0 Jul19 ?        00:00:00 [rcu_gp]
root         4     2  0 Jul19 ?        00:00:00 [rcu_par_gp]
```

### 2. ps -ef | grep - 查找特定进程

`ps -ef | grep`是一个强大的命令组合，用于查找系统中的特定进程。这个命令结合了`ps`和`grep`两个命令的功能。

- `ps -ef`列出所有进程的详细信息
- `|`是管道符，它将`ps`命令的输出传递给`grep`命令
- `grep`用于搜索包含特定字符串的行

用法：

```Plain Text
ps -ef | grep [搜索字符串]
```

例子和输出：

```Plain Text
$ ps -ef | grep firefox
user     3423  3400  5 15:30 ?        00:00:12 /usr/lib/firefox/firefox
user     3628  3423  0 15:30 ?        00:00:00 /usr/lib/firefox/firefox -contentproc -childID 1 -isForBrowser -prefsLen 1 -prefMapSize 231131 -parentBuildID 20230622053201 -appDir /usr/lib/firefox/browser 3423 true tab
user     3868  2498  0 15:32 pts/0    00:00:00 grep --color=auto firefox
```

在这个例子中：

- 第一行和第二行显示了与 Firefox 浏览器相关的进程
- 最后一行是`grep`命令本身的进程（因为它也包含"firefox"这个字符串）

这个命令组合非常有用，特别是在以下情况：

1. 检查特定程序是否正在运行
2. 查找可能导致系统问题的进程
3. 获取进程的 PID（进程 ID），以便进行进一步操作，如终止进程

注意：当使用这个命令时，结果中通常会包含`grep`命令自身的进程。如果你想排除这个结果，可以使用更复杂的命令，如：

```Plain Text
ps -ef | grep [f]irefox
```

这样可以防止`grep`命令匹配到自身。

## 四、文件权限管理命令

### 1. chmod - 修改文件权限

`chmod`命令用于修改文件或目录的权限。

用法：

```Shell
chmod [选项] 模式 文件名
```

例子和输出：

```Plain Text
$ ls -l script.sh
-rw-r--r-- 1 user user 50 Jul 20 11:00 script.sh

$ chmod 755 script.sh
$ ls -l script.sh
-rwxr-xr-x 1 user user 50 Jul 20 11:00 script.sh

$ chmod u+x file.txt
$ ls -l file.txt
-rwxr--r-- 1 user user 20 Jul 20 11:05 file.txt
```

## 五、网络相关命令

### 1. ping - 测试网络连接

`ping`命令用于测试到某个主机的网络连接。

用法：

```Shell
ping [选项] 主机名或IP地址
```

例子和输出：

```Shell
$ ping -c 4 www.example.com
PING www.example.com (93.184.216.34) 56(84) bytes of data.
64 bytes from 93.184.216.34: icmp_seq=1 ttl=56 time=11.6 ms
64 bytes from 93.184.216.34: icmp_seq=2 ttl=56 time=11.8 ms
64 bytes from 93.184.216.34: icmp_seq=3 ttl=56 time=11.7 ms
64 bytes from 93.184.216.34: icmp_seq=4 ttl=56 time=11.7 ms

--- www.example.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 11.648/11.739/11.842/0.070 ms
```

## 写在最后

以上就是一些最常用的Linux命令及其输出示例。

记住，学习Linux命令最好的方法就是多加练习。不要害怕犯错，每个Linux高手都是从新手开始的。

如果你想进一步学习，可以查阅Linux的官方文档或者一些更详细的教程。祝你学习愉快！
