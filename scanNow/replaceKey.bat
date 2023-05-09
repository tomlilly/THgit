@echo off
REM Copy the old key to the new key
REG COPY [OldKey] [NewKey] /s /f
REM Delete the old key
REG DELETE [OldKey] /f