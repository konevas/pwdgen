# pwdgen
Password generator. Generates password from key phrase.

## Example:

```shell
python pwdgen.py -k key_phrase -l 12
Jks<LB|Os~"4
```

## Usage
```
pwdgen.py [-h] [-k KEYWORD] [-l LENGTH]

optional arguments:
-h, --help            show this help message and exit
-k KEYWORD, --keyword KEYWORD
                        Keyword
-l LENGTH, --length LENGTH
                        Generated password length
```

>**Note**
Agorithm ensures that at least one punctuacion, one lowercase and one uppercase symbol is in the generated password.
