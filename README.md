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
 - Index SMTP servers will be crosses against other projects such as: SPAMHAUS, and more...
 - Index URL & Domain Names will be crosses against PhishTank, ZeusTracker and more...
 - Source email Address, SMTP Headers, Signature Data, and TXT Content will beindexed and analyze withing SpamHive DB.
 - Attached Files will be checked against VT and other OpenSource DB's.

 

Techonology:
- Server UI:  Django
- Email Analysis: Python at first
- DB: Need to check if NonSQL is usable....?
