//将一个数组中的值按逆序重新存放，例如，原来顺序为：a、b、c、d。要求改为：d、c、b、a。

#include <iostream>
using namespace std;


int main()
{
	char str[1000];
	cin.get(str, 1000);
	int start = 0;

	int number = strlen(str) - 1;
	for (int i = 0; i < number; i++)
	{
		while (start < number)
		{
			int temp = str[start];
			str[start] = str[number];
			str[number] = temp;
			start++;
			number--;
		}
	}

	cout << str << endl;
	return 0;
}
/*
#include<iostream>
using namespace std;
void back(char *);
int main()
{
char a[50];
cin.getline(a,50);
back(a);
}
void back(char *p)
{
int i=0;
while(*p!='\0')
{
p++;//把指针定位到字符串末尾
i++;//统计字符个数
}
cout<<"a=";
for(;i>0;i--)//逆序输出
{
p--;
cout<<*p;
}
cout<<endl;
}*/

/*
 1.通过字符数组表示字符串,用strlen(str)以达到统计字符个数作用
*/