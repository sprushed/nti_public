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
