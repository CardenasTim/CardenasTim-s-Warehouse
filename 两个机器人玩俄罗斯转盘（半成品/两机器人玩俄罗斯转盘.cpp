#include<iostream>
#include<string>
#include<ctime>
#include"Base_Robot.h"
#include"Referee.h"

using namespace std;

//���������Խṹ��
struct Robot
{
	int HP=200;
	string name;
};

//������ֵ�ṹ��
struct AttackValue
{
	const int shoot = 10;
	const int no = 0;
	const int bomb = 40;
};

//������������
class Base_Robot
{
	friend class Referee;
public:
	Base_Robot(string name)//������������
	{
		m_robot.name = name;
	}
	void GunShooting()
	{
		srand((unsigned int)time(NULL));//������������
		int num = rand() % 100 + 1;//���������

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
		//����������3�ı����������ӵ��������2�ı�����û���ӵ����������Ȳ���3�ı���Ҳ����2�ı�������ը�š���
		//����3��2�Ĺ���������û���ӵ����
	}
protected:
	Robot m_robot;//����������
	AttackValue hurt;//������ֵ
	int m_behavior;//�ж���Ϊ 0.û���ӵ� 1.����ӵ� 2.ը��
	//�ֻ�ǹȨ������ӵ�������������û�з�������ǹ�������滻��2������0��1��
};

//����ϵͳ��
class Referee
{
public:
	bool end = true;//�ж���Ϸ�Ƿ����
	bool holder=true;//��ǹ���Ƿ��ֻ�
	void Set(Base_Robot &robot1, Base_Robot& robot2)//���˫��������Ѫ��
	{
		if (robot1.m_behavior == 2)
			cout << "����Ϊը��" << endl;
		else if (robot1.m_behavior == 1)
			cout << "����Ϊ����ӵ�";
		else
			cout << "����Ϊû���ӵ�";
		cout << "robot1Ѫ��Ϊ" << robot1.m_robot.HP;
		cout << "robot2Ѫ��Ϊ" << robot2.m_robot.HP;
	}

	void Isend(Base_Robot& robot1, Base_Robot& robot2)//�ж���Ϸ�Ƿ����
	{
		if (robot1.m_robot.HP <= 0 && robot2.m_robot.HP <= 0)
			bool end = false;
	}

	int ChangeHolder(Base_Robot& robot1, Base_Robot& robot2)//��ǹ���ֻ�
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
	Base_Robot robot1("robot1");//����������
	Base_Robot robot2("robot2");
	Referee referee;

	while (referee.end)//����ѭ��
	{
		void GunShooting();//��ǹ

	}
	return 0;
}