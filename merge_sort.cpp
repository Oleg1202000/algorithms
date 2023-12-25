void merge_sort(int* arr, int start_index, int stop_index) {

    int size_subarray = stop_index - start_index;
    int half_index = start_index + (size_subarray) / 2;

    if (size_subarray > 2) {
        // Разделяем массив на подмассивы пока длина > 2
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
