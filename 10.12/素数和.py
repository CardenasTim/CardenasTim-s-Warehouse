/*

6. 求1至200之间的所有质数，将质数和存入变量 sum 中并输出。
质数（素数）的说明：“质数是只能被1和其本身整除的数”。
输入提示要求：无
输出结果格式要求：质数之间以一个空格隔开
输出所有质数后换行输出：sum = 4227

*/
#include<iostream>
using namespace std;

int main()
{
	int sum = 0;
	int b = 0;
	for (int i = 2; i<=200; i++)
	{
		b = 0;
		for (int j = 2; j < i; j++)
		{
			if (i % j == 0)b = 1;

		}
		if (b == 0)
		{
			sum += i;
			cout << i << " ";
		}
	}
	cout << endl << "sum=" << sum;
	return 0;
}