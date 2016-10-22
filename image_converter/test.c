#include <stdio.h>
#include "imgdata.h"

#define height 48
#define width 84

int main() {
	int x, y;
	for( y = 0; y < height; y++ ) {
		for( x = 0; x < width; x++ ) {
			int i = x * height + y;
			int j = i / 8;
			int r = i % 8;
			int v = (img_data[j] >> r) & 0x01;
			printf( v ? "x" : " " );
		}
		printf("\n");
	}
}
