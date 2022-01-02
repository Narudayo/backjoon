#include <iostream>

using namespace std;
int findSquareRoot(int N, int k);

int main(){

    // N = 3^k
    int N;
    cin>>N;
    int k = findSquareRoot(N,1);


    return 0;
}

// findSquareRoot => N에 상응하는 k값을 반환. 1<=k<8
int findSquareRoot(int N, int k){
    if(N==3)    return k;
    return findSquareRoot(N/3,k+1);
}

// printStar => 상수 N,k 에서 현재값 curr을 변경하며 recursion
void printStar(int N, int k, int curr){

    // 한 줄에 별을 N만큼 찍었을(공백포함) 때, n으로 나눈 나머지가 0일 때 endl
    // 가운데이면 공백. 가운데는 어떻게 알지?
    // (1) 현재 줄에서 3으로 나눈 나머지가 1이고,
    // (2) 출력 횟수에서 3으로 나눈 나머지가 1이면.
    // (1),(2) 이면 가운데. 공백출력

    if()

    cout<<"*";
    if(N%k == 0)  cout<<endl;

}

