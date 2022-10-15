/*1 写一个程序根据从键盘输入的里氏强度显示地震的后果。根据里氏强度地震的后果如下：
里氏强度	        后果
小于4			很小
4.0到5.0		窗户晃动
5.0到6.0		墙倒塌；不结实的建筑物被破坏
6.0到7.0		烟囱倒塌；普通建筑物被破坏
7.0到8.0		地下管线破裂；结实的建筑物也被破坏
超过8.0			地面波浪状起伏；大多数建筑物损毁

* *输入格式要求：实数， 提示信息：cout << "请输入地震的里氏强度: " << endl;
**输出格式要求：
"本次地震后果：很小！"
"本次地震后果：窗户晃动！"
"本次地震后果：墙倒塌；不结实的建筑物被破坏！"
"本次地震后果：烟囱倒塌；普通建筑物被破坏！"
"本次地震后果：地下管线破裂；结实的建筑物也被破坏！"
"本次地震后果：地面波浪状起伏；大多数建筑物损毁！"
*/
#include<iostream>
using namespace std;

int main()
{
	float Mag= 0;
	cout << "请输入地震的里氏强度: " << endl;
	cin >> Mag;
	if (Mag < 4.0)cout << "本次地震后果：很小！" << endl;
	else if(Mag < 5.0&& Mag >= 4.0)cout << "本次地震后果：窗户晃动！" << endl;
	else if (Mag < 6.0 && Mag >= 5.0)cout << "本次地震后果：墙倒塌；不结实的建筑物被破坏！" << endl;
	else if (Mag < 7.0 && Mag >= 6.0)cout << "本次地震后果：烟囱倒塌；普通建筑物被破坏！" << endl;
	else if (Mag < 8.0 && Mag >= 7.0)cout << "本次地震后果：地下管线破裂；结实的建筑物也被破坏！" << endl;
	else if (Mag >= 8.0)cout << "本次地震后果：地面波浪状起伏；大多数建筑物损毁！" << endl;
	return 0;
}