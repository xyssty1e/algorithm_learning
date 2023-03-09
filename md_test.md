<!-- TOC depthFrom:2 depthTo:4 -->

- [markdown语法学习](#markdown语法学习)
    - [基础语法](#基础语法)
        - [三级标题](#三级标题)
            - [四级标题](#四级标题)
                - [五级标题](#五级标题)
                    - [六级标题](#六级标题)
    - [高级用法](#高级用法)
        - [目录TOC](#目录toc)
        - [LaTeX公式](#latex公式)
        - [流程图](#流程图)
        - [序列图](#序列图)
        - [甘特图](#甘特图)
        - [html标签](#html标签)
        - [待办事宜 ToDo](#待办事宜-todo)
        - [](#)

<!-- /TOC -->

# markdown语法学习

## 基础语法

### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题

换行操作  
行尾添加两个空格  
行尾添加<br>

*斜体*  
_斜体_  
**粗体**  
__粗体__  
~~删除线~~  


[百度链接](https://www.baidu.com)

无序列表
* a
* b
* c
 
+ a
+ b

- a
- b

有序列表
1. a
2. b
3. c

> 一级引用
> > 二级引用
> > > 三级引用

`行内代码`

    代码块

高亮代码
```python
class A:
    def __init__(self):
        pass
```
```cpp

# include <iostream>
# incluce <string>
using namespace std;

int main() {
    return 0;
}
```

图片展示

![描述](./ball.png)

html展示图片，可以调整显示大小，居中
<div align="center">
    <img height=50px src="./ball.png">
</div>


表格  
|名称|价格|数量|
|:-:|:-|-:|
|香蕉|3|1|
|苹果|5|1|
|泰国榴莲|8|1|


脚注[^1]   


分隔线
----------
**********

## 进阶用法

### 目录TOC
vscode可以安装插件Markdown TOC，作者CharlesWan；setting的EOL设置为\n  
两个功能设置：
- 生成的标题栏不带跳转链接  
    `<!-- TOC withLinks:false -->`
- 指定目录深度  
    `<!-- TOC depthFrom:2 depthTo:4 -->`

### LaTeX公式
行内  
质能转换公式 $E=mc^2$  

整行
$$\sum^n_{i=1} a_i^2 = 0$$
$$f(x_1, x_2, \ldots, x_n) = x_1^2 + x_2^2 + \cdots + x_n^2 $$  
$$\sum^{j-1}_{k=0}{\widehat{\gamma}_{kj} z_k \alpha_k \beta^2 \sigma}$$  


### 流程图
```flow
st=>start: Start:>https://www.zybuluo.com
io=>inputoutput: verification
op=>operation: Your Operation
cond=>condition: Yes or No?
sub=>subroutine: Your Subroutine
e=>end

st->io->op->cond
cond(yes)->e
cond(no)->sub->io
```


### 序列图
```seq
Alice->Bob: Hello Bob, how are you?
Note right of Bob: Bob thinks
Bob-->Alice: I am good thanks!
```


### 甘特图
```gantt
    title 项目开发流程
    section 项目确定
        需求分析       :a1, 2016-06-22, 3d
        可行性报告     :after a1, 5d
        概念验证       : 5d
    section 项目实施
        概要设计      :2016-07-05  , 5d
        详细设计      :2016-07-08, 10d
        编码          :2016-07-15, 10d
        测试          :2016-07-22, 5d
    section 发布验收
        发布: 2d
        验收: 3d
```


### html标签
<table>
    <tr>
        <th rowspan="2">值班人员</th>
        <th>星期一</th>
        <th>星期二</th>
        <th>星期三</th>
    </tr>
    <tr>
        <td>李强</td>
        <td>张明</td>
        <td>王平</td>
    </tr>
</table>


### 待办事宜 ToDo
- [ ] **abc**
  - [x] x
  - [ ] y
  - [ ] z



[博文1](https://www.zybuluo.com/mdeditor)  
[博文2](https://www.zybuluo.com/mdeditor?url=https://www.zybuluo.com/static/editor/md-help.markdown)



[^1]: 这是一个脚注的文本。
