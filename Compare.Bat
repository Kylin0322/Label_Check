SET FileName=Label_Picture
SET FilePath=C:\Users\wangyu\OneDrive\learn\Python\VS_Code\Label_Check\
::pyinstaller -F C:\Users\wangyu\OneDrive\learn\Python\VS_Code\Label_Check\%FileName%.py
pyinstaller -F %FilePath%\%FileName%.py
pause
copy /Y %FilePath%\%FileName%.exe C:\Label_Check\
copy /Y %FilePath%\%FileName%.exe \\cnhuahpteserver\npi_program\Tools\Label_Check\
copy /Y %FilePath%\%FileName%.exe \\CNHUAM0HPFILE01\HP_Data\HP_TE\software\Label_Check\

pause
