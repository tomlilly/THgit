@echo off

rem create script file
echo d = date () - 1 > yesterday.vbs
rem ddmmyyyy
echo wscript.echo right (100 + day (d),2) & right (100 + month (d),2) & year (d) >> yesterday.vbs
rem yyyymmdd
:: echo wscript.echo year (d) * 10000 + month (d) * 100 + day (d) >> yesterday.vbs

rem store yesterdays date in variable yesterday
for /f %%a in ('cscript //nologo yesterday.vbs') do set yesterday=%%a

rem create the reg file
echo Windows Registry Editor Version 5.00 > update.reg
rem insert key between [], appends to update.reg
echo [HKEY_CURRENT_USER\Software\VB and VBA Program Settings\Locus\DMEmail\] >> update.reg
rem insert value to be updated between ""
echo "InBoxLastProcessedDate"="%yesterday%" >> update.reg
rem insert key between [], appends to update.reg
echo [HKEY_CURRENT_USER\Software\VB and VBA Program Settings\Locus\DMEmail\] >> update.reg
rem insert value to be updated between ""
echo "SentItemLastProcessedDate"="%yesterday%" >> update.reg

rem update the registry
reg import update.reg

rem delete temp files
del yesterday.vbs
del update.reg
