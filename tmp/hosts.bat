＠echo on
pip install paramiko
cls
:menu
ECHO.
ECHO ...............................................
ECHO 請選擇功能
ECHO ...............................................
ECHO.
ECHO 1 - 開啟遠端管理網站網頁
ECHO 2 - 關閉遠端管理網站網頁
ECHO 3 - 開始網站
ECHO 4 - 闗閉網站
ECHO 5 - EXIT
ECHO.
SET /P M=Input 1, 2, 3, 4, 5 then press ENTER:
IF %M%==1 GOTO S1M
IF %M%==2 GOTO S2M
IF %M%==3 GOTO S3M
IF %M%==4 GOTO S4M
IF %M%==5 GOTO EOF
:S1M
start python C:\tmp\startRemoteHost.py
pause
:S2M
start python C:\tmp\stopRemoteHost.py
pause
:S3M
start python C:\tmp\startWWW.py
pause
:S4M
start python C:\tmp\stopWWW.py
pause
:EOF
exit /b
GOTO menu