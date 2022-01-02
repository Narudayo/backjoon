//
// Created by HOTIPPO on 2022-01-02.
// 백준 1193번 분수찾기 문제

#include <iostream>

using namespace std;

// 객체를 생성하지 않을 경우 main에 모조리 넣거나,
// dia와 sum을 찾기 위한 함수를 각자 돌려야 함.
class nAndsum{
public:
    int dia;
    int sum;
};

nAndsum numOfDia(int x);

int main(void){

    int x;
    cin>>x;
    nAndsum diasum = numOfDia(x);

//    cout<<"dia 개수 :"<<diasum.dia<<endl;
//    cout<<"sum : "<<diasum.sum<<endl;

    int numerator = diasum.sum-x+1;
    int denominator = diasum.dia - (diasum.sum-x);

    // 지그재그니까, dia가 even이면 분수,분모가 reverse
    if(diasum.dia%2 == 0){
        cout<<denominator<<"/"<<numerator;
    }else{
        cout<<numerator<<"/"<<denominator;
    }

    return 0;
}


//  other by 승현.몇 번째 대각선
// numOfDia => 입력받은 param x가 몇 번째를 통과하는지
// 그리고 해당 dia의 sum은 얼마인지
// 1/1 => 1번째, sum은 1
// 2/1, 1/2 => 2번째, sum은 3
// 3/1, 2/2, 1/3 => 3번째, sum은 6
// ~~

nAndsum numOfDia(int x){

    int s=1;  // 총 합. 처음 시작은 1/1 적용. 아래 n도 동일.
    int n=1;  // 몇 번째 dia인지

    while(x>s){
        n++;
        s+=n;
    }

    nAndsum diasum = {n,s};
    return diasum;
}