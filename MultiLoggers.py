import logging

#------------------------------------------------------------------------METHOD STARTS
def createLogger(loggerName, logFileName, level=logging.INFO)
  logger=logging.getLogger(loggerName)                    #Creating logger by giving name
  formatting=logging.Formatter(%(message)s')              #Message format to write into logger
  createLogFile=logging.FileHandler(logFileName,mode='w') #Giving log file name & mode='a' for append file
  createLogFile.setFormatter(formatting)                  #Giving message format to log file

  logger.setLevel(level)                                 #Setting level to log file
  logger.addHandler(createLogFile)                       #Giving attributes to handler
  
#Including below line writes the logging to console along with the log file

  #stremHandler=logging.StreamHandler()
  #streamHandler.setFormatting(formatting)
  #logging.addHandler(streamHandler)

#-------------------------------------------------------------------------METHOD ENDS

#Logger1
createLogger('allLines','AllLinesDebug.log') #Logger name, File name
allLogger=logging.getLogger('allLines') #Get instance of given logger

#Below is the format of logging the message to file
#<logger instance name>.<logging level>('<message to file>') No need to include \n as it's already in logging

#Logger2
createLogger('refreshLines','RefreshData.log') #Logger name, File name
refreshLogger=logging.getLogger('refreshLines') #Get instance of given logger

##Performing logic
line='12345678901234567890'
mobileNumber=line[0:9] #For formatting the line and copying to log file

#Writing to log file 
allLogger.info('Mobile number found is '+line)
refreshLogger.info('Info refresh list '+mobileNumber)
