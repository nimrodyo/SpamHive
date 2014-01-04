__author__ = 'nimrod'

from elasticsearch import Elasticsearch

class DAO:
    es = None

    def __init__(self):
        self.es = Elasticsearch()

    def InsertContent(self, jsonContent):
        insertResult = self.es.index(index="contentIndex", doc_type="content", body=jsonContent)
        print(insertResult)

    def InsertSMTPNode(self, smtpNode):
        #insertResult = self.es.index(index="nodesIndex", doc_type="smtpNode", body=smtpNode)
        None



    def InsertSMTPNodes(self, smtpNodes):
        for smtpNode in smtpNodes:
            self.__InsertSMTPNode(smtpNode)


