#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>


#define N 1000
#define j 100
#define len_a 10
#define l_0 80
#define f_0 1.0e-12
#define a 1.94e-22 //V*mu/(2*T*N)
#define Kb 1.38e-23

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
                l0_i +=1.0;
                for(int k=1+i*len_a; k<1+(1+i)*len_a; k++){
                A_[k]=(double)l0_i;
                //printf("%f\n",A_[k]);
		//Z+=A_[k];
		//Z = Z + exp(A_[k]/k+f_0*exp(k-l_0)/k);
		//printf("%d\n",Z);
                }
        }
        for(int m=1+9*len_a; m<j; m++){
                A_[m]=(double)l0_i+1.0;
		//Z=Z+exp(A_[m]/m+f_0*exp(m-l_0)/m);
		//printf("%f\n",A_[m]);
        }

	Z=0;
	double kKb=1e-0;
	double l1_i=0;  
	double zin1;
	double zin2;
	double akb;
	akb = f_0/Kb;
	for(int h=0; h<j; h++){
		//printf("%f\n",Z);
		l1_i += 1.0;
		//Z += exp(((N*A_[h])/l1_i) + ((a*f_0)/((1.0+exp(l_0-l1_i))*Kb)));
		zin1=(A_[h]*kKb)/l1_i ;
	  zin2 =(akb*a)/(1.0+exp(l_0-l1_i));
		Z += exp(zin1-zin2);
		//printf("%f\n",Z);
		//Z +=(A_[h]/l1_i) + (f_0*exp(l1_i-l_0)/l1_i);
	}

	//printf("%f\n",Z);

	//make_a(A_);

	//double z;
	//Z=make_z(A_);


	FILE* fp0;
       	fp0 = fopen("kkb1e-0_f0_1e-12_l080.dat" , "w");
 	if(fp0==NULL){
 		printf("File open faild.");
	 }

	double l_i=0;
	for(int i=0; i<j; i++){
		l_i += 1.0;
		double n_i=0.0;

		zin1=(A_[i]*kKb)/l_i ;
    zin2 =(akb*a)/(1.0+exp(l_0-l_i));

		n_i=N*exp(zin1-zin2)/Z;
		
		double c_i =log(n_i);
		double log_l_i=log(l_i);
		double al=A_[i]/l_i;

		printf("%f\n",n_i);
		fprintf(fp0, "%f\t%f\t%f\t%f\n",l_i,n_i,log_l_i,c_i);
		
	}
	fclose(fp0);
	
	return 0;
}
