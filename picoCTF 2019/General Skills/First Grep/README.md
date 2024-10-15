# First Grep : General Skills

Can you find the flag in [file](file)? This would be really tedious to look through manually, something tells me there is a better way.

Author : Alex Fulton, Danny Tunitis

# Solution

タイトルより、grepを使いたくなるほど大量の文字が並んでいると推測できる。
```
$ file file
file: ASCII text, with very long lines (4200)
```
stringsとgrepでフラグを探す。
```
$ strings file | grep pico
picoCTF{grep_is_good_to_find_things_f77e0797}
```

flagが得られた。

`picoCTF{grep_is_good_to_find_things_f77e0797}`
