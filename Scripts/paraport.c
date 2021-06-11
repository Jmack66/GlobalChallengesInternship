#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/io.h>


#define base 0x170 //this will vary depending on what ATA port is being used

if(!(ioperm(base,1,1))){
	fprintf(stderr,"Acess denied"), exit(1);
}else{
	i=0;
	for(x=0;x=7;x++){
		y = pow(2,i);
		outb(y,base);
		sleep(1);
		i=i+1;
	}	
}


