#include<iostream>
using namespace std;

int main()
{
	long int arr[] = { 4,2,8,0,5,7,1,3,9 };
	int n = sizeof(arr)/sizeof(arr[0]);
	cout << n;
	for (int j = n - 1; j > 0; j--)
	{
		for (int i = 0; i <j; i++)//多一个等于号会报错
		{
			if (arr[i] > arr[i + 1])
			{
				int temp = arr[i];
				arr[i] = arr[i + 1];
				arr[i + 1] = temp;
			}
		}
	}
	for (int i = 0; i < n; i++)
	{
		cout << arr[i];
	}

	return 0;
}