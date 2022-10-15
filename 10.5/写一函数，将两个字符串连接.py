//写一函数，将两个字符串连接
#include<iostream>
#include<string>
#include<math.h>
using namespace std;

void connect(string a, string b)
{
	cout << a << b << endl;
}

int main()
{
	string a, b;
	cin >> a >> b;
	connect(a, b);

	return 0;
}


/*
#include<iostream>
using namespace std;
#include<string.h>
int main()
{
const int size=100;
char a[size],b[size];
cin.getline(a,size);
cin.getline(b,size);
strcat(a,b);
cout<<a<<endl;
}*/


/*输出字符串变量不用加双引号
* string a, b;
* cout << a << b << endl;
* 即可
* 给字符串变量赋值要加双引号
* string a, b;
* a="water";
* b="melon";
* */