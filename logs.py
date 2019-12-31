'''
Programl: logs.py
Developer: Dhiraj
Date: 01/01/2020

Note:
    This program is just an example of how to take logs of the output of commands which are ran in cmd/linux shell.

'''

import logging
from os import getcwd
import subprocess

#class for logs
class LOGS():

    #--------------------------------------------------------------------------------------------------
    '''
    initializing log file
    '''
    def __init__(self):
        
        #filname = path + <LogFileName>
        #level = DEBUG
        #format = format of the text in logs e.g. Date-Time -> Programfile -> Module -> Funcaiton Name -> Message

        logging.basicConfig(
            filename= getcwd() + '\\MyLogs.log',
            level=logging.DEBUG,
            format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s -> %(funcName)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')

    #--------------------------------------------------------------------------------------------------
    
    '''
    This function will clear the unnecessary '\n', '\r', '\t' etc. then format the output and log it.
    '''

    def formatting_and_logging(self, output):

        output = output.replace("(b'", '')
        output = output.replace(', None)', '')
        output = output.split("\\n") 

        for line in output:
            line = line.replace('\\r', '')
            if line:
                logging.info(line)
                #print(line)
    
    #--------------------------------------------------------------------------------------------------

    '''
    This function will read some windows commands from a text file and run using subprocess,
    then the output of the commands will be store in the log file.
    '''
    def read_Commands(self):

        # reading commands from file
        cmds = open(getcwd() + '\\commands.txt', 'r')
        
        # going through eachline
        for line in cmds.readlines():

            try:
                # replacing '\n' from the line to get only command
                cmd = line.split('\n')[0]
                print(cmd)               
                logging.info(cmd)

                # using the Popen function to execute the command and store the result in temp. 
                # it returns a tuple that contains the data and the error if any. 
                temp = subprocess.Popen(cmd, stdout = subprocess.PIPE)

                # we use the communicate function 
                # to fetch the output 
                output = str(temp.communicate()) 

                self.formatting_and_logging(output)
  
            except Exception as e:
                # if some errors happens it will log as error
                logging.error(e)


#Creating instance
log = LOGS()

log.read_Commands()