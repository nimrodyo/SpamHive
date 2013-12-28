SpamHive
========

SpameHive is a new website dedicated to receive spam emails or any other suspicious email.

SpamHive will analyze the spam for you, it will extract every detail in that email and cross it with other data known to be malicious.

Usage:
 - Users will forward their spam email to SpamHive email address. A response email will be sent back to the user with link to SpamHive analysis report.
 - Users will upload emails in various formats (eml, emlx, msg, mbx, txt, etc...) and will receive analysis response in a few seconds.

Extracted Data:
 - SMTP Servers IP Adresses
 - Source email address
 - SMTP Headers
 - Signature Data
 - Domain Names & URL's
 - Attached Files
 - TXT Content

SpamHive will support the following features:
 - SPAM Filtering Services like SpamAssasin, Etc...
 - SPAM Blacklists:
  -  http://mxtoolbox.com/problem/blacklist/
  -  http://www.stopforumspam.com/
 - Indexed SMTP servers will be crosses against other projects such as: SPAMHAUS, and more...
 - Indexed URL & Domain Names will be crosses against PhishTank, ZeusTracker and more...
 - Source email Address, SMTP Headers, Signature Data, and TXT Content will be indexed and analyzed withing SpamHive DB.
 - Attached Files will be checked against VT and other OpenSource DB's.



Techonology:
- Server UI:  Django
- Email Analysis: Python at first
- DB: Need to check if NonSQL is usable....?
