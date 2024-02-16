#This code is used to validate whether the XML is having the exempted list of values or not in the given sub node. If the values are not in exemption list get their mobile number.
#The XML is present as a single line in the input file, each ine is considered as one XML HUMAN DATA
#!USECASE: To all HUMANS MOBILENUMBER from file whose MARKSs & GRADEs from any DEGREE are in the excusion list
###Below is the XML Layout EX: Human Details

# <HUMAN>-->ROOT_TAG_NAME
#   <METADETA1></METADATA1>
#   <DETAILS>-->ROOT_TAG_NAME[1]
#    <STATE>--->ROOT_TAG_NAME[1][0]
#      <METADATA2></METADATA2>
#      <CATEGORY>--->ROOT_TAG_NAME[1][0][1]
#        <PERSONAL>
#          <NAME>PERSON NAME</NAME>
#          <MOBILE>1234567890</MOBILE>
#        </PERSONAL>
#        <ALL_DEGREE>
#          <DEGREE>
#            <NAME>POSTGRADUATE</NAME>
#            <MARKS>999</MARKS>
#            <GRADE>A</GRADE>
#          </DEGREE>
#          <DEGREE>
#            <NAME>UNDERGRADUATE</NAME>
#            <MARKS>998</MARKS>
#            <GRADE>B</GRADE>
#          </DEGREE>
#         <DEGREE>
#           <NAME>CLASS X</NAME>
#           <MARKS>996</MARKS>
#         </DEGREE>
#        </ALL_DEGREE>
#        </OTHERS>
#      </CATEGORY>
#     </STATE>
#   </DETAILS>
# </HUMAN>

###EXMAPLE 2 WHERE PERSON DOESN'T HAVE ANY DEGREE, SENT AS NULL FROM SOURCE
# <HUMAN>
#   <METADETA1></METADATA1>
#   <DETAILS>
#    <STATE>
#      <METADATA2></METADATA2>
#      <CATEGORY>
#        <PERSONAL>
#          <NAME>PERSON NAME</NAME>
#          <MOBILE>1234567890</MOBILE>
#        </PERSONAL>
#        </ALL_DEGREE>
#        </OTHERS>
#      </CATEGORY>
#     </STATE>
#   </DETAILS>
# </HUMAN>
###EXAMPLE 2

###END of XML Layout

import re
import xml.etree.ElementTree as XML

codes=[]
letters=[]
writeIntoFile=True
prefixList=['M','L','P'] #GRADEs exclusion list
codeList=[123, 143,153, 163] #MARKS exclusion list
getXML=re.compile(r'<HUMAN>(.*)</HUMAN>')#Pattern with which XML is present in the file, specifying the ROOT_TAG_NAME

with open(r'C:\path\to\folder\filename.txt','r',encoding='utf8') as readFile:
  with open(r'C:\path\to\final\data\name.txt','w') as writeFile:
    for fileLine in readFile:
      writeIntoFile=True
      xmlLine=getXML.search(fileLine).group() #Getting the string/pattern start-end based on the pattern given from fileLine
      #If  fileLine doesn't contain the pattern then xmlLine variable will have None value that need to validated before proceeding further, my assumption is that everyline in file will be one XML
      
      finalXML=XML.fromstring(xmlLine) #Converting the string format to XML format
      if xmlLine[1][0[1].find('ALL_DEGREE')==None or xmlLine[1][0[1].find('DEGREE')==None:
        mobileNumber=xmlLine[1][0[1].find('PERSONAL').find('MOBILE').text
        writeFile.write(mobileNumber+'\n') #Writing number into file directly as the searched CHILD_NODES does not exist in the XML value
      else:
        codes=[]
        letters=[]
        for child in xmlLine[1][0[1].find('ALL_DEGREE').findall('DEGREE'): #As ALL_DEGREE exist in XML DEGREE is mandatory it'll be in XML so not validated for None
          codes.append(int(child.find('MARKS').text)) #Loading the MARKS into list
          if child.find('GRADE') != None:
            letters.append(child.find('GRADE').text) #Loading the GRADE into list if exist
        for code in codes:
          if code in codeList:
            writeIntoFile:False  #Checking MARKSs found in the XML are in exemption list or not Viz codeList
        for letter in letters:
          if letter in prefixList:
            writeIntoFile:False #Checking GRADEs found in the XML are in exemption list or not Viz prefixList
        if writeIntoFile:
          mobileNumber=xmlLine[1][0[1].find('PERSONAL').find('MOBILE').text
          writeFile.write(mobileNumber+'\n') #As MARKSs & GRADEs found are not exemption list we're writing into new file
    print('Writing into file completed')
