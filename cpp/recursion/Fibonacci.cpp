//
// Created by HOTIPPO on 2022-01-02.
// 백준 10870번 피보나치수 5

#include <iostream>

using namespace std;

int fibo(int i);

int main(){

    int val;
    cin>>val;
    cout<<fibo(val);

    return 0;
}

int fibo(int i){
    if(i==0)    return 0;
    if(i==1)    return 1;
    return fibo(i-1) + fibo(i-2);
}