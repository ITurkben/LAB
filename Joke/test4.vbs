Dim objShell, i, strPath
Set objShell = CreateObject("WScript.Shell")

' Chemin vers l'image de fond d'écran
strPath = "‪C:\Windows\System32\SecurityAndMaintenance_Error.png"  ' Changez ce chemin vers l'image désirée

' Boucle pour changer le fond d'écran toutes les 10 secondes
For i = 1 to 10
    objShell.RegWrite "HKEY_CURRENT_USER\Control Panel\Desktop\Wallpaper", strPath
    objShell.Run "%windir%\System32\RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters", 1, False
    WScript.Sleep 10000  ' Délai de 10 secondes
Next
