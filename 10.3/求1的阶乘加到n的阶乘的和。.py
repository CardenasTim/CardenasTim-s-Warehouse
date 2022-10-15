//求1 + 2!+ 3!+ ... + n!的和。

#include<iostream>
using namespace std;

int main()
{
	int n = 0;
	int sum = 0;
	int su = 1;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		su *= i;
		sum += su;

	}
	cout << sum << endl;
	return 0;
}

/*
#include<iostream>
using namespace std;
int main()
{
	int i,n;
	cin>>n;
	long double sum,mix;
	sum=0,mix=1;
	for(i=1;i<=n;i++)
	{
		mix=mix*i;
		sum=sum+mix;
	}
	cout<<sum;
}*/