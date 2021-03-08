#include <iostreame>
#include <string>
using namespace std;
int main() {
    string name;
    int age;
    cout << 'What is your name?';
    cin >> name;
    cout << 'What is your age?';
    cin >> age;
    if (age < 5) {
        cout << 'You are not old enough to play....';
        return;
    }
    cout << 'You are old enough to play!';    
}
