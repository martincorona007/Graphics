#include <stdio.h>
#include <stdlib.h>
#include <ctime>


int main()
{
int n,m,number,aux_i,aux_j,aux_i1,aux_j1,aux_i2,aux_j2,sum=0;

    srand((unsigned)NULL);

    printf("Write the Matrix Size \n");

    printf("Size N ");
        scanf("%i",&n);

    printf("Size M ");
        scanf("%i",&m);

    int matrix_1[n][m];
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            int data=rand()%50+1;
            matrix_1[i][j]=data;
        }
    }



    for(int i=0;i<n;i++){
            printf("\n");
        for(int j=0;j<m;j++){
            printf(" [%i]{%i,%i} ",matrix_1[i][j],i,j);
        }
    }
    printf("\nSelect number: ");
        scanf("%i",&number);

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(matrix_1[i][j]==number){
                printf("Yes [%i,%i]",i,j);
                aux_i=i;
                aux_j=j;


            }else{
                printf("NOP");
            }
        }
    }
    printf("out [%i,%i]",aux_i,aux_j);
    aux_i1=aux_i2=aux_i;
    aux_j1=aux_j2=aux_j;
    aux_i1-=1;aux_j1-=1;
    aux_i2+=1;aux_j2+=1;
    printf("\nPOINT [%i,%i] + [%i,%i]",aux_i1,aux_j1,aux_i2,aux_j2);
    
    for(int x=aux_i1;x<=aux_i2;x++){
        for(int y=aux_j1;y<=aux_j2;y++){
            printf("M %i",matrix_1[x][y]);
             sum+=matrix_1[x][y];
            // printf("sum %i",sum);
        }
    }
    printf("\nthe sum %i",sum);
    return 0;
}
