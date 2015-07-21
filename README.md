# The Businessifier

The best businessification tool on the Internets.

##Introduction
Have you ever wanted to lose weight, impress your boss, meet beautiful women, and finally get that promotion?

This tool does none of those things.

It does however take wordlists and removes content clients and cusomters may find objectionable.

How objectionable you ask? Well lets just say that we can confidently assert that any wordlist sanitized via The Businessifier is safe to pass a rigourous inspection by even the most conservative and discerning clients, or your money back (see GPL in repo).

Our crack team of Internet experts has worked around the clock to ensure that The Businessifier Detection Engine is kept current with the most cutting edge swear words and objectionable content from the dark corners of the Nets. This includes words such as f\*\*k, p\*\*n, and even the rarely seen a\*\*\*\*\*2.

Scientific tests performed by real people wearing labs coats has shown that regular use of The Businessifier can increase client satisfaction by as much as 33%.

So ask yourself; Can you afford *not* to use it?

No. No you can't.

##Features
  - Sanitize wordlists with ease!
  - Detection based on real wordlists!
  - Written in Python!
  - Several command line flags!
  - Works directly in Kali!
  - Gluten free!
  - Commented!

##Example Usage
```sh
root@kali:~/tools/businessifier# ./businessifier.py --help
usage: businessifier [-h] [-v] [-c CONFIGFILE] [-i INPUT] [-o OUTPUT]

Businessify wordlists by removing inapproprate content

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -c CONFIGFILE, --configfile CONFIGFILE
                        override the default config file
  -i INPUT, --input INPUT
                        input filename, defaults to stdin
  -o OUTPUT, --output OUTPUT
                        output filename, defaults to default.bfr_out

Written by TheTwitchy. For more information, see
https://github.com/TheTwitchy/businessifier
```

```sh
root@kali:~/tools/businessifier# ./businessifier.py -i /usr/share/wordlists/dirb/common.txt -o ~/common_sanitized.txt
The following words have been removed from the wordlist:
 crack
 evil
 fuck
 fuckoff
 fuckyou
 hack
 hacker
 hacking
 hackme
 hardcore
 nude
 porn
 pr0n
 sex
 shit
 spyware
 terrorism
 teste
 torrent
 torrents
 viagra
 XXX
 xxx
 warez

If you see a mistake, please open a new issue at
https://github.com/TheTwitchy/businessifier
and include the word and wordlist source.

```

##FAQs
  - Who in the world is this for?
      - This is for anyone who wants to not have to explain to a client why they searched for "pr0n" on a system where very serious businessing happens.
  - What wordlists were used to build the initial searches?
      - The dirb common wordlist was the main one, but we've noticed it works with most common wordlists for web directory brute forcing.
  - Will this work with a password list for an online brute force attack?
      - Probably, but maybe glance through the final wordlist to make sure it didn't miss anything. It should grab most of the obvious stuff, but something huge like rockyou will probably let a lot slip through the cracks.
  - Will this work with a password list for an offline brute force attack?
      - Did you read any of the docs? Go sit in the corner.
  - I found a false positive/false negative.
      - That's not really a question, but open up an Issue on Github and tell us what wordlist it was and what the word was.
  - What wordlists are on the TODO list?
      - Probably the main DirBuster wordlists once we have the time, funding, and willpower.
  - I'm having trouble meeting women, what advice can you offer me?
      - It all boils down to one simple rule: people want to meet and mingle with interesting people. Try to find a way to be that interesting person by going to the gym, reading books, or learning a new hobby. This has the added benefit of expanding your horizons and social circle. It's win-win for everyone.


