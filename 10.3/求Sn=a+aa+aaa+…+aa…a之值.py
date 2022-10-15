//求Sn = a + aa + aaa + … + aa…a之值，其中a是一个数字。例如：2 + 22 + 222 + … + 22222（此时n = 5），a, n由键盘输入。
#include<iostream>
#include<math.h>
using namespace std;

int main()
{
	long long int a, n, i = 0, Sn = 0;
	cin >> a >> n;
	for (int j = 0; n > 0; n--, j++)
	{
		i = (a * n) * pow(10, j);
		Sn += i;
	}
	cout << Sn << endl;
	return 0;
}


/*
#include <iostream>
using namespace std;
int main()
{
	double a, sn = 0.0, sum = 0.0;
	int n, i;
	cin >> a;
	cin >> n;
	sn = a;
	sum = a;
	for (i = 2; i <= n; i++)
	{
		sum = sum * 10 + a;
		sn += sum;
	}
	cout << sn << endl;
}*/

/*思维局限
第一点 未立刻想到使用循环结构累加数列
第二点 未立刻想到如何表示十的指数
第三点 认为 10^j可以表示10的j次方 最终解决方法：引入#include<math.h>头文件，用pow(10, j)表示10的j次方
*/