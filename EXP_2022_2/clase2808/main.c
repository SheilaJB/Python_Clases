
#include<stdio.h>
#include<x86intrin.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int suma(int a, int b){
    return a+b;
}
int resta(int a, int b){
    return a-b;
}
int producto(int a,int b){
    return a*b;
}
int suma_cuadrados(int a, int b){
    return ((a*a)+(b*b));
}
int suma_cubo(int a, int b){
    return ((a*a*a)+(b*b*b));
}
int suma_cuarta_potencia(int a, int b){
    return ((a*a*a*a)+(b*b*b*b));
}


double CalcularMediana(long* ptr, int N){
    if (N % 2 == 0){
        double mediana =(ptr[ N / 2 ] + ptr[ (N/2) - 1 ]) / 2.0;
        return mediana;
    }
    return ptr[ N / 2 ];  
}

int HallarNumeroInst(int n){
    int p;
    if(n==1){
        p=3;
        printf("Número de instruciones :%d.\n",p);
        return p;
        }
    if(n==2){
        p=4;
        printf("Número de instruciones :%d.\n",p);
        return p;
        }
    if(n==3){
        p=4;
        printf("Número de instruciones :%d.\n",p);
        return p;
        }
    if(n==4){
        p=5;
        printf("Número de instruciones :%d.\n",p);
        return p;
        }
    if(n==5){
        p=9;
        printf("Número de instruciones :%d.\n",p);
        return p;
        }
    if(n==6){
        p=7;
        printf("Número de instruciones :%d.\n",p);
        return p;
        }
}
double CalcularCPI(double ciclo, double instr){
    return ciclo/instr;
}

double CalcularMIPS(double CPI, double Frecuencia_cpu){
    return Frecuencia_cpu/(CPI*pow(10,6));
}
double CPI_mediano(int j){
    int a=(rand()%500)+1;
    int b=(rand()%500)+1;
    int N=250000;
    long* ptr = (long*)calloc(N, sizeof(long));
    long tic,toc;
    for(int i=0;i<N;i++){
        int a=(rand()%5)+1;
        int b=(rand()%5)+1;
        if(j==1){
            tic = __rdtsc();
            suma(a,b);
            toc = __rdtsc(); 
            ptr[i]=(toc-tic);
        }
        if(j==2){
            tic = __rdtsc();
            resta(a,b);
            toc = __rdtsc(); 
            ptr[i]=(toc-tic);
        }
        if(j==3){
            tic = __rdtsc();
            producto(a,b);
            toc = __rdtsc(); 
            ptr[i]=(toc-tic);
        }
        if(j==4){
            tic = __rdtsc();
            suma_cuadrados(a,b);
            toc = __rdtsc(); 
            ptr[i]=(toc-tic);
        }
        if(j==5){
            tic = __rdtsc();
            suma_cubo(a,b);
            toc = __rdtsc(); 
            ptr[i]=(toc-tic);
        }
        if(j==6){
            tic = __rdtsc();
            suma_cuarta_potencia(a,b);
            toc = __rdtsc(); 
            ptr[i]=(toc-tic);
        }
    }
    double ciclo= CalcularMediana(ptr,N);
    double num_inst= HallarNumeroInst(j);
    double r =CalcularCPI(ciclo,num_inst);
    free(ptr);
    return r;
}

double CalcularMediaPitag(long* ptr_cpi, int k){
    double s=0.0;
    for(int i=0;i<k;i++){
        s+=ptr_cpi[i];
    }
    return s/(double)k;
}

int main(int argc, char const *argv[]){

    srand(time(NULL));
    int k=6;
    long* ptr_cpi = (long*)calloc(k, sizeof(long));
    double CPI,CPI_Suma,CPI_Resta,CPI_producto,CPI_suma_cuadrados,CPI_suma_cubo,CPI_suma_cuarta_potencia;
    
    int j= atoi(argv[1]);
    printf("Opcion ingresada: %d.\n",j );
    
    //Para 6 funciones, hallar el CPI
    
        
    if(j==1){//suma
        printf("Funcion suma de dos enteros.\n ");
        CPI_Suma= CPI_mediano(j);
        ptr_cpi[j-1]=CPI_Suma;
    }
    else if(j==2){
        printf("Funcion resta de dos entero.\n ");
        CPI_Resta= CPI_mediano(j);
        ptr_cpi[j-1]=CPI_Resta;
    }
    else if(j==3){
        printf("Funcion producto de dos enteros.\n ");
        CPI_producto= CPI_mediano(j);
        ptr_cpi[j-1]=CPI_producto;
    }
    else if(j==4){
        printf("Funcion suma de los cuadrados de dos enteros.\n ");
        CPI_suma_cuadrados= CPI_mediano(j);
        ptr_cpi[j-1]=CPI_suma_cuadrados;
    }
    else if(j==5){
        printf("Funcion suma de los cubos de dos enteros.\n ");
        CPI_suma_cubo= CPI_mediano(j);
        ptr_cpi[j-1]=CPI_suma_cubo;
    }
    else if(j==6){
        printf("Funcion suma de las cuartas potencias de dos enteros.\n ");
        CPI_suma_cuarta_potencia= CPI_mediano(j);
        ptr_cpi[j-1]=CPI_suma_cuarta_potencia;
    }else{
        printf("Error.\n ");
    }
    
    
    //Aplicamos la media aritmetica para hallar el CPI
    CPI=CalcularMediaPitag(ptr_cpi,k);
    printf("El CPI es :%lf.\n",CPI);
    
    //frecuencia de la pc
    double Frecuencia_cpu=(double)(48000000 +8000000)/2.0;
    printf("La frecuencia de la PC es %lf.\n",Frecuencia_cpu);
    
    //hallamos el MIP
    double MIP= CalcularMIPS(CPI,Frecuencia_cpu);
    printf("El MIP es :%lf.\n", MIP);
    
    free(ptr_cpi);
    
    return 0;
}
