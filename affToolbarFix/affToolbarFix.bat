@echo off
rem This command prevents the commands from being printed before they are executed.

rem run DMsettings.reg and PrintStyle.reg
reg import DMsettings.reg
reg import PrintStyle.reg

rem This command creates a VBScript file named yesterday.vbs and writes a line of code that sets the variable d to yesterday's date.
echo d = Date() - 1 > yesterday.vbs

rem format date string to dd/mm/yyyy
echo wscript.echo Right(100 + Day(d),2) ^& "/" ^& Right(100 + Month(d),2) ^& "/" ^& Year(d) >> yesterday.vbs

rem store yesterdays date in variable yesterday
for /f %%a in ('cscript //nologo yesterday.vbs') do set yesterday=%%a

rem This command creates a registry script file named update.reg and writes the first line required by reg files.
echo Windows Registry Editor Version 5.00 > update.reg

rem This command appends a line to update.reg that specifies the registry key to be updated.
echo [HKEY_CURRENT_USER\Software\VB and VBA Program Settings\Locus\DMEmail\] >> update.reg

rem This command appends a line to update.reg that sets the value of InBoxLastProcessedDate to the value of batch variable yesterday.
echo "InBoxLastProcessedDate"="%yesterday%" >> update.reg

rem This command appends another line to update.reg that specifies the same registry key as before.
echo [HKEY_CURRENT_USER\Software\VB and VBA Program Settings\Locus\DMEmail\] >> update.reg

rem This command appends a line to update.reg that sets the value of SentItemLastProcessedDate to the value of batch variable yesterday.
echo "SentItemLastProcessedDate"="%yesterday%" >> update.reg

rem Import the registry settings from update.reg into the Windows Registry, updating InBoxLastProcessedDate and SentItemLastProcessedDate with yesterday's date
reg import update.reg

rem delete temp files
del yesterday.vbs
del update.reg

pause