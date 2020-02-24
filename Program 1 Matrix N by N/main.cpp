#include <stdio.h>
#include <stdlib.h>
#include <ctime>

int matrix_1[20][20];//Matrix_1 is going to be the first matrix 
int matrix_2[20][20];//Matrix_2 is going to be the second matrix
int result[20][20];//Result is going to be the output of the operation
int n1,m1,n2,m2,res,n3,m3;//Matrix's Sizes
int flag_a=0;//Check if the condition was true

int main(){
   //Ask data
    printf("Matrix 1");
    printf("\nSize R: ");
        scanf("%i",&n1);
    printf("Size C: ");
        scanf("%i",&m1);
    
    printf("\nMatrix 2");
    printf("\nSize R: ");
        scanf("%i",&n2);
    printf("Size C: ");
        scanf("%i",&m2);
    //Validate the matrix
    if(m1==n2){
        flag_a=1;
    }else{
        printf("Error Matrix");
    }

    if(flag_a==1){
        //Create matrix's output size 
            n3=n1;
            m3=m2;
            result[n3][m3];
        //Fill the matrix 1
        int data;
        for(int i=0;i<n1;i++){
            for(int j=0;j<m1;j++){
               printf("Write for [%i,%i]= ",i,j);
                scanf("%i",&data);
               matrix_1[i][j]=data;
            }
        }
        //Fill the matrix 2
        int data1;
        for(int i=0;i<n2;i++){
            for(int j=0;j<m2;j++){
               printf("Write for [%i,%i]= ",i,j);
                scanf("%i",&data1);
               matrix_2[i][j]=data1;
            }
        }
        //Operation
        for (int i = 0; i < n1; i++){
            for (int j = 0; j < m2; j++){
                for (int x = 0; x < m1; x++){
                    result[i][j]=matrix_1[i][x]*matrix_2[x][j]+result[i][j];
                }
            }
        }
        //Print the Matrix
        printf("\nMatrix 1");
        for(int i=0;i<n1;i++){
            printf("\n");
            for(int j=0;j<m1;j++){
                printf(" [%i]{%i,%i} ",matrix_1[i][j],i,j);
            }
        }
        printf("\nMatrix 2");
        for(int i=0;i<n2;i++){
            printf("\n");
            for(int j=0;j<m2;j++){
                 printf(" [%i]{%i,%i} ",matrix_2[i][j],i,j);
            }
        }
        printf("\nOutPut ");
        for(int i=0;i<n3;i++){
            printf("\n");
            for(int j=0;j<m3;j++){
                printf(" [%i]{%i,%i} ",result[i][j],i,j);
            }
        }
    }
    return 0;
}