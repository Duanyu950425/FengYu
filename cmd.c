#include <stdio.h>
#include <stdlib.h>

void main01()
{
    printf("突突真可爱\n");
    system("taskmgr.exe");
}

void main()
{
    std::wstring name = L"突突";
    printf(name.c_str());
    printf("突突不乖！\n");
    system("pause");
}