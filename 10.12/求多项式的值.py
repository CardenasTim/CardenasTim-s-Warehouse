/*

5.求多项式 1!+ 2!+ 3!+ …… + 15!的值。
输出格式要求：cout << "s=" << s << endl;

*/
#include<iostream>
using namespace std;

int main()
{

	int n = 15;
	int sum = 0;
	int su = 1;
	for (int i = 1; i <= n; i++)
	{
		su *= i;
		sum += su;

	}
	cout << sum << endl;
	return 0;
}