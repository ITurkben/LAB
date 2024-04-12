Dim objVoice
Set objVoice = CreateObject("SAPI.SpVoice")
Do
    objVoice.Speak "Attention, votre ordinateur a un virus. Ha, ha, ha. Juste une plaisanterie."
    WScript.Sleep 10000  ' Pause de 10 secondes
Loop
