Do
    result = MsgBox("Voulez-vous continuer ?", vbYesNo + vbQuestion, "Confirmation requise")
    If result = vbNo Then
        MsgBox "Vous ne pouvez pas dire non !", vbExclamation, "Erreur"
    End If
Loop While result = vbNo
