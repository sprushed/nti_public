CC=clang

.PHONY: default
default: libpon.so
#default: libpon.so test
#	ssh-keygen -D ./libpon.so

test: main.c
	$(CC) main.c -o test
	sudo chown root:root test
	sudo chmod a+s test

libpon.o: sploitlib.c
	$(CC) -c -Wall -fpic sploitlib.c -o libpon.o

libpon.so: libpon.o
	$(CC) -shared -o libpon.so libpon.o
	-@rm libpon.o
