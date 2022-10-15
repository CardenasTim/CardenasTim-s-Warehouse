//写两个函数，分别求两个整数的最大公约数和最小公倍数，用主函数调用这两个函数，并输出结果，两个整数由键盘输入。

#include<iostream>
#include<math.h>
using namespace std;
int GCD(int num1, int num2);
int LCM(int num1, int num2);

int main()
{
	int num1, num2, gcd, lcm;
	cin >> num1 >> num2;
	gcd = GCD(num1, num2);
	lcm = LCM(num1, num2);
	cout << "common divisor is " << gcd << endl;
	cout << "common multiple is " << lcm << endl;
	return 0;
}

//最大公约数
int GCD(int num1, int num2)
{
	int small = min(num1, num2);
	int gcd = 0;
	for (int i = 1; i <= small; i++)
	{
		if (num1 % i == 0 && num2 % i == 0)
		{
			gcd = i;
		}
	}
	return gcd;
}
//最小公倍数
int LCM(int num1, int num2)
{
	int small = min(num1, num2);
	int gcd = 0;
	for (int i = 1; i <= small; i++)
	{
		if (num1 % i == 0 && num2 % i == 0)
			gcd = i;
	}
	int lcm = num1 * num2 / gcd;
	return lcm;
}

/*
#include<iostream>
using namespace std;
int cdivisor(int,int);
int cmultiple(int,int,int);
int main()
{
	int x,y,d,m;
	cin>>x>>y;
	d=cdivisor(x,y);
	m=cmultiple(x,y,d);
	cout<<"common divisor is "<<d<<endl<<"common multiple is "<<m<<endl;
}

int cdivisor(int x1,int y1)//最大公约数
{
	int r,temp;
	if (x1<y1)
	{
		temp=x1;
		x1=y1;
		y1=temp;
	}
	while(x1%y1)//当较大数除以较小数余数等于0时，较小数为最大公约数
	{
		r=x1%y1;
		x1=y1;
		y1=r;
	}
	return y1;
}

int cmultiple(int x2,int y2,int d1)//最小公倍数
{
	return x2*y2/d1;//两数相乘结果除以它们的最大公约数为最小公倍数
}*/

/*
第一点
错误代码：
int gcd = 0;
for (int i = 1，gcd; i <= small; i++)
该代码在编写时不会报错，在程序运行的错误列表中，报错位置也不在该修改的位置，因此极难发现错误
启发：在循环内递增或递减的数 在循环语句内定义 否则在循环语句外定义

第二点
对函数的声明、引用、定义掌握不熟练

思路差异
1.
*/