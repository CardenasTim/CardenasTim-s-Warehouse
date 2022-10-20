#include<iostream>
#include<string>
#include<ctime>
#include<cstdlib> // rand()和srand() 包含在这个库中
using namespace std;

//机器人属性结构体
struct Robot
{
	int HP = 200;
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
	bool holder = true;//持枪方是否轮换

	void GunShooting(Base_Robot& robot,int num)//打枪
	{
		

		if (num % 3 == 0)
		{
			if (num % 2 == 0)
			{
				robot.m_robot.HP -= robot.hurt.no;
				robot.m_behavior = 0;
			}
			else
			{
				robot.m_robot.HP -= robot.hurt.shoot;
				robot.m_behavior = 1;
			}
		}
		if (num % 3 != 0)
		{
			if (num % 2 == 0)
			{
				robot.m_robot.HP -= robot.hurt.no;
				robot.m_behavior = 0;
			}
			else
			{
				robot.m_robot.HP -= robot.hurt.bomb;
				robot.m_behavior = 2;
			}
		}
		//随机数如果是3的倍数，则打出子弹，如果是2的倍数则没有子弹打出。如果既不是3的倍数也不是2的倍数，则炸膛。如
		//果是3和2的公倍数，则没有子弹打出
	}
	void Set(Base_Robot& robot1, Base_Robot& robot2)//输出双方操作和血量
	{
		if (robot1.m_behavior == 2)
			cout << "操作为炸膛" ;
		else if (robot1.m_behavior == 1)
			cout << "操作为打出子弹";
		else
			cout << "操作为没有子弹";
		cout << "robot1血量为" << robot1.m_robot.HP;
		cout << "robot2血量为" << robot2.m_robot.HP<<endl;
	}

	void Isend(Base_Robot& robot1, Base_Robot& robot2)//判断游戏是否结束
	{
		if ((robot1.m_robot.HP <= 0 )|| (robot2.m_robot.HP <= 0))
			end = false;//加多了个bool使得end变为局部变量，导致循环无法退出
	}

	void ChangeHolder(Base_Robot& robot)//持枪方轮换
	{
		if (robot.m_behavior == 2)
			holder = true;
		else
			holder = false;


	}
};
int main()
{
	Base_Robot robot1("robot1");//创建机器人
	Base_Robot robot2("robot2");
	Referee referee;
	Base_Robot* robot = &robot1;
	srand((unsigned int)time(NULL));//添加随机数种子
	int i = rand() % 100 + 1;//生成随机数

	while (referee.end)//进入循环
	{
		i++;
		srand(i);
		int num = rand();
		
		
		if (robot == &robot1)
		{
			referee.GunShooting(robot1,num);//打枪
			referee.Set(robot1, robot2);//输出双方操作和血量
			referee.Isend(robot1, robot2);//判断游戏是否结束
			referee.ChangeHolder(robot1);//持枪方轮换
			if (referee.holder == false)robot = &robot2;
		}
		else
		{
			referee.GunShooting(robot2,num);//打枪
			referee.Set(robot1, robot2);//输出双方操作和血量
			referee.Isend(robot1, robot2);//判断游戏是否结束
			referee.ChangeHolder(robot2);//持枪方轮换
			if (referee.holder == false)robot = &robot1;
		}
	}

	return 0;
}