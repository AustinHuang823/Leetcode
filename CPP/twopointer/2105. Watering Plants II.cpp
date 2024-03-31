#include <vector>
#include <iostream>

int minimumRefill(vector<int>& plants, int& capacityA, int& capacityB) {
    int a = 0, b = plants.size()-1;
    int A = capacityA, B = capacityB;
    int count = 0;
    while (a <= b){
        if (a == b) {
            if (plants[a] > A && plants[b] > B) count++;
            break;
        }
        if (plants[a] > A){
            A = capacityA - plants[a];
            count++;
        }
        else{
            A -= plants[a];
        }
        if (plants[b] > B){
            B = capacityB - plants[b];
            count++;
        }
        else{
            B -= plants[b];
        }
        a++;
        b--;
    }
    return count;
}

int main(){
    vector<int> plants = {2,1,1};
    int capacityA = 2;
    int capacityB = 2;
    cout << minimumRefill(plants, capacityA, capacityB) << endl;
    return 0;
}