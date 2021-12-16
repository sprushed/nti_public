# chinasocialcredit
Смысл задания заключается в том, что надо узнать секретное китайское приветствие, которое по совместительству является флагом. Проверка флага находится в библиотеке check.so, которая подгружается в check.py
## Алгоритм check.so
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
По сути, алгоритм довольно прост:
1. Сначала проверяется, является ли введенная строка размером 35 символа. Если проверка выполнена, продолжаем
1. Делается memfrob введенной строки
1. Каждый введенный символ ксорится с предыдущим, причем нулевой ксорится с 34ым.
1. Полученные байты проверяются с помощью memcmp (в декомпиле оно оказалось inline)
## Решение
Обратить алгоритм возможно, для этого надо:
1. Понять, что первый символ флага - f
1. Построить плейнтекст. Каждый iый элемент плейнтекста = шифротекст[i] ^ шифротекст[i-1]
1. Поксорить каждый элемент плейнтекста с 42.
1. ???
1. PROFIT
Пример решения можно найти в скрипте solve.py
