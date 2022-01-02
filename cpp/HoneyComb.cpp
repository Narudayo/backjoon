//
// Created by HOTIPPO on 2021-12-30.
// 백준 2292번 벌집 문제.

#include <iostream>

using namespace std;

int main(void){

    // 6을 더했을때, 보다 작으면 2.
    // 12를 더했을때, 보다 작으면 3.
    // ~~

    int num;
    cin>>num;

    const int six = 6;
    int count = 1; // 지나온 방의 갯수. 무조건 1부터 시작
    int differ = 0;  // 계차
    int max = 1;    // 계차가 적용된 최대값
    bool is_find = false;

    while(!is_find){    //값을 찾으면 종료
        if(num == 1){   // num이 1일경우
            is_find = true;
            cout<<count;
        }else{
            differ += six;        // 계차 더하기.
            max += differ;        // 계차로 더해진 최대값. 7,19,37 ...
            count++;        // 지나온 방 추가
            if(num<=max){
                is_find = true;
                cout<<count;
            }
        }
    }
    return 0;
}