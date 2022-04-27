#include <stdio.h>
#include <iostream>
#include <fstream>
#include <list>
#include <sys/types.h>
#include <dirent.h>
#include <unistd.h>

int main(void)
{
    /*
    HANDLE hFind;
    WIN32_FIND_DATA fd;
    std::list<std::string> f_list;
    hFind = FindFirstFile((LPCWSTR) "./output/geo-point/*.twitter", &fd);
    if (hFind == INVALID_HANDLE_VALUE)
        return -1;
    do
    {
        std::wstring fileName = fd.cFileName;
        f_list.push_back("fileName");
    } while (FindNextFile(hFind, &fd));

    std::fstream f_input, f_output;
    f_input.open("./dataset/geo-point/*.tweets", std::ios_base::out);
    */
    std::fstream f_output;
    f_output.open("./output/TPR.txt", std::ios_base::out);

    char tmp[256];
    getcwd(tmp, 256);

    const char *path = "./input/geo-point";
    DIR *dp;
    dp = opendir(path);
    f_output << "aaa nnn";
    if (!dp)
        return -1;
    f_output << "aaa";
    dirent *entry = readdir(dp);
    while (entry)
    {
        f_output << path << entry->d_name << std::endl;
        entry = readdir(dp);
    }

    std::cout << "test2";
    printf("test");
    return 0;
}
