Set oWMP = CreateObject("WMPlayer.OCX.7" )
Set colCDROMs = oWMP.cdromCollection
if colCDROMs.Count >= 1 then
    For i = 0 to colCDROMs.Count - 1
        colCDROMs.Item(i).Eject
        WScript.Sleep 2000
        colCDROMs.Item(i).Eject
    Next
End If
Set oWMP = Nothing
