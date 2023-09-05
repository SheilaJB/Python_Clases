
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <math.h>

void llenar_arreglo(double* arr, int N){
    double temp = 0.0;
    for(int i = 0; i < N; i++){
        temp = rand() % 5;
        arr[i] = temp;
    }
}

void imprimir_arreglo(double* arr, int N){
    printf("[ ");
    for(int i = 0; i < N-1; i++){
        printf("%lf, ", arr[i]);
    }
    printf("%lf ]\n", arr[N-1]);
}

void ordenar_arreglo(double* arr, int N){
    double temp = 0.0;
    for(int i = 0; i < N - 1; i++){
        for(int j = 0; j < N - i - 1; j++){
            if (arr[j] > arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

double mediana(double* arr_ord, int N){
    if (N % 2 == 0){
        return (arr_ord[ N / 2 ] + arr_ord[ (N/2) - 1 ]) / 2.0;
    }
    return arr_ord[ N / 2 ];
}

double minimo(double* arr_ord, int N){
    return arr_ord[ 0 ];
}

double maximo(double* arr_ord, int N){
    return arr_ord[ N-1 ];
}

int main(){

    srand(time(NULL));

    int N = 4;

    double* arr = (double*)calloc(N, sizeof(double));

    llenar_arreglo(arr, N);

    imprimir_arreglo(arr, N);

    ordenar_arreglo(arr, N);

    imprimir_arreglo(arr, N);

    double medi = mediana(arr, N);

    double mini = minimo(arr, N);

    double maxi = maximo(arr, N);

    printf("Mediana: %lf\n", medi);
    printf("Mínimo: %lf\n", mini);
    printf("Máximo: %lf\n", maxi);

    return 0;
}
