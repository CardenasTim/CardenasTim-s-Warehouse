#include<iostream>
#include<string>
#include<ctime>
#include"Base_Robot.h"
#include"Referee.h"

using namespace std;

//机器人属性结构体
struct Robot
{
	int HP=200;
	string name;
};

//攻击数值结构体
struct AttackValue
{
	const int shoot = 10;
	const int no = 0;
	const int bomb = 40;
};

//基础机器人类
class Base_Robot
{
	friend class Referee;
public:
	Base_Robot(string name)//命名析构函数
	{
		m_robot.name = name;
	}
	void GunShooting()
	{
		srand((unsigned int)time(NULL));//添加随机数种子
		int num = rand() % 100 + 1;//生成随机数

		if (num % 3 == 0)
		{
			if (num % 2 == 0)
			{
				m_robot.HP -= hurt.no;
				m_behavior = 0;
			}
			else
			{
				m_robot.HP -= hurt.shoot;
				m_behavior = 1;
			}
		}
		if (num % 3 != 0)
		{
			if (num % 2 == 0) 
			{
				m_robot.HP -= hurt.no;
				m_behavior = 0;
			}
			else
			{
				m_robot.HP -= hurt.bomb;
				m_behavior = 2;
			}
		}
		//随机数如果是3的倍数，则打出子弹，如果是2的倍数则没有子弹打出。如果既不是3的倍数也不是2的倍数，则炸膛。如
		//果是3和2的公倍数，则没有子弹打出
	}
protected:
	Robot m_robot;//机器人属性
	AttackValue hurt;//攻击数值
	int m_behavior;//判断行为 0.没有子弹 1.打出子弹 2.炸膛
	//轮换枪权：如果子弹正常发出或者没有发出，持枪方轮流替换。2不换，0、1换
};

//裁判系统类
class Referee
{
public:
	bool end = true;//判断游戏是否结束
	bool holder=true;//持枪方是否轮换
	void Set(Base_Robot &robot1, Base_Robot& robot2)//输出双方操作和血量
	{
		if (robot1.m_behavior == 2)
			cout << "操作为炸膛" << endl;
		else if (robot1.m_behavior == 1)
			cout << "操作为打出子弹";
		else
			cout << "操作为没有子弹";
		cout << "robot1血量为" << robot1.m_robot.HP;
		cout << "robot2血量为" << robot2.m_robot.HP;
	}

	void Isend(Base_Robot& robot1, Base_Robot& robot2)//判断游戏是否结束
	{
		if (robot1.m_robot.HP <= 0 && robot2.m_robot.HP <= 0)
			bool end = false;
	}

	int ChangeHolder(Base_Robot& robot1, Base_Robot& robot2)//持枪方轮换
	{
		if (robot1.m_behavior == 2)
			holder = true; 
		else
			holder = false;


		return holder;
	}
};
int main()
{
	Base_Robot robot1("robot1");//创建机器人
	Base_Robot robot2("robot2");
	Referee referee;

	while (referee.end)//进入循环
	{
		void GunShooting();//打枪

	}
	return 0;
}