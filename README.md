                        ██████╗░░██╗░░░░░░░██╗██████╗░
                        ██╔══██╗░██║░░██╗░░██║██╔══██╗
                        ██████╔╝░╚██╗████╗██╔╝██║░░██║
                        ██╔═══╝░░░████╔═████║░██║░░██║
                        ██║░░░░░░░╚██╔╝░╚██╔╝░██████╔╝
                        ╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═════╝░

                      (c) 2021-2022 by Seth Wallace / Maxproton
             <maxpr0t0n@protonmail.com> https://github.com/sethvoid/pwd
               Licensed under Apache License 2.0 (see LICENSE file)

           Please do not use in military or for illegal purposes.
      (This is the wish of the author and non-binding. Many people working
       in these organizations do not care for laws and ethics anyways.
            You are not one of the "good" ones if you ignore this.)

Introduction
------------
So you have crawled a target's website, or perhaps looked on social media, you have there kids names, where they went 
to school and now got a list of about 4 to 8 words? what's next? You need to create a list of potential combinations next
and pwd does just that. It takes these words, combines them and creates a list of potential passwords for use in something
like hydra etc. 

Combinations 
------------
pwd comes with some combinations baked in for example

[word1] would represent the first word on the list, it would then iterate through the other words and combine them like so:

[word1][word2]]

[word1].[word2]

[word1]1234

[word1].[word2].1234

These are just some of the examples of combinations pwd will generate. 

Usage
----
pwd is a php|python script and is ran as follows 

<code>
php pwd.php --file=[path to list of words] --output=[where you want the list saved] 

python3 pwd.py -f [path to list of words] -o [where you want the list saved]
</code>

<code>--file</code> and <code>--output</code> are mandatory

Non-mandatory arguments 
-----------------------
<code>--vvv</code> verbose mode - displays everything!
<code>--help</code> show a simple help. 

WARNING
-------
Using a list of more than 8 to 10 words will produce a very large password list.

Future improvements
-------------------
* Add a file split feature




