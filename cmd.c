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

// 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
// 已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比。
// 写出三队赛手的名单
void main03()
{
    char i, j, k;
    for (i = 'x'; i <= 'z'; i++)
    {
        for (j = 'x'; j <= 'z'; j++)
        {
            if (i != j)
            {
                for (k = 'x'; k <= 'z'; k++)
                {
                    if (i != k && j != k)
                    {
                        if (i != 'x' && k != 'x' && k != 'z')
                        {
                            printf("顺序为： a--%c\tb--%c\tc--%c\n", i, j, k);
                        }
                    }
                }
            }
        }
    }
}
// 将一个正整数分解质因数。例如：输入90，打印出90 = 2*3*3*5
void main04()
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

// 用*号输出字母C的图案
void main()
{
    printf("用*号输出字母C! \n");
    printf(" ****\n");
    printf(" *\n");
    printf(" *\n");
    printf(" ****\n");
    return 0;
}