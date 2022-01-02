//
// Created by HOTIPPO on 2022-01-02.
// 백준 10872번 팩토리얼


#include <iostream>

using namespace std;

int fac(int i);

int main(){
    int val;
    cin>>val;
    cout<<fac(val);

    return 0;
}

int fac(int i){
    if(i==0)
        return 1;
    if(i==1)
        return 1;
    return i*fac(i-1);
}
