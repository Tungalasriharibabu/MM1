from time import gmtime, strftime
      
class CommonLibrary:
    
    def __init__(self):
       pass
    def generation_of_unique_id(self,type):
        uniqueNumber = strftime("%Y%m%d%H%M%S", gmtime())
        uniqueTimeStamp=str(uniqueNumber)
        uniqueId=uniqueTimeStamp
        x=uniqueId[-7:]
        uniqueIds=x
        mmMailFormat='rhwpte+'+type+uniqueIds+'@gmail.com'
        print mmMailFormat
        return mmMailFormat
