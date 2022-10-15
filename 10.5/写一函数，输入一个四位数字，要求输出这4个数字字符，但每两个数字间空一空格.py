//写一函数，输入一个四位数字，要求输出这4个数字字符，但每两个数字间空一空格

#include<iostream>
using namespace std;

int main()
{
	int num, a, b, c, d;
	cin >> num;
	a = num % 10;
	b = num / 10 % 10;
	c = num / 100 % 10;
	d = num / 1000 % 10;
	cout << d << " " << c << " " << b << " " << a << " " << endl;

	return 0;
}

/*
#include<iostream>
using namespace std;
#include<string.h>
void outs(char a[]);
int main()
{
const int size=10;
char a[size];
cin.getline(a,size);
outs(a);
}
void outs(char a[10])
{
int i;
if(strlen(a)<=4)
{
for(i=0;i<4;i++)
cout<<a[i]<<" ";
}
else cout<<"input error."<<endl;
}
*/

//输出时 abcd顺序别弄混