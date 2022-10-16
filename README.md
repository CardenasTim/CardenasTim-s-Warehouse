# CardenasTim-s-Warehouse
任务清单：
- [ ] C++基础任务
- [ ] ROS2基础任务
- [ ] 基础知识框架：C++、Python、Cmake、Linux、ROS2、docker、github
- [ ] 拟真开发:Gazebo（edifice）、RVIZ
- [ ] slam开发:《视觉slam十四讲》


学习记录：

| 日期| 学习过程（关键信息：知识点、技能 查阅平台 链接）| 遇到问题（关键信息：自己没想通的问题点）|解决过程（关键信息：分析思路、与别人的交流）|收获|
|--------|--------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|-------------------------------|
|9.31|c++知识学习完成结构体前所有c++语法学习||||
|10.1|c++案例学习：1.最简单算法冒泡排序 2.给出年、月、日，计算该日是该年的第几天|  2.对闰年定义理解有偏差（2100年的日期算错）  |2. 百度搜索解决|2.第一点 代码冗杂 应构想用数组与循环输出月份 第二点 发现新思路 可以用goto语句跳出嵌套循环 第三点 将判断闰年写为函数 结构会更清晰
|10.2|c++案例学习：1.将一个数组中的值按逆序重新存放，例如，原来顺序为：a、b、c、d。要求改为：d、c、b、a 2.将一个正整数分解质因数。例如 输入90, 打印出90 = 2乘3乘3乘5|1.如何统计字符个数 2.第一点如何消除最后一个*  第二点 for (int i = 2; i <= PrimeFactor; i++ )将i赋值为二放在了i++前，使得i取值错误|1.通过字符数组表示字符串,用strlen(str)以达到统计字符个数作用2.使用goto语句if (PrimeFactor == 1){goto FLAG;}else{cout << "星号";}|1.学会了strlen和cin.get的用法
|10.3|c++案例学习：1.求1的阶乘加到n的阶乘的和。 2.求Sn=a+aa+aaa+…+aa…a之值| 2.错误地认为 10^j可以表示10的j次方|2.  引入#include<math.h>头文件，用pow(10, j)表示10的j次方 |
|10.4|c++案例学习：1.输入一个华氏温度，要求输出摄氏温度。公式为  输出要求有文字说明，取2位小数。 2.写两个函数，分别求两个整数的最大公约数和最小公倍数，用主函数调用这两个函数，并输出结果，两个整数由键盘输入。|  | | 
|10.5|c++案例学习：1.写一函数，将两个字符串连接 2.写一函数，输入一个四位数字，要求输出这4个数字字符，但每两个数字间空一空格|  | | 2.将一个整型数取模于十，除以十取模于十，除以一百取模于十......可以得到该数的个位 十位 百位......
|10.6|c++案例学习：1.有n个人围成一圈，顺序排号。从第1个人开始报数（从1到3报数），凡报到3的人 退出圈子 ，直到只剩一人，问最后留下的是原来第几号的那位|构思思路不清晰|1.圈出题目中的关键词如“退出圈子”“报数”“排号”	2.将题目中的数据抽象为概念（如行数，列数，号码等有规律的名词），并创建变量，找出变量间的关系，或者变量的变化趋势	3.将数据取值范围抽象，写出变量取值范围	4.开始写题纲（伪代码）	有些操作利用已有变量无法完成时，可以创建新的概念（变量）完成操作	将一个完整循环语句或条件语句用方框框住，这样语句与语句间的思路就会非常清晰| 	1.对变量赋值，进行逻辑运算，可以达到“退出圈子”的操作	2.如果输入n，再创建n个数的数组较难，不妨直接创建一个较大容量的数组	3.剩余人数可以用于决定是否退出循环	4.将报号人序号i和报的号码j区分，前期两个变量的变化相同，但后期报号人序号i大于等于n时要重新从0开始，与报的号码变化不同	5.写复杂代码切忌边写边想，容易1被噪音打断思路，2不易查错漏点
|10.7|解决10.6c++案例学习的其中一个问题：如何输入n，再创建n个数的数组|如何输入n，再创建n个数的数组|与c++老师请教 老师推荐使用百度搜索：动态内存分配|C++语言中，我们可以使用指针的方法建立一维或二维动态数组 也可以通过结构体创建动态结构体数组（10.7代码参考自csdn@hust_xiaowei）
|10.8|放假|  | | 
|10.9|学习线性代数|  | | 
|10.10|学习高数|  | | 
|10.11|学习高数|  | | 
|10.12|c++案例学习：1.百万富翁破产 2.素数和 3.自然数的立方和 4.里氏震级 5.求多项式的值 6.星期|1.计算正确 但输出错误  |1.自己检查代码 发现cout默认输出有效数字为7位，实际需要输出的位数为10位 | 可以用setprecision( )实现高精度输出




## 背景


## 安装

（环境配置和代码部署）


## 使用说明



## 徽章


## 示例



## 相关仓库

- A
- B
- C

## 维护者



## 如何贡献

非常欢迎你的加入！提一个 Issue或者提交一个 Pull Request。


### 贡献者

感谢以下参与项目的人：



## 使用许可
