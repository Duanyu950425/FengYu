#include <stdio.h>
#include <stdlib.h>

void main01()
{
    printf("突突真可爱\n");
    system("taskmgr.exe");
}

void main02()
{
    std::wstring name = L"突突";
    printf(name.c_str());
    printf("突突不乖！\n");
    system("pause");
}

// 将一个正整数分解质因数。例如：输入90，打印出90 = 2*3*3*5
void main()
{
    int n, i;
    printf("请输入整数：");
    scanf("%d", &n);
    printf("%d = ", n);
    for (i = 2; i <= n; i++)
    {
        while (n%i == 0)
        {
            printf("%d", i);
            n /= i;
            if (n != 1)printf("*");
        }
    }
    printf("\n");
    return 0;
}