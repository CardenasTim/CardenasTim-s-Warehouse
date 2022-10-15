//将一个正整数分解质因数。例如：输入90, 打印出90 = 2 * 3 * 3 * 5。
#include<iostream>
using namespace std;

int main()
{
	int PrimeFactor = 0;
	cin >> PrimeFactor;
	cout << PrimeFactor << "=";
	for (int i = 2; i <= PrimeFactor; )
	{
		if (PrimeFactor % i == 0)
		{
			PrimeFactor /= i;
			cout << i;

			if (PrimeFactor == 1)
			{
				goto FLAG;
			}
			else
			{
				cout << "*";
			}
			i = 2;
		}
		else
			i++;
	}
FLAG:
	return 0;
}

/*
#include<iostream>
using namespace std;
void change(int a[],int n);
int main()
{
int n,i;
cin>>n;
cout<<n<<"=";

for(i=2;i<=n;i++) {
while(n!=i){
if(n%i==0)
{cout<<i<<"*";
n=n/i;}
else break;
}
}
cout<<n;
}*/

/*
第一点 未立刻想到如何消除最后一个*
			if (PrimeFactor == 1)
			{
				goto FLAG;
			}
			else
			{
				cout << "*";
			}
第二点 if (PrimeFactor == i)
第三点 for (int i = 2; i <= PrimeFactor;i++ )
将i赋值为二放在了i++前，使得i取值错误
*/