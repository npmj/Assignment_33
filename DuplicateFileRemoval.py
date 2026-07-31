##########################################################
#
#   Importing required libraries
#
##########################################################

import sys
import os
import time
import schedule
from Modules import ChekSumModule
from Modules import MailModule

##########################################################
#
#   Function name :     FindDuplicate
#   Input :             Name of Directory
#   Description :       Finds duplicate files in the specified
#                       directory using their checksum, 
#   Date :              27/07/2026   
#   Author :            Neha Jayvant Kadam
#
##########################################################


def FindDuplicate(DirectoryName):
    Ret = False
    Ret = os.path.exists(DirectoryName)

    if (Ret == False):
        return

    Ret = os.path.isdir(DirectoryName)

    if (Ret == False):
        return

    Duplicate = {}

    for FolderName , SubfolderName, FileName in os.walk(DirectoryName):

        for fName in FileName:

            fName = os.path.join(FolderName,fName)

            CheckSum = ChekSumModule.CalculateCheckSum(fName)

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fName)
            else:
                Duplicate[CheckSum] = [fName]

    return Duplicate  

##########################################################
#
#   Function name :  RemoveDuplicateFile
#   Input         :  Directory name
#   Output        :  Removes duplicate files and generates
#                    a log report.
#   Description   :  deletes the duplicate copies while retaining one
#                    original file, creates a log file
#                    containing details of the deleted files,
#                    and sends the log report via email.
#   Date           : 27/07/2026   
#   Author         : Neha Jayvant Kadam
#
##########################################################              

def RemoveDuplicateFile(DirectoryName,Receiver_Email):
    Border = "-"*50

    MyDict = FindDuplicate(DirectoryName)

    Result = list(filter(lambda x : len(x) > 1,MyDict.values()))

    StartTime = time.strftime("%d %B %Y, %I:%M:%S %p")
    TimeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    TotalFileScanned = 0
    TotalDeleted = 0
    Count = 0
    DeletedFiles = []
    ChecksumValues = []
    Errors = []
    TotalDuplicateFiles = 0
    
    
    LogFile = os.path.join(DirectoryName,"Marvellous_%s.log" % TimeStamp)
    fobj = open(LogFile,"w")

    fobj.write("           Duplicate File Removal Report\n")
    fobj.write(Border + "\n\n")

    for value in Result:
            TotalFileScanned = TotalFileScanned + 1
            TotalDuplicateFiles = (TotalDuplicateFiles + len(value)) - 1 

            for subValue in value:

                Count = Count + 1

                if (Count > 1):
                    try:
                        ChecksumValues.append(ChekSumModule.CalculateCheckSum(subValue))

                        os.remove(subValue)

                        DeletedFiles.append(subValue)

                        TotalDeleted = TotalDeleted + 1
                        
                    except Exception as e:
                        Errors.append(str(e))    
            Count = 0

    EndTime = time.strftime("%d %B %Y, %I:%M:%S %p")

             
    absDirectoryName = os.path.abspath(DirectoryName)   
    fobj.write(f"Starting time of directory scanning          : {StartTime}\n")
    fobj.write(f"Completion time of directory Scanning        : {EndTime}\n")
    fobj.write(f"Name of directory Scanned                    : {absDirectoryName}\n")
    fobj.write(f"Total number of files scannedund             : {TotalFileScanned}\n")
    fobj.write(f"Total number of duplicate files Found        : {TotalDuplicateFiles}\n")
    fobj.write(f"Total number of duplicate files Deleted      : {TotalDeleted}\n\n")

    fobj.write("Complete paths of all deleted duplicate files:\n")
    if DeletedFiles:
        for file in DeletedFiles:
            fobj.write(file + "\n")
    else:
        fobj.write("None\n")

    fobj.write("\nChecksum values of duplicate files:\n")
    if ChecksumValues:
        for checksum in ChecksumValues:
            fobj.write(checksum + "\n")
    else:
        fobj.write("None\n")

    fobj.write("\nErrors encountered during execution:\n")
    if Errors:
        for error in Errors:
            fobj.write(error + "\n")
    else:
        fobj.write("No Errors\n")


    Email_Subject = "Duplicate File Removal Report"
    Email_Body = f"""
    Jay Ganesh,

    The duplicate file removal operation has been completed successfully.

    Operation Statistics:

    Starting time of scanning: {StartTime}
    Completion time of scanning: {EndTime}
    Directory scanned: {DirectoryName}
    Total number of files scanned: {TotalFileScanned}
    Total number of duplicate files found: {TotalDuplicateFiles}
    Total number of duplicate files deleted: {TotalDeleted}

    Please find the detailed log file attached to this email.

    Regards,
    Neha Kadam
    """      
            
    Ret = MailModule.SendMail(FileName = LogFile,ReceiverEmail = Receiver_Email, Subject = Email_Subject,Body = Email_Body)

    if Ret == True:
        fobj.write("Email delivery status : Success\n")
    else:
        fobj.write("Email delivery status : Failed\n") 
               
    fobj.write(Border+"\n")
    fobj.write("--------------- End of Log File ----------------\n")
    fobj.write(Border+"\n")
    fobj.close() 


##########################################################
#
#   Function name :     main
#   Input :             Time interval (minutes), Directory path 
#   Description :       Schedules the duplicate file removal task
#                       at the specified time interval and keeps
#                       the scheduler running continuously.
#   Date :              27/07/2026   
#   Author :            Neha Jayvant Kadam
#
##########################################################             
                   

def main():
    Border = "-"*80
    print(Border)
    print("---- Duplicate File Removal Automation ----")
    print(Border)
        
    # --h & --u handleing
    if (len(sys.argv) == 2):
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script scans a directory, identifies duplicate files using checksum,")
            print("deletes duplicate files, creates a log file, and sends the log file thriugh email.\n")
                    
                    
        elif(sys.argv[1] == "--usage" or sys.argv[1] == "--u"):
            print("Usage:")
            print("python DuplicateFileRemoval.py <IntervalMinutes> <DirectoryPath> <ReceiverEmail>\n")

            print("Example:")
            print("python DuplicateFileRemoval.py 1 E:/Data/Demo your_email@gmail.com\n")

            print(f"python {sys.argv[0]} <Time_Interval> <Folder_Name> <Receiver_Email>\n")
            print("Time_Interval : Time interval in minutes for periodic execution")
            print("Folder_Name   : Path of the directory to scan for duplicate files")
            print("Receiver_Email: Email address to receive the log file")
        else:
            print("Unable to proceed as there is argument is not matching") 
            print("Plase Use --h or --u gettig more details")

    elif (len(sys.argv) == 4):
        print("Scedulaer Started Sucessfully")
        print("Press Ctrl + C to abort the automation script")
        schedule.every(int(sys.argv[1])).minutes.do(RemoveDuplicateFile,sys.argv[2],sys.argv[3])
        
        while True:
            schedule.run_pending()
            time.sleep(1)
        
    else:
        print("Invalid Number of Argumnets")  
        print("Unable to proceed as there is argument is not matching")  
        print("Plase Use --h or --u gettig more details")     
        
        
        
    print(Border)
    print("---- Thank You for using automation system ----")
    print(Border)
    

##########################################################
#
#   Starter of the automation script
#
##########################################################

if __name__ == "__main__":
    main()