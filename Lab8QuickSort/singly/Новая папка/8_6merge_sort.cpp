#include <iostream>

using namespace std;

void swap(int *a, int *b);
void merge(int (*arr)[2], int left, int mid, int right);
void mergeSort(int (*arr)[2], int left, int right);
void display(int (*arr)[2], int n);

int main() {
    int n;
    cin >> n;
    int arr[n][2];
    for (int i = 0; i < n; i++) {
        cin >> arr[i][0] >> arr[i][1];
        if (arr[i][0] > arr[i][1]) {
            swap(&arr[i][0], &arr[i][1]);
        }
    }
    mergeSort(arr,0, n-1);
    display(arr, n);
    return 0;
}

void merge(int (*arr)[2], int left, int mid, int right) {
    int i, j, k;
    int n1 = mid - left +1;
    int n2 = right - mid;
    int L[n1][2], R[n2][2];
    for (int i = 0; i < n1; i++) {
        L[i][0] = arr[left + i][0];
        L[i][1] = arr[left + i][1];
    }
    for (int j = 0; j < n2; j++) {
        R[j][0] = arr[mid + 1 + j][0];
        R[j][1] = arr[mid + 1 + j][1];
    }
    i = 0;
    j = 0;
    k = left;
    while (i < n1 && j < n2) {
        if (L[i][0] <= R[j][0]) {
            arr[k][0] = L[i][0];
            arr[k][1] = L[i][1];
            i ++;
        }
        else{
            arr[k][0] = R[j][0];
            arr[k][1] = R[j][1];
            j++;
        }
        k++;
    }
    while (i < n1) {
        arr[k][0] = L[i][0];
        arr[k][1] = L[i][1];
        k++;
        i++;
    }
    while (j < n2) {
        arr[k][0] = R[j][0];
        arr[k][1] = R[j][1];
        k++;
        j++;
    }
}

void mergeSort(int (*arr)[2], int left, int right) {
    if (left < right) {
        int mid = left + (right - left)/2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void display(int (*arr)[2], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i][0] << " " << arr[i][1] << endl;
    }
}
