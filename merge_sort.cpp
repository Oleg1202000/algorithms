#include <iostream>

using namespace std;

void merge_sort(int* arr, int start_index, int stop_index);
void print_array(int* arr, int size);


int main() {
    srand(42);
    int range_min = -100;
    int range_max = 100;
    const int size = 30;
    int arr[size];

    for(int i=0;i<size;i++) {
        arr[i] = rand() % (range_max - range_min) + range_min;
    }

    cout << "Unsorted: ";
    print_array(arr, size);
    merge_sort(arr, 0, size);
    cout << "Sorted: ";
    print_array(arr, size);
}


void merge_sort(int* arr, int start_index, int stop_index) {

    int size_subarray = stop_index - start_index;
    int half_index = start_index + (size_subarray) / 2;

    if (size_subarray > 2) {
        merge_sort(arr, start_index, half_index);
        merge_sort(arr, half_index, stop_index);
    }

    int index1 = start_index;
    int index2 = half_index;
    int* temp_arr = new int [size_subarray]; //Временный массив для хранения результата
    int index = 0;

    // Пока index не равен размеру подмассива
    while (index != size_subarray) {

        // Если index1 не достиг половины массива И число слева меньше числа справа
        // ИЛИ index2 достиг правой границы
        if (index2 == stop_index || index1 != half_index & arr[index1]<=arr[index2]) {
            temp_arr[index] = arr[index1];
            index1++;
        } else {
            temp_arr[index] = arr[index2];
            index2++;
        }
        index++;
    }

    // Заменяем подмассив на результат сортировки
    for (int i=0; i<index;i++) {
        arr[start_index+i] = temp_arr[i];
    }
}


void print_array(int* arr, int size) {
    for(int i=0;i<size;i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}
