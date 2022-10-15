动态创建一维数组

int len;
 cout<<"输入一维数组大小:"<<endl;
 cin>>len;
 int *p=new int[len];
 
 cout<<"输入元素，元素之间以空格分隔!"<<endl;

 int val,i=0;
 for(i=0;i!=len;i++)
 {cin>>val;
  p[i]=val;
 }
 cout<<"输出一维数组:"<<endl;
 for(i=0;i!=len;i++)
 {
 
 cout<<p[i]<<"  ";
 }
 cout<<endl;

动态分配二维数组

int  main(int argc,char **argv)
{


int column,row; 
cout<<"输入二维数组的行数和列数"<<endl; 
cin>>row>>column;
int **array;
//array = (int **)malloc(sizeof(int *)*row);//方法一
  array=new int *[row];
for(int i=0;i!=row ; i++)
 //array[i]=(int *) malloc(sizeof(int )*column);//方法一
 array[i]=new int [column];
cout<<"输入二维数组"<<endl;
for(int j=0 ; j !=row ; j++)
{for(int k=0 ; k !=column ; k++) {cin>>array[j][k]; } } 
cout<<"输入的二维数组为"<<endl; 
for( int j=0 ; j !=row ; j++ ) 
{ for(int k=0 ; k !=column ; k++) 
{cout<<array[j][k]<<" "; } 
cout<<endl; } 
//释放空间 　　
for(int i=0 ;i!=row;i++)
 free(array[i]); 
free(array);
return 0;
}

 

C++中在结构体里面动态创建数组，而且创建动态结构体数组

大家看一下这个例子就知道了！

int main(int argc, char* argv[])
{
int n,i,m,j;
   struct test
{
   int *array;
};
test *testarray;
cin>>n>>m;
testarray=new test[m];
for (i=0;i<m;i++)
{
testarray[i].array=new int[n];
}
for (i=0;i<m;i++)
{
   for (j=0;j<n;j++)
   {
    testarray[i].array[j]=i+j;
   }
  
}
for (i=0;i<m;i++)
{
   for (j=0;j<n;j++)
   {
    cout<<testarray[i].array[j];
   
   }
   cout<<endl;
}
return 0;
}