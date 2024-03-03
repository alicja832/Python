#include "zad2.h"
#include <stddef.h>
#include <stdio.h>
void swap(int *a,int *b)
{
    int tmp=*a;
    *a=*b;
    *b=tmp;

}
void sort_one(int A[],int n)
{
    int i,j;
    int k;
     for (i=2;i<n;i++){
      //Wstaw A[i] w posortowany ciąg A[1 ... i-1]
     k = A[i];
     j = i - 1;
     while (j>0 && A[j]>k){
         A[j+1]=A[j];
          j = j - 1;
     }
     A[j + 1] = k;
     }
}
