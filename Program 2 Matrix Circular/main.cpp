#include <stdio.h>
#include <stdlib.h>
#include <ctime>


int matrix_1[20][20];
int matrix_2[20][20];


int n,m,number,aux_i,aux_j,aux_i1,aux_j1,aux_i2,aux_j2,sum=0,sum1=0,size,rule_1=0,op;
int aux_i3,aux_j3,aux_i4,aux_j4;//for coner left side
int sect_a=0,sect_b=0,sect_c=0,sect_d=0,sect_e=0,sect_f=0,sect_g=0,sect_h=0,sect_i=0;
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
                
                aux_i3=aux_i4=aux_i;
                aux_j3=aux_j4=aux_j;
                
                aux_i3-=1;aux_j3+=1;
                aux_i4+=1;aux_j4-=1;

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
                if(aux_i1<0){//ABOVE SIDE
                    sect_c=1;
                    sect_b=0;
                    sect_a=0;
                }
                if(aux_j2>rule_1){//RIGHT SIDE
                    sect_d=1;
                    sect_b=0;
                }
                if(aux_j1<0){//LEFT SIDE
                    sect_e=1;
                    sect_b=0;
                }
                if(aux_i2>rule_1&&aux_j2>rule_1){//BELOW RIGHT SIDE CONER 
                    sect_f=1;
                    sect_b=0;
                    sect_d=0;
                    sect_a=0;
                }
                if(aux_i4>rule_1&&aux_j4<0){//BELOW LEFT SIDE CONER 
                    sect_g=1;
                    sect_f=0;
                    sect_b=0;
                    sect_d=0;
                    sect_a=0;
                    sect_e=0;
                }
                if(aux_i1<0&& aux_j1<0){//ABOVE LEFT SIDE CONER
                    sect_h=1;
                    sect_g=0;
                    sect_f=0;
                    sect_b=0;
                    sect_d=0;
                    sect_a=0;
                    sect_e=0;
                    sect_c=0;
                }
                if(aux_i3<0&& aux_j3>rule_1){//ABOVE RIGHT SIDE CONER
                    sect_i=1;
                    sect_h=0;
                    sect_g=0;
                    sect_f=0;
                    sect_b=0;
                    sect_d=0;
                    sect_a=0;
                    sect_e=0;
                    sect_c=0;
                }
                //ABOVE RIGHT SIDE CONER
                if(sect_i){
                    aux_i3+=1;
                    aux_j3-=2;
                    aux_j4+=1;
                    for(int x=aux_i3;x<=aux_i4;x++){
                        for(int y=aux_j3;y<=aux_j4;y++){
                            printf("M10a >%i< {%i,%i}",matrix_1[x][y],x,y);
                            sum1+=matrix_1[x][y];
                        }
                    }
                    int i=0;
                    while (i<=aux_i4)
                    {
                        printf("M10b >%i< {%i,%i}",matrix_1[i][0],i,0);
                        sum1+=matrix_1[i][0];
                        i++;
                    }
                    int x=aux_j3;
                    while (x<=rule_1)
                    {
                        printf("M10c >%i< {%i,%i}",matrix_1[rule_1][x],rule_1,x);
                        sum1+=matrix_1[rule_1][x];
                        x++;
                    }
                    
                    matrix_2[aux_i][aux_j]=sum1+matrix_1[rule_1][0];

                }
                //ABOVE LEFT SIDE CONER
                if(sect_h){
                    aux_i1+=1;
                    aux_j1+=1;
                    for(int x=aux_i1;x<=aux_i2;x++){
                        for(int y=aux_j1;y<=aux_j2;y++){
                            printf("M9a >%i< {%i,%i}",matrix_1[x][y],x,y);
                            sum1+=matrix_1[x][y];
                        }
                    }
                    int i=0;
                    while (i<=aux_j2)
                    {
                        printf("M9b >%i< {%i,%i}",matrix_1[rule_1][i],rule_1,i);
                        sum1+=matrix_1[rule_1][i];
                        i++;
                    }
                    int x=0;
                    while (x<=aux_j2)
                    {
                        printf("M9c >%i< {%i,%i}",matrix_1[x][rule_1],x,rule_1);
                        sum1+=matrix_1[x][rule_1];
                        x++;
                    }
                    
                    matrix_2[aux_i][aux_j]=sum1+matrix_1[rule_1][rule_1];
                }
                //BELOW LEFT SIDE CONER 
                if(sect_g){
                    aux_j3-=1;
                    aux_i4-=1;
                    aux_j4+=2;
                    for(int x=aux_i3;x<=aux_i4;x++){
                        for(int y=aux_j3;y<=aux_j4;y++){
                            printf("M8a >%i< {%i,%i}",matrix_1[x][y],x,y);
                            sum1+=matrix_1[x][y];
                        }
                    }
                    int i=0;
                    while (i<=aux_j4)
                    {
                        printf("M8b >%i< {%i,%i}",matrix_1[0][i],0,i);
                        sum1+=matrix_1[0][i];
                        i++;
                    }
                    int x=aux_i3;
                    while (x<=rule_1)
                    {
                        printf("M8c >%i< {%i,%i}",matrix_1[x][rule_1],x,rule_1);
                        sum1+=matrix_1[x][rule_1];
                        x++;
                    }
                    
                    matrix_2[aux_i][aux_j]=sum1+matrix_1[0][rule_1];

                }
                //BELOW RIGHT SIDE CONER 
                if(sect_f){
                    aux_i2-=1;
                    aux_j2-=1;
                    for(int x=aux_i1;x<=aux_i2;x++){
                        for(int y=aux_j1;y<=aux_j2;y++){
                            printf("M7a >%i< {%i,%i}",matrix_1[x][y],x,y);
                            sum1+=matrix_1[x][y];
                        }
                    }
                    int i=aux_i1;
                    while (i<=rule_1)
                    {
                        printf("M7b >%i< {%i,%i}",matrix_1[i][0],i,0);
                        sum1+=matrix_1[i][0];
                        i++;
                    }
                    int x=aux_j1;
                    while (x<=rule_1)
                    {
                        printf("M7c >%i< {%i,%i}",matrix_1[0][x],0,x);
                        sum1+=matrix_1[0][x];
                        x++;
                    }
                    
                    matrix_2[aux_i][aux_j]=sum1+matrix_1[0][0];
                }
                //LEFT SIDE
                if(sect_e){
                    aux_j1+=1;
                    for(int x=aux_i1;x<=aux_i2;x++){
                        for(int y=aux_j1;y<=aux_j2;y++){
                            printf("M6a >%i< {%i,%i}",matrix_1[x][y],x,y);
                            sum1+=matrix_1[x][y];
                        }
                    }
                    int i=aux_i1;
                    while (i<=aux_i2)
                    {
                        printf("M6b >%i< {%i,%i}",matrix_1[i][rule_1],i,rule_1);
                        sum1+=matrix_1[i][rule_1];
                        i++;
                    }
                    matrix_2[aux_i][aux_j]=sum1;
                }
                //RIGHT SIDE
                if (sect_d){
                    aux_j2-=1;
                    for(int x=aux_i1;x<=aux_i2;x++){
                        for(int y=aux_j1;y<=aux_j2;y++){
                            printf("M5a >%i< {%i,%i}",matrix_1[x][y],x,y);
                            sum1+=matrix_1[x][y];
                        }
                    }
                    int i=aux_i1;
                    while (i<=aux_i2)
                    {
                        printf("M5b >%i< {%i,%i}",matrix_1[i][0],i,0);
                        sum1+=matrix_1[i][0];
                        i++;
                    }
                    matrix_2[aux_i][aux_j]=sum1;
                }
                
                //ABOVE SIDE
                if (sect_c){
                    aux_i1+=1;
                    for(int x=aux_i1;x<=aux_i2;x++){
                        for(int y=aux_j1;y<=aux_j2;y++){
                            printf("M4a >%i< {%i,%i}",matrix_1[x][y],x,y);
                            sum1+=matrix_1[x][y];
                        }
                    }
                    int i=aux_j1;
                    while (i<=aux_j2)
                    {
                        printf("M4b >%i< {%i,%i}",matrix_1[aux_j2][i],aux_j2,i);
                        sum1+=matrix_1[rule_1][i];
                        i++;
                    }
                    matrix_2[aux_i][aux_j]=sum1;
                }
                
                //BELOW SIDE
                if(sect_a){
                    aux_i2-=1;
                    printf("\nPOINT2 [%i,%i] + [%i,%i]",aux_i1,aux_j1,aux_i2,aux_j2);
            
                
                    for(int x=aux_i1;x<=aux_i2;x++){
                        for(int y=aux_j1;y<=aux_j2;y++){
                            printf("M1a %i",matrix_1[x][y]);
                            sum1+=matrix_1[x][y];
                        }
                    }
                    printf("\nPOINT3 [%i,%i] + [%i,%i]",aux_i1,aux_j1,aux_i2,aux_j2);
            
                    int i=aux_j1;
                    while (i<=aux_j2)
                    {
                        printf("M1b %i",matrix_1[0][i]);
                        sum1+=matrix_1[0][i];
                        i++;
                    }
                    matrix_2[aux_i][aux_j]=sum1;

                }

            //    printf("\nPOINT5 [%i,%i] + [%i,%i]",aux_i1,aux_j1,aux_i2,aux_j2);
            
                //CENTER SIDES
                if(sect_b){
                    for(int x=aux_i1;x<=aux_i2;x++){
                        for(int y=aux_j1;y<=aux_j2;y++){
                            printf("M3a %i",matrix_1[x][y]);
                            sum1+=matrix_1[x][y];
                        }
                    }
                    matrix_2[aux_i][aux_j]=sum1;
	            }
                
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
                sect_c=0;
                sect_d=0;
                sect_e=0;
                sect_f=0;
                sect_g=0;
                sect_h=0;
                sect_i=0;
            }

        }while (op!=1);
        
        


        
    }
    return 0;
}