#include <iostream>

int main() {
    std::cout << "How many times do you want to calculate the Fibonacci sequence?: ";
    int n;
    std::cin >> n;

    int prior=0, current=1, nxterm=0;

    for (int i=1; i<=n; i++){
        if(i == 1) {
            std::cout << prior << " ";
            continue;
        }
        if(i == 2) {
            std::cout << current << " ";
            continue;
        }
        nxterm=prior+current;
        std::cout << nxterm << " ";
        prior=current;
        current=nxterm;
    }
    return 0;
}