#include <stdio.h>
#include <stdlib.h>
#include <ctime>


int matrix_1[20][20];
int matrix_2[20][20];


int n,m,number,aux_i,aux_j,aux_i1,aux_j1,aux_i2,aux_j2,sum=0,sum1=0,size,rule_1=0,op;
int sect_a=0,sect_b=0;
bool flag_1=true,flag_2,flag_3=true;


void print();

int main()
{
    srand((unsigned)NULL);

    printf("Write the Matrix Size \n");

    printf("Size N ");
        scanf("%i",&n);

    printf("Size M ");
        scanf("%i",&m);
    
    
    while(n<3&&m<3){//make the user insert N and M grater than 3
        printf("Error Matrix Size");
        flag_1=false;
        printf("\nSize N ");
            scanf("%i",&n);

        printf("Size M ");
            scanf("%i",&m);
    
        
    }
    if(n>=3&&m>=3){//change the flag 
            flag_1=true;
    }
    if(flag_1==true){
        int matrix_1[n][m];
        int matrix_2[n][m];
        //ask the data
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                 int data=rand()%50+1;
                matrix_1[i][j]=data;
            }
        }
        //fill in the other matrix
        for (int i = 0; i < n ;i++) {
            for (int j=0; j < m; j++)
            {
            matrix_2[i][j]=0;
            }
            
        }
        
        printf("\nMatrix 1");
            for(int i=0;i<n;i++){
                    printf("\n");
                for(int j=0;j<m;j++){
                    printf(" [%i]{%i,%i} ",matrix_1[i][j],i,j);
                }
            }
        printf("\nMatrix 2");
            for(int i=0;i<n;i++){
                    printf("\n");
                for(int j=0;j<m;j++){
                    printf(" [%i]{%i,%i} ",matrix_2[i][j],i,j);
                }
            }
        
            
        do{
          //s  printf("\nPOINT4 [%i,%i] + [%i,%i]",aux_i1,aux_j1,aux_i2,aux_j2);
            
            
            printf("\n\nSelect number: ");
            scanf("%i",&number);
            
            for(int i=0;i<n;i++){//FIND THE NUMBER AND VERIFY IF EXITS
                for(int j=0;j<m;j++){
                    if(flag_3){
                        if(matrix_1[i][j]==number){
                            printf("Yes [%i,%i]",i,j);
                            aux_i=i;
                            aux_j=j;
                            flag_2=true;
                            
                            flag_3=false;
                        }else{
                            flag_2=false;
                        }

                    }
                }
            }
                        //VERIFY IF THE NUMBER EXIST
            if(flag_2==false){
                printf("Number not found");
            }else if(flag_2==true){
                printf("out [%i,%i]",aux_i,aux_j);
                aux_i1=aux_i2=aux_i;
                aux_j1=aux_j2=aux_j;
                aux_i1-=1;aux_j1-=1;
                aux_i2+=1;aux_j2+=1;
                printf("\nPOINT1 [%i,%i] + [%i,%i]",aux_i1,aux_j1,aux_i2,aux_j2);
                //RULES TO KNOW IF 
                rule_1=n;
                rule_1-=1;
                printf("\n aux_i2 %i rule_1 %i ",aux_i2,rule_1);
                if(aux_i2>rule_1){//BELOW SIDE
                    sect_a=1;
                }
                if(aux_i2<=rule_1){//CENTER SIDES
                    sect_b=1;
                }
                //BELOW SIDE
                if(sect_a){
                    aux_i2-=1;
                    printf("INSIDE");
                    printf("\nPOINT2 [%i,%i] + [%i,%i]",aux_i1,aux_j1,aux_i2,aux_j2);
            
                
                    for(int x=aux_i1;x<=aux_i2;x++){
                        for(int y=aux_j1;y<=aux_j2;y++){
                            printf("M1 %i",matrix_1[x][y]);
                            sum1+=matrix_1[x][y];
                        }
                    }
                    printf("\nPOINT3 [%i,%i] + [%i,%i]",aux_i1,aux_j1,aux_i2,aux_j2);
            
                    int i=aux_j1;
                    while (i<=aux_j2)
                    {
                        printf("M2 %i",matrix_1[0][i]);
                        sum1+=matrix_1[0][i];
                        i++;
                    }
                    matrix_2[aux_i][aux_j]=sum1;

                }

                printf("\nPOINT5 [%i,%i] + [%i,%i]",aux_i1,aux_j1,aux_i2,aux_j2);
            
                //CENTER SIDES
                if(sect_b){
                    for(int x=aux_i1;x<=aux_i2;x++){
                        for(int y=aux_j1;y<=aux_j2;y++){
                            printf("M3 %i",matrix_1[x][y]);
                            sum1+=matrix_1[x][y];
                        }
                    }
                    matrix_2[aux_i][aux_j]=sum1;
	            }
                //normal
                /**/
                printf("\nMatrix 1x");
                for(int i=0;i<n;i++){
                        printf("\n");
                    for(int j=0;j<m;j++){
                        printf(" [%i]{%i,%i} ",matrix_1[i][j],i,j);
                    }
                }
                printf("\nMatrix 2x");
                for(int i=0;i<n;i++){
                        printf("\n");
                    for(int j=0;j<m;j++){
                        printf(" [%i]{%i,%i} ",matrix_2[i][j],i,j);
                    }
                }
                printf("\nthe sum %i",sum1);
            
            }


            printf("\n\nSelect 1 to finish 0 to cotinue: ");
            scanf("%i",&op);
            if(op==0){
                flag_3=true;
                aux_j=0;
                aux_i=0;
                sum1=0;
                sect_b=0;
                sect_a=0;
            }

        }while (op!=1);
        
        


        
    }
    return 0;
}