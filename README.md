# QUICK CLIPBOARD IMAGE SAVE
This script saves the image in your clipboard to a folder in your computer in "C:/Users/\[your\_user]/Pictures/ClipboardImage". The next time you use the script. it will delete the previous image saved there and replace it with the current one in your clipboard. That way those random images you needed to only download once will not take up all your drive space in "~/Downloads".

The only thing the batch file does is run the Python script. It was included because it has console icon when pinned to the Start Menu or Taskbar.



## Pin script to Task Bar or Start Menu
If you want to have this script accessible from the Taskbar or Start Menu, there are a couple extra steps you must take:

### 1. Make a shortcut
   Make a shortcut for the batch file. You can also make the shortcut for the python file, but it will use the miscellaneous executable file icon, which looks worse.

   
### 2. Change the TARGET
   Open the shortcut's properties, and change the TARGET. It should show something like "C:/Users/\[name]/Programs/clipboard-image.bat".
   What you should do is add "cmd.exe c/ " at the beginning of the TARGET. It will end up looking something like "cmd.exe c/ C:/Users/\[name]/Programs/clipboard-image.bat".

   
### 3. Pin it
   Right-click on the new shortcut, click "Show More Options", and finally pin it to the Taskbar or Start Menu.



## Note

ChatGPT assisted with the debugging of the script.
