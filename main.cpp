#include <iostream>

#include "buble_sort.cpp"
#include "merge_sort.cpp"

using namespace std;


void print_array(int* arr, int size);
void compare_elements(int arr1[], int arr2[], int size);

int main() {

    int range_min = -100;
    int range_max = 100;
    const int size = 30;
    int arr[size], control_array[size];

    for(int i=0;i<10;i++) {
        srand(42+i);
        for(int j=0;j<size;j++) {
        arr[j] = rand() % (range_max - range_min) + range_min;
        control_array[j] = arr[j];
        }

        cout << "Unsorted: ";
        print_array(arr, size);

        cout << "Merge sort: ";
        merge_sort(arr, 0, size);
        print_array(arr, size);

        cout << "Buble sort: ";
        buble_sort(control_array, size);
        print_array(control_array, size);

        cout << endl;
        compare_elements(arr, control_array, size);
        cout << endl;
    }
}



void print_array(int* arr, int size) {
    for(int i=0;i<size;i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void compare_elements(int arr1[], int arr2[], int size) {
    char message[13] = {"arr1 == arr2"};
    for(int i=0;i<size;i++) {
        if (arr1[i] != arr2[i]) {
            message[5] = *"!";
            break;
        }
    }
    cout << message << endl;
}
