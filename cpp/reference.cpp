//
// Created by HOTIPPO on 2021-12-29.
//

#include <iostream>
using namespace std;

int main(void){

    int num=12;
    int *ptr=&num;   // ptr -> num의 주소값
    int **dptr=&ptr; // dptr -> ptr의 주소값

//   cout<<ptr<<endl;
//   cout<<dptr<<endl;

    int &ref=num;  // ref -> num의 참조자
    int *(&pref)=ptr;  // ptr의 참조자
    int **(&dpref)=dptr; // dptr의 참조자

    cout<<ref<<endl;
    cout<<*pref<<endl;
    cout<<**dpref<<endl;

    return 0;
}