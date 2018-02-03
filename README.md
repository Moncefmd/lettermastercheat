# lettermastercheat
Quickly hacked together script to cheat on letter master

The script utilizes a very interesting data structure which is called a **prefix tree**. A prefix tree can be used to check for the validity of any word in a given dictionary (in my case, francais.txt) while still being lightweight in memory. https://en.wikipedia.org/wiki/Trie

Everything in the script could probably be a lot more efficient, but hey, it works well enough !

### Usage :
Simply run main.py with python 3 and enjoy your cheating.

### Note : 
You may have to install some dependencies (pip install unidecode).
The dictionary used is from http://www.gwicks.net/dictionaries.htm, you can download almost any other latin language and it will work just as well



## Todo : 
Refactor code
Optimize algo
Give choice of language
