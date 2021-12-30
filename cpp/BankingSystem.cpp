//
// Created by HOTIPPO on 2021-12-29.
//


#include <iostream>
#include <vector>
#include <cstring>
#include <string>

using namespace std;

typedef struct {
    int accID;
    int balance;
    string name;

//    char name[10];
} Account;

enum {
    Make=1,
    DEPOSIT,
    WITHDRAW,
    INQUIRE,
    EXIT
};

vector<Account> accVec;

//Account* accArr = new Account[1];


void printMenu(void);   // 메뉴출력
void createAccount(void);   // 1. 계좌생성
void deposit(void);         // 2. 입 금
void withdraw(void);        // 3. 출 금
void printAllAcount(void);  // 4. 계좌정보 전체 출력

int main() {
    int choice;

    while(1){
        printMenu();
        cout<<"선택 : ";
        cin >> choice;
        cout<<endl;

        switch(choice){
            case Make:
                createAccount();
                break;
            case DEPOSIT:
                deposit();
                break;
            case WITHDRAW:
                withdraw();
                break;
            case INQUIRE:
                printAllAcount();
                break;
            case EXIT:
                return 0;
            default:
                cout<<"잘못된 접근입니다."<<endl;
        }
    }

    return 0;
}


// 메뉴리스트를 프린트
void printMenu(){
    cout<<"----Menu----"<<endl;
    cout<<"1. 계좌개설"<<endl;
    cout<<"2. 입 금"<<endl;
    cout<<"3. 출 금"<<endl;
    cout<<"4. 계좌정보 전체 출력"<<endl;
    cout<<"5. 프로그램 종료"<<endl;

}

void createAccount(){

    int id;
    string name;
//    char name[10];
    int balance;

    cout<<"[계좌개설]"<<endl;
    cout<<"계좌ID :"; cin>>id;
    cout<<"이 름 :"; cin>>name;
    cout<<"입금액 : "; cin>>balance;

    Account acc;
    acc.accID = id;
    acc.name = name;
//    strcpy(acc.name,name);
    acc.balance = balance;

    accVec.push_back(acc);

}

void deposit(){
    int id;
    int amount;
    cout << "계좌ID: "; cin>>id;
    cout << "입금액: "; cin>>amount;

    for(int i = 0; i < accVec.size(); i++){
        if(accVec[i].accID == id){  //값을 찾으면
            accVec[i].balance += amount;
            cout<<"입금완료"<<endl;
            return;
        }
    }
    cout<<"유효하지 않은 ID 입니다."<<endl;
}

void withdraw(){
    int id;
    int amount;
    cout << "계좌ID: "; cin>>id;
    cout << "출금액: "; cin>>amount;

    for(int i = 0; i < accVec.size(); i++){
        if(accVec[i].accID == id){  //값을 찾으면
            accVec[i].balance -= amount;
            cout<<"출금완료"<<endl;
            return;
        }
    }
    cout<<"유효하지 않은 ID 입니다."<<endl;
}

void printAllAcount(){

    for(auto loop : accVec){
        cout<<loop.accID <<endl;
        cout<<loop.name <<endl;
        cout<<loop.balance <<endl;
    }

//    for(int i =0; i < accVec.size(); i++){
//        cout<<"계좌ID: "<<accVec[i].accID<<endl;
//        cout<<"이 름: "<<accVec[i].name<<endl;
//        cout<<"잔 액: "<<accVec[i].balance<<endl;
//    }
}