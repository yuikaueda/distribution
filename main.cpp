#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>


#define N 1000
#define j 100
#define len_a 10
#define l_0 10
#define f_0 5.0e-30

/*void make_a(double *a)
{
	double l_i=1;
	a[0]=1.0;
	printf("%d\n",a[0]);


	for(int i=0; i<9; i++){
		l_i +=1;
		for(int k=1+i*len_a; k<1+(1+i)*len_a; k++){
		a[k]=l_i;
		printf("%d\n",a[k]);
		}
	}
	for(int m=1+9*len_a; m<j; m++){
		a[m]=l_i+1.0;
	}
	
}
*/

/*double make_z(int b[j])
{
	double z=0;
	int l_i=1;
	for(int i=0; i<j; i++){
		z=z+exp((b[i]+f_0*exp(l_i-l_0))/l_i);
		l_i+=1;
	}
	return z;
}*/

int main()
{
	double Z;
	double A_[j];
	double l0_i=1.0;

        A_[0]=1.0;

        //printf("%d\n",A_[0]);
	//Z=exp((A_[0]+f_0*exp(l0_i-l_0))/l0_i);
	//printf("%d\n",Z);

        for(int i=0; i<9; i++){
                l0_i +=1;
                for(int k=1+i*len_a; k<1+(1+i)*len_a; k++){
                A_[k]=l0_i;
                //printf("%f\n",A_[k]);
		//Z+=A_[k];
		//Z = Z + exp(A_[k]/k+f_0*exp(k-l_0)/k);
		//printf("%d\n",Z);
                }
        }
        for(int m=1+9*len_a; m<j; m++){
                A_[m]=l0_i+1.0;
		//Z=Z+exp(A_[m]/m+f_0*exp(m-l_0)/m);
		//printf("%f\n",A_[m]);
        }

	Z=0;
	double l1_i=0;
	for(int h=0; h<j; h++){
		l1_i += 1.0;
		Z += exp((A_[h]/(2*l1_i)) + (f_0*exp(l1_i-l_0)/l1_i));
		//Z +=(A_[h]/l1_i) + (f_0*exp(l1_i-l_0)/l1_i);
	}

	//printf("%f\n",Z);

	//make_a(A_);

	//double z;
	//Z=make_z(A_);


	FILE* fp0;
       	fp0 = fopen("l_ni.dat" , "w");
 	if(fp0==NULL){
 		printf("File open faild.");
	 }

	double l_i=0;
	for(int i=0; i<j; i++){
		l_i += 1.0;
		double n_i=0.0;
		n_i=N*exp((A_[i]/(2*l_i)) + (f_0*exp(l_i-l_0)/l_i))/Z;

		fprintf(fp0, "%f\t%f\n",l_i,n_i);
		
	}
	fclose(fp0);

	return 0;
}
