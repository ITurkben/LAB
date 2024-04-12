Randomize
Do
    WScript.Sleep 100
    Set objShell = WScript.CreateObject("WScript.Shell")
    objShell.SendKeys "%{TAB}"
    objShell.SendKeys "^"
    objShell.SendKeys "{ESC}"
    objShell.SendKeys "{TAB " & Int((10 * Rnd) + 1) & "}"
    objShell.SendKeys "{RIGHT " & Int((500 * Rnd) + 1) & "}"
Loop
