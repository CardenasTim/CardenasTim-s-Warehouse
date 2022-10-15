/*
3.有一天，一位百万富翁遇到一个陌生人，陌生人找他谈一个换钱的计划，陌生人对百万富翁说：“我每天给你10万元，而你第一天只需给我1分钱，第二天我仍给
你10万元，你给我2分钱，第三天我仍给你10万元，你给我4分钱……。你每天给我的钱是前一天的两倍，直到满一个月（30天）为止”，百万富翁很高
兴，欣然接受了这个契约。请编程计算在这一个月中陌生人总计给百万富翁多少钱，百万富翁总计给陌生人多少钱。
* *输入提示信息和数据格式：无
* *输出提示信息和数据格式：
cout << "百万富翁给陌生人:" << toStranger << "元" << endl;
cout << "陌生人给百万富翁:" << toRichman << "元" << endl;
*/
#include<iostream>
#include<cmath>
#include<iomanip>
using namespace std;

int main()
{
	int toRichman = 100000 * 30;
	long double toStranger = 0;
	long double j = 0;
	for (int i = 0; i < 30; i++)
	{
		j = 0.01 * pow(2, i);
		toStranger += j;
	}
	cout << "百万富翁给陌生人:" << setprecision(10) << toStranger << "元" << endl;
	cout <<"陌生人给百万富翁:"  << toRichman << "元" << endl;
	
	return 0;
}
/*
cout << setprecision(10) << y;
long double y = 0.01 * (pow(2, 30) - 1);
*/