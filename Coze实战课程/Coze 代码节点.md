---
title: "Coze 代码节点"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/CUqtwHxZ5iTbHbkglHEcKGmnn1e
node_token: CUqtwHxZ5iTbHbkglHEcKGmnn1e
obj_token: SGDzdr8qSo6uh1x2OBPcHUhOnFt
obj_type: docx
space_id: 7345704071740817411
space_name: "Coze 代码节点"
depth: 0
breadcrumb:
  - "Coze 代码节点"
obj_create_time: 1718600443
obj_edit_time: 1718606934
creator: ou_42f81f09eb31290df2b37914c257f875
owner: ou_42f81f09eb31290df2b37914c257f875
revision_id: 938
from_group_share: true
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - Coze 代码节点
---

# Coze 代码节点

# 自我介绍

我是一个电商和供应链产品经理，不是很懂代码，前段时间刚接触了coze，发现要稳定输出还是得会code节点的使用，所以自学了python的基础语法，我先把学习资料分享下：

1. [先导篇 | 为什么做这个教程，UP主是闲得发慌吗_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1944y1x7SW/?p=1&vd_source=e94f42ead4c2e95f4b13bec257d95670)
2. w3school的python教程：https://www.w3school.com.cn/python/index.asp

# 正文

前置知识大伙了解之后，基础语法就会了，剩下的不需要在基础部分死磕，直接上项目就行了。这里我来解释下coze里面代码节点中的示例代码是什么意思，先上示例代码：

```Python
async def main(args: Args) -> Output:
    params = args.params
    ret: Output = {
        "key0": params['input'] + params['input'],
        "key1": ["hello", "world"],
        "key2": {
            "key21": "hi"
        },
    }
    return ret
```

相信大家和我一样，一上来是懵的，没关系，我会一点一点给大家解释这段代码的含义。首先先说下方法论，也就是我自己是怎么弄清楚这段代码的，答案是通过gpt4来一点一点了解，大家可以试试。

## 整个代码解释

```Plain Text
这是一段Python的异步函数代码，我逐行来解释一下：
async def main(args: Args) -> Output: 这是一个异步函数的定义，名为main，接收一个名为args的参数，参数类型为Args，返回值类型为Output。
params = args.params 这一行从args中获取params的值，并将它赋给变量params。
ret: Output = { 这一行定义了一个名为ret的变量，类型为Output，并初始化为一个字典。
"key0": params['input'] + params['input'], 这一行在字典ret中创建了一个键为key0的项，值为params['input']的两倍。
"key1": ["hello", "world"], 这一行在字典ret中创建了一个键为key1的项，值为一个包含两个字符串"hello"和"world"的列表。
"key2": { 这一行在字典ret中创建了一个键为key2的项，值为一个新的字典。
"key21": "hi" 这一行在key2对应的字典中创建了一个键为key21的项，值为字符串"hi"。
}, 这一行表示key2对应的字典结束。
} 这一行表示字典ret的定义结束。
return ret 这一行表示函数返回ret这个字典。
```

看不懂没关系，我会一段一段解释。

## 第一段

```Python
async def main(args: Args) -> Output:
```

**async：**在Python中，`async`是"asynchronous"的缩写，意为“异步的”。在编程中，异步通常指的是能够在等待某些操作（如I/O操作）完成的同时，继续执行其他代码的能力，注意这是固定写法。

当你看到一个函数定义以`async def`开始，这意味着这个函数是一个“协程”（coroutine）。协程是可以在任何时候暂停和恢复的函数，它们是异步编程的核心。

在这种情况下，`async def main(args: Args) -> Output:`定义了一个异步的`main`函数，这意味着这个函数可以在等待某些操作完成的同时，执行其他代码。这样可以提高程序的整体性能，特别是在处理I/O密集型任务（如网络请求或读写文件）时。

**def：**这个不用多说了吧，就是函数声明。

**main函数：**这里的main函数是用户自定义的。在Python中，函数名是可以自由设定的，只要遵守命名规则（例如，不能以数字开头，不能包含空格或特殊字符等）。在这个例子中，函数名为main，但它可以被任何其他有效的Python标识符替换。也就是可以换成其他任何名字，不是固定的。

需要注意的是，虽然main在许多编程语言（如C，C++，Java）中是程序执行的入口点，但在Python中并没有这样的规定。在Python中，main只是一个常见的函数名，没有特殊含义。如果你想在Python程序中设定一个执行入口点，通常会使用if **name** == "\_\_main\_\_":这样的结构。

**(args: Args)：**args是arguments的缩写，意为"参数"，args可以写成任何其他字符，只是约定俗称用args而已。<: Args>是一个类型注解，表示args应该是Args类型。Args可能是一个自定义的类或者数据类型，具体取决于代码的其他部分。类型注解在Python中并不会强制执行，它们主要用于提高代码的可读性和可维护性，同时也能被一些IDE和工具用于类型检查，帮助开发者更早地发现潜在的错误，也就是说它只是一个注释，可以去掉。

**-> Output：**这也是一个类型注释，在Python中，你可以使用->语法在函数定义中指定返回值的类型，这样做可以帮助理解函数的期望输出，不参与代码执行。

所以以上代码可以简化为如下，也就是一个函数的代码入口

```Python
async def main(args):
```

## 第二段

```Python
params = args.params
    ret: Output = {
        "key0": params['input'] + params['input'],
        "key1": ["hello", "world"],
        "key2": {
            "key21": "hi"
        },
    }
```

**params = args.params：**代表将args对象的params属性赋值给这个函数中的params变量，params可以写成其他任何字符，这里是定义变量环节。从代码中可以猜测，在上文Args类的定义中，存在params这个属性且可能是一个字典。

**ret：Output：**ret通常是return的缩写，用于表示函数的返回值。这是一种常见的命名约定，特别是在需要存储或处理函数返回值的情况下。所以，ret在这里是用来存储并最终返回函数结果的变量。<: Output>同上文一样，是一个类型注解，不参与实际代码执行，是用来帮助程序员阅读代码用的，这里表示ret这个变量可能是和Output类一样的返回类型，从结果看是字典。

**{ XXX }：**大括号中的内容就是具体的字典内容，在这里面可以将用户输入的参数值通过一定计算返回给ret的键 key0,key1,key2，这里的key0,key1,key2对应输出的变量名。

![图片展示了Coze代码节点的界面及代码示例。左侧为输入、代码、输出区域，输入部分有input1和input2两个输入框，代码区域显示Python代码，输出部分有key0、key1、key21三个变量。右侧是代码编辑区域，代码内容为定义一个名为main的异步函数，接收args参数，返回Output类型，其中key0等于params\['input'\]加params\['input'\]，key1为字典，key21为字符串“hi”，最后返回ret。该图片与文档中解释代码节点处理输入生成返回值的内容相关，直观呈现了代码节点的代码示例及运行结果。](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MzJjNTAwYWQ0NGE3Y2I3OTVkMjEwZDBlZGE5ZDhmZjVfZmE3YjAxYWRjNDg5M2IzYzA0ZGM4MDVlMjA3MmI0NWFfSUQ6NzM4MTM1MjMyMDM0NjkxNDg0NF8xNzg1Mjk5NjUyOjE3ODUzMDMyNTJfVjM)

我举其中一个key0 = params['input'] + params['input']来解释下，实际上为key0 = params['input1'] + params['input2']，key0代表输出变量，这里可以自定义变量名，代码中同步即可。params['input1']代表取params字典中key=input1的value值，对应的就是输入框中，参数名为input1后面的参数值value1，两者相加在此仅是做了一个例子，代表value1+value2，最终将结果复制给key0的值中。

其他key1、key2在此也只是举了几个例子，key1的值是一个字符串列表，key2的值是另一个字典，在这里只是示例而已，不用太在意。

## 第三段

return ret：这个应该都看得懂，就是把ret的值返回给main函数供其他代码调用。

# 总结

## 这段代码的简化形式

```Python
async def main(args):
    params = args.params
    ret = {
        "key0": params['input'] + params['input'],
        "key1": ["hello", "world"],
        "key2": {
            "key21": "hi"
        },
    }
    return ret
```

## 该代码是代码片段，猜测上下文后可能的代码

```Python
# 我们可以假设Args是一个具有params属性的类，params可能是一个字典。
class Args:
    def __init__(self, params):
        self.params = params

# 这是给出的异步函数
async def main(args):
    params = args.params
    ret = {
        "key0": params['input'] + params['input'],
        "key1": ["hello", "world"],
        "key2": {
            "key21": "hi"
        },
    }
    return ret

# 这是一个可能的使用方式
if __name__ == "__main__":
    import asyncio

    # 创建一个Args实例
    args = Args(params={'input': 'test'})

    # 运行main函数并打印结果
    print(asyncio.run(main(args)))
```

## 后续具体使用

在{ }中操作，填写输入变量、计算方式，最后赋值给输出变量，{ }以外的部分不需要变动。
