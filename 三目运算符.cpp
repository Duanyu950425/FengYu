#include "iostream"

using namespace  std;



int main()
{
	int a = 10;
	int b = 20;

	//返回一个最小数 并且给最小数赋值成3
	//三目运算符是一个表达式 ，表达式不可能做左值
	//	(a < b ? a : b )是一个表达式 表达式的运算结果在寄存器中。。。

	//原来的C中 返回的不是a本身，但是c++中，对三目运算符进行功能增强。。。
	//c++返回的是a本身
	(a < b ? a : b ) = 30;
	//a = 30;

	printf("a = %d, b = %d\n", a, b);

	system("pause");

	return 0;
}