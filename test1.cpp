#include<iostream>
#include<algorithm>
using namespace std;
int main() {
    int i, n, a, lit[100] = {};
    i = 0;
    while (cin >> n) {
        lit[i] = n;
        i += 1;
        if (n == -1) {
            i=i-1;
            break;
        }
    }
    sort(lit+0,lit+i);
    if (i % 2 == 0) {
        a =( lit[i / 2] + lit[(i / 2) -1] )/ 2;
        cout << lit[i / 2] << endl;
    }
    else if (i/ 2 != 0) {
        a = (i / 2);
        cout << lit[a] << endl;
    }
    
}