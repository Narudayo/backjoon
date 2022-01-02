//
// Created by HOTIPPO on 2022-01-02.
// 백준 2869번 달팽이는 올라가고 싶다.

#include <iostream>

using namespace std;

int main(){

    // 낮에는 a 미터, 밤에는 b미터 미끄러진다.
    // 높이는 v인 나무이다.
    int a,b,v;
    cin>>a>>b>>v;


    // day => 올라가는데 걸린 최종 기간.
    // oneDayV => 낮, 밤이 지나서 하루 올라가는 높이
    // min => v에 상응하는 day의 최소값
    int oneDayV = a-b;
    int day;
    int min = (v-a)/oneDayV;

    // currV => 현재 높이 v
    int currV = oneDayV*min;
    int count = 0;

    // 최소높이부터 반복문
    while(true){
        currV+=a;       // 낮에 올라감
        if(currV>=v) break;
        currV-=b;       // 밤에 내려감
        count++;        // 밤이 지난 다음이어야 하루가 지남.
    }
    day = min+count+1;

    cout<<day;


    return 0;
}