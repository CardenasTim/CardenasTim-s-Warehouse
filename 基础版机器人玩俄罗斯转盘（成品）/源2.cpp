#include<iostream>
#include<string>
#include<ctime>
#include<cstdlib> // rand()��srand() �������������
using namespace std;

//���������Խṹ��
struct Robot
{
	int HP = 200;
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
	bool holder = true;//��ǹ���Ƿ��ֻ�

	void GunShooting(Base_Robot& robot,int num)//��ǹ
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
		//����������3�ı����������ӵ��������2�ı�����û���ӵ����������Ȳ���3�ı���Ҳ����2�ı�������ը�š���
		//����3��2�Ĺ���������û���ӵ����
	}
	void Set(Base_Robot& robot1, Base_Robot& robot2)//���˫��������Ѫ��
	{
		if (robot1.m_behavior == 2)
			cout << "����Ϊը��" ;
		else if (robot1.m_behavior == 1)
			cout << "����Ϊ����ӵ�";
		else
			cout << "����Ϊû���ӵ�";
		cout << "robot1Ѫ��Ϊ" << robot1.m_robot.HP;
		cout << "robot2Ѫ��Ϊ" << robot2.m_robot.HP<<endl;
	}

	void Isend(Base_Robot& robot1, Base_Robot& robot2)//�ж���Ϸ�Ƿ����
	{
		if ((robot1.m_robot.HP <= 0 )|| (robot2.m_robot.HP <= 0))
			end = false;//�Ӷ��˸�boolʹ��end��Ϊ�ֲ�����������ѭ���޷��˳�
	}

	void ChangeHolder(Base_Robot& robot)//��ǹ���ֻ�
	{
		if (robot.m_behavior == 2)
			holder = true;
		else
			holder = false;


	}
};
int main()
{
	Base_Robot robot1("robot1");//����������
	Base_Robot robot2("robot2");
	Referee referee;
	Base_Robot* robot = &robot1;
	srand((unsigned int)time(NULL));//������������
	int i = rand() % 100 + 1;//���������

	while (referee.end)//����ѭ��
	{
		i++;
		srand(i);
		int num = rand();
		
		
		if (robot == &robot1)
		{
			referee.GunShooting(robot1,num);//��ǹ
			referee.Set(robot1, robot2);//���˫��������Ѫ��
			referee.Isend(robot1, robot2);//�ж���Ϸ�Ƿ����
			referee.ChangeHolder(robot1);//��ǹ���ֻ�
			if (referee.holder == false)robot = &robot2;
		}
		else
		{
			referee.GunShooting(robot2,num);//��ǹ
			referee.Set(robot1, robot2);//���˫��������Ѫ��
			referee.Isend(robot1, robot2);//�ж���Ϸ�Ƿ����
			referee.ChangeHolder(robot2);//��ǹ���ֻ�
			if (referee.holder == false)robot = &robot1;
		}
	}

	return 0;
}