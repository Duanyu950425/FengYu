
#include "iostream"  //包含c++标准头文件

//iostream.h  PK iostream

using namespace std; //使用c++标准命名空间 里面的标准的定义

/*
在C语言中
	int f(    )；表示返回值为int，接受任意参数的函数
	int f(void)；表示返回值为int的无参函数
	在C++中
	int f(  );和int f(void)具有相同的意义，都表示返回值为int的无参函数
*/


/*
f(i)
{
	printf("i:%d \n", i);
}
*/

/*
int main(int argc, char *argv[])
{

	f(10);

	printf("g() = %d\n", g(1, 2, 3, 4, 5));


	getchar();	
	return 0;
}
*/

//注意在c++中return返回值的细节
int getA()
{
	printf("aaaaaaa");
	//return 10;
}

int main()
{
	//f(100);
	system("pause");

}


