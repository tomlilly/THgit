@echo off

REM Copy old key value to the new key with updated name eg "\lastProcessed_BAK"
REG COPY [OldKey] [NewKey] /s /f

REM Delete the old key
REG DELETE [OldKey] /f

REM results in existing key value stored in newly named key as backup, default key will be created at run