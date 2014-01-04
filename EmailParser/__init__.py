__author__ = 'nimrod'

from email.parser import Parser

import DAO
from EmailParser import NodeParser



class EmailParser:
    emailHeaders = None

    def __init__(self):
        self.dbObeject = DAO.DAO()

    #@staticmethod
    def ParseEmail(self, fileEmail):
        self.emailHeaders = Parser().parse(fileEmail)
        if self.emailHeaders is None:
            print "Failed to parse Email headers..."
            exit()

        #Parse Nodes
        #Parse Source Emails
        #Parse Destination Emails
        #Parse Other X-Headers
        #Parse URL's from Content

    def Store(self):
        if self.emailHeaders is not None:
            # for each SMTP node store in DB
            for smtpNode in self.emailHeaders.get_all("Received"):
                print smtpNode
                self.dbObeject.InsertSMTPNode(smtpNode)
        else:
            print "Please Call ParseEmail() First..."
            exit()


