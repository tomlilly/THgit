@echo off

REM Copy old key value to the new key with updated name eg "\lastProcessed_BAK"
REM REG COPY [OldKey] [NewKey] /s /f
REG COPY [HKEY_CURRENT_USER\Software\VB and VBA Program Settings\Locus\DMEmail\InBoxLastProcessedDate] [HKEY_CURRENT_USER\Software\VB and VBA Program Settings\Locus\DMEmail\InBoxLastProcessedDate_BAK] /s /f
REG COPY [HKEY_CURRENT_USER\Software\VB and VBA Program Settings\Locus\DMEmail\SentItemLastProcessedDate] [HKEY_CURRENT_USER\Software\VB and VBA Program Settings\Locus\DMEmail\SentItemLastProcessedDate_BAK] /s /f

REM Delete the old key
REM REG DELETE [OldKey] /f
REG DELETE [HKEY_CURRENT_USER\Software\VB and VBA Program Settings\Locus\DMEmail\InBoxLastProcessedDate] /f
REG DELETE [HKEY_CURRENT_USER\Software\VB and VBA Program Settings\Locus\DMEmail\SentItemLastProcessedDate] /f

REM results in existing key value stored in newly named key as backup, default key will be created at run
