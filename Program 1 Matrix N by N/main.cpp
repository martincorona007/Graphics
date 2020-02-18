#include <stdio.h>
#include <stdlib.h>
#include <ctime>

int matrix_1[20][20];
int matrix_2[20][20];
int result[20][20];
int n1,m1,n2,m2,res,n3,m3;
int flag_a=0;
int main(){
    srand((unsigned)NULL);
    printf("Matrix 1");
    printf("\nSize N: ");
        scanf("%i",&n1);
    printf("Size M: ");
        scanf("%i",&m1);
    
    printf("\nMatrix 2");
    printf("\nSize N: ");
        scanf("%i",&n2);
    printf("Size M: ");
        scanf("%i",&m2);
    
    if(m1==n2 && n1==m2){//VALIDATE THE MATRIX
        flag_a=1;
    }else{
        printf("Error Matrix");
    }

    if(flag_a==1){
        //create size of the output matrix 
        n3=n1;
        m3=m2;
        result[n3][m3];
        //FILL THE MATRIX 1
    int data;
    for(int i=0;i<n1;i++){
       for(int j=0;j<m1;j++){
                //printf("Write for [%i,%i]= ",i,j);
              //  scanf("%i",&data);
                data=rand()%50+1;
                matrix_1[i][j]=data;
       }
    }
    //FILL THE MATRIX 2
    int data1;
    for(int i=0;i<n2;i++){
       for(int j=0;j<m2;j++){
                //printf("Write for [%i,%i]= ",i,j);
              //  scanf("%i",&data);
                data1=rand()%50+1;
                matrix_2[i][j]=data1;
       }
    }

    //print
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