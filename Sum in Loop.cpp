#include <iostream>
using namespace std;

int main(){
    int n, a[100];
    cin>>n;
    for (int i=0; i<n; i++)
        cin>>a[i];
    int jmlh=0;
    for (int i=0; i<n; i++)
        jmlh+=a[i];
    cout<<jmlh<<endl;
}
