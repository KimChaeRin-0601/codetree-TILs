#include <iostream>
using namespace std;

int main() {
    int h, w;
    cin >> h >> w;
    int bmi = 100*100*w/(h*h);
    cout << bmi << endl;;
    if (bmi>=25)
    cout << "Obesity";
    return 0;
}