rem the path to this repository
set REPOS=%1
rem the number of the revision just committed.
set REV=%2
 
set HOOK_DIR=F:\Repositories\local_svn\hooks
set PYTHON_BIN=C:\Python35\python.exe
%PYTHON_BIN% %HOOK_DIR%/mailer.py %REPOS% %REV%