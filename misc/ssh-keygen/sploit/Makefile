.PHONY: default
default: libpon.so

libpon.o: sploitlib.c
	$(CC) -c -Wall -fpic sploitlib.c -o libpon.o

libpon.so: libpon.o
	$(CC) -shared -o libpon.so libpon.o
	-@rm libpon.o
