Set objShell = CreateObject("WScript.Shell")
objShell.Run "control mouse"
WScript.Sleep 1000
objShell.SendKeys "{TAB}{TAB}{RIGHT}{TAB}{TAB}{TAB}{TAB}{TAB}{SPACE}{TAB}{TAB}{TAB}{TAB}{ENTER}"
WScript.Sleep 1000
