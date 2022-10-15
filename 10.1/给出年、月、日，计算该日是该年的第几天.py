//给出年、月、日，计算该日是该年的第几天。

#include<iostream>
using namespace std;

int main()
{
	int year, month, day, date = 0;
	cin >> year >> month >> day;

	if ((year % 4) == 0)
	{
		if (((year % 100) == 0) && ((year % 400) != 0))
		{
			goto FLAG;
		}
		switch (month)
		{
		case 1:
			date = day;
			break;
		case 2:
			date = day + 31;
			break;
		case 3:
			date = day + 31 + 29;
			break;
		case 4:
			date = day + 31 + 29 + 31;
			break;
		case 5:
			date = day + 31 + 29 + 31 + 30;
			break;
		case 6:
			date = day + 31 + 29 + 31 + 30 + 31;
			break;
		case 7:
			date = day + 31 + 29 + 31 + 30 + 31 + 30;
			break;
		case 8:
			date = day + 31 + 29 + 31 + 30 + 31 + 30 + 31;
			break;
		case 9:
			date = day + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31;
			break;
		case 10:
			date = day + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 31;
			break;
		case 11:
			date = day + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 31 + 30;
			break;
		case 12:
			date = day + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 31 + 30 + 31;
			break;
		}
	}
	else
	{
	FLAG:
		switch (month)
		{
		case 1:
			date = day;
			break;
		case 2:
			date = day + 31;
			break;
		case 3:
			date = day + 31 + 28;
			break;
		case 4:
			date = day + 31 + 28 + 31;
			break;
		case 5:
			date = day + 31 + 28 + 31 + 30;
			break;
		case 6:
			date = day + 31 + 28 + 31 + 30 + 31;
			break;
		case 7:
			date = day + 31 + 28 + 31 + 30 + 31 + 30;
			break;
		case 8:
			date = day + 31 + 28 + 31 + 30 + 31 + 30 + 31;
			break;
		case 9:
			date = day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31;
			break;
		case 10:
			date = day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 31;
			break;
		case 11:
			date = day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 31 + 30;
			break;
		case 12:
			date = day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 31 + 30 + 31;
			break;
		}
	}
	cout << "你输入的日期是当年的第" << date << "天" << endl;
	return 0;
}

/*答案：
#include<iostream>
using namespace std;
 int lead(int);
 int main()
 {
 int ly,year,month,date,i,sum=0;
 cin>>year>>month>>date;
 int a[12]={31,0,31,30,31,30,31,31,30,31,30,31};
 ly=lead(year);
 if (ly==1)
 a[1]=29;//366天
 else a[1]=28;//365天
 for(i=0;i<month-1;i++) //当前月之前所有月天数累加和
 sum+=a[i];
 sum+=date; //加上当前月天数
 cout<<"你输入的日期是当年的第"<<sum<<"天";
 }
 int lead(int y)//判断闰年
 {
 if((y%4==0&&y%100!=0)||(y%400==0)) return 1;//是闰年
 else return 0;//不是闰年
 }*/

 /*
   第一点 代码冗杂 未构想用数组与循环输出月份
   第二点 对闰年定义理解有偏差
   第三点 用goto语句跳出嵌套循环 思路新颖
   第四点 将判断闰年写为函数 结构会更清晰
 */