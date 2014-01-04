__author__ = 'nimrod'

import EmailParser

mailManager = EmailParser.EmailParser()

emailFile = open(r"D:\Projects\GitHub\SpamHive\tests\email1.eml", 'r')

mailManager.ParseEmail(emailFile)

mailManager.Store()





