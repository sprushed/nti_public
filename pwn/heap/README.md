# heap

Это задание с классической идеей менеджера заметок. При анализе кода, мы видим, что все функции написано корректно, но присутствует одна интересная особенность: есть возможность однажды создать заметку с размером больше размера выделенного с помощью `malloc` участка памяти. Этого переполнения недостаточно для изменения "пользовательских" указателей в последовательно следующем чанке (1), но достаточно для изменения метаданных: второго элемента структуры чанка в Linux, размера чанка. 

```
struct malloc_chunk {
  INTERNAL_SIZE_T      mchunk_prev_size;  /* Size of previous chunk, if it is free. */
  INTERNAL_SIZE_T      mchunk_size;       /* Size in bytes, including overhead. */
  struct malloc_chunk* fd;                /* double links -- used only if this chunk is free. */
  struct malloc_chunk* bk;
  /* Only used for large blocks: pointer to next larger size.  */
  struct malloc_chunk* fd_nextsize; /* double links -- used only if this chunk is free. */
  struct malloc_chunk* bk_nextsize;
};

typedef struct malloc_chunk* mchunkptr;
```
Далее эксплуатация достаточно проста: мы освобождаем чанк с увеличенным размером (1) и создаём заново уже с новым размером (1). После этого можно получить ещё большее переполнение в последовательно следующий чанк (2). Теперь можно освободить чанк (2) и с помощью переполнения можно выполнить эксплуатацию классической уязвимости [tcache poisoning](https://github.com/shellphish/how2heap/blob/master/glibc_2.31/tcache_poisoning.c), таким образом получая arbitrary write. Так как в программе не включен механизм PIE, то произвольная запись автоматически даёт исполнение кода: просто переписываем любой указатель в Global Offset Table на [one gadget](https://pwnbykenny.com/en/2020/12/31/one-gadget-easy-powerful-tool-example).
