
Go to the directory mentioned
```
mcskidy@tbfc-web01:~$ cd /home/mcskidy/Documents/
mcskidy@tbfc-web01:~/Documents$ ls
read-me-please.txt
mcskidy@tbfc-web01:~/Documents$ cat read-me-please.txt 
```

from the file we get the login credentials
> username: eddi_knapp
> word: S0mething1Sc0ming

change user
```
mcskidy@tbfc-web01:~/Documents$ sudo su
root@tbfc-web01:/home/mcskidy/Documents$ su eddi_knapp
eddi_knapp@tbfc-web01:/home/mcskidy/Documents$ cd ~
eddi_knapp@tbfc-web01:~$ ls -al
-rw-r--r--  1 eddi_knapp eddi_knapp 3797 Nov 11 16:24 .bashrc
```
go to home directory and do ls

> 1. “I ride with your session, not with your chest of files. Open the little bag your shell carries when you arrive.”

Decoding the Riddle:
- “Ride with your session” → exists during your login session
- “Not with your chest of files” → not stored in permanent files
- “Little bag your shell carries” → shell environment variables

Solution:
Environment variables are typically set in shell configuration files like `.bashrc`, which loads when you start a shell session.

```
eddi_knapp@tbfc-web01:~$ cat .bashrc

export PASSFRAG1="3ast3r"
```

> <span style="color:rgb(255, 0, 0)">PASSFRAG1="3ast3r"</span>

> 2) The tree shows today; the rings remember yesterday.  
Read the ledger’s older pages.

Decoding the Riddle:
- “Tree shows today” → current state of a git repository
- “Rings remember yesterday” → like tree rings, git commits record history
- “Ledger’s older pages” → old commit history

Solution:
Git repositories maintain complete history of all changes, including deleted content. Even if sensitive information is removed in a later commit, it remains in the repository history.

From the home directory listing:

![|556x434](./attachments/image.png)

```
eddi_knapp@tbfc-web01:~$ cd .secret_git
eddi_knapp@tbfc-web01:~/.secret_git$ ls -al
drwx------  8 eddi_knapp eddi_knapp 4096 Nov 11 12:07 .git

eddi_knapp@tbfc-web01:~/.secret_git$ cd .git
eddi_knapp@tbfc-web01:~/.secret_git/.git$ ls -al
-rwx------  1 eddi_knapp eddi_knapp  467 Nov 11 12:07 COMMIT_EDITMSG

eddi_knapp@tbfc-web01:~/.secret_git/.git$ cat COMMIT_EDITMSG 
# Last commands done (2 commands done):
#    edit b65ff21 add private note
#    pick 98f546c remove sensitive note
# No commands remaining.
# You are currently rebasing branch 'master' on '0a7462a'.
#
# Changes to be committed:
#	deleted:    secret_note.txt

eddi_knapp@tbfc-web01:~/.secret_git/.git$ git show b65ff21:secret_note.txt
PASSFRAG2: -1s-
```

OR

```
eddi_knapp@tbfc-web01:~/.secret_git$ git log --all --full-history
commit e924698378132991ee08f050251242a092c548fd (HEAD -> master)
Author: mcskiddy <mcskiddy@robco.local>
Date:   Thu Oct 9 17:20:11 2025 +0000
    remove sensitive note

eddi_knapp@tbfc-web01:~/.secret_git$ git show e924698378132991ee08f050251242a092c548fd

-PASSFRAG2: -1s-
```

> <span style="color:rgb(255, 0, 0)">PASSFRAG2: -1s-</span>

**Clues 3:**

> When pixels sleep, their tails sometimes whisper plain words.  
Listen to the tail.

Decoding the Riddle:
- “Pixels sleep” → static/stored images
- “Tails sometimes whisper plain words” → data hidden at the end of image files
- “Listen to the tail” → use tools like `tail`, `strings`, or check file metadata

Solution:
The riddle suggests looking at image files, specifically their “tails” (end of file) or metadata.

```
eddi_knapp@tbfc-web01:~$ cd Pictures/
eddi_knapp@tbfc-web01:~/Pictures$ ls -la
-rw-rw-r--  1 eddi_knapp eddi_knapp    1442 Oct  9 18:07 .easter_egg

eddi_knapp@tbfc-web01:~/Pictures$ cat .easter_egg
PASSFRAG3: c0M1nG
```

> <span style="color:rgb(255, 0, 0)">PASSFRAG3: c0M1nG</span>

## Combine the Password Fragments

Assemble the three fragments in order:

- PASSFRAG1: `3ast3r`
- PASSFRAG2: `-1s-`
- PASSFRAG3: `c0M1nG`

**Complete Password:** `3ast3r-1s-c0M1nG`

![|432x375](./attachments/image-1.png)

```
eddi_knapp@tbfc-web01:~$ cd Documents/
eddi_knapp@tbfc-web01:~/Documents$ ls -la
-rw-rw-r--  1 eddi_knapp eddi_knapp 1004 Nov 14 19:31 mcskidy_note.txt.gpg
```

**Decrypt using GPG:**
```
gpg --batch --passphrase "3ast3r-1s-c0M1nG" -d mcskidy_note.txt.gpg
```

> <span style="color:rgb(255, 0, 0)">UNLOCK_KEY: 91J6X7R4FQ9TQPM9JX2Q9X2Z</span>

![|641x324](./attachments/image-2.png)

