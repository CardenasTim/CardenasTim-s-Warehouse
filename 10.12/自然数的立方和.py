/*

4.编程计算自然数的立方和，直到立方和大于等于1000000时为止。统计并输出实际累加的项数。
输出格式要求：cout << "sum=" << sum << endl;
cout << "count =" << i << endl;
输出结果为: sum = 1071225
count = 45

*/
#include<iostream>
using namespace std;

int main()
{
	int i = 1;
	int sum = 0;
	for (; sum <= 1000000; i++)
	{

		sum += pow(i, 3);
	}
	i--;
	cout << "sum=" << sum << endl;
	cout << "count =" << i << endl;
	
	return 0;
}

//代码中的i在判断条件前被加多了一次 很阴险！