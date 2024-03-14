# Importer le module ImportExcel
Import-Module ImportExcel

# Chemin du fichier Excel d'entrée
$inputFilePath = "‪C:\Users\itu\Documents\LAB\Projet_automatisation_creation_profil\test.xlsx"
# Chemin du fichier Excel de sortie
$outputFilePath = "‪C:\Users\itu\Documents\LAB\Projet_automatisation_creation_profil\"

# Lire les données depuis le fichier Excel
$users = Import-Excel -Path $inputFilePath

# Fonction pour générer le trigramme
function GenerateTrigram($firstName, $lastName) {
    $trigram = ($firstName[0] + $lastName[0..1]) -join ''
    return $trigram.ToLower()
}

# Fonction pour générer un mot de passe
function GeneratePassword() {
    $password = [System.Web.Security.Membership]::GeneratePassword(12, 2)
    while ($password -notmatch "[A-Z]" -or $password -notmatch "\d" -or $password -notmatch "\W") {
        $password = [System.Web.Security.Membership]::GeneratePassword(12, 2)
    }
    return $password
}

# Ajouter les nouvelles informations
foreach ($user in $users) {
    $user.Trigram = GenerateTrigram $user.Prénom $user.Nom
    $user.MotDePasse = GeneratePassword
    $user.Email = ("{0}.{1}@groupe-lepine.com" -f $user.Prénom[0], $user.Nom).ToLower()
}

# Écrire les données dans un nouveau fichier Excel
$users | Export-Excel -Path $outputFilePath

Write-Host "Le fichier a été généré : $outputFilePath"
