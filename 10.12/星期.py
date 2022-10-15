/*
2.写一个程序从键盘输入1到7中的某个数字，其中1代表星期天，2代表星期一，3代表星期二等。根据用户输入的数字显示相应的星期几。如果用户输入的数字超出
了1到7的范围，显示输出一个错误提示信息。
* *输入格式要求：整数， 提示信息：cout << "Please input a single numeral(1-7): ";
**输出格式要求："Monday" （星期几的英文单词首字母大写加换行）
*/
#include<iostream>
using namespace std;

int main()
{
	int num = 0;
	cout << "Please input a single numeral(1-7): "<<endl;
	cin >> num;
	switch (num)
	{
		case 1:cout << "Monday" << endl;
			break;
		case 2:cout << "Tuesday" << endl;
			break;
		case 3:cout << "Wednesday" << endl;
			break;
		case 4:cout << "Thursday" << endl;
			break;
		case 5:cout << "Friday" << endl;
			break;
		case 6:cout << "Saturday" << endl;
			break;
		case 7:cout << "Sunday" << endl;
			break;
		default:cout << "输入的数字超出了1到7的范围" << endl;
	}
	return 0;
}