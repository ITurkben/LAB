# Sp�cifiez le chemin complet de la nouvelle image de fond d'�cran
$ImagePath = "C:\les_des_du_destins.png"

# Utilisez SystemParametersInfo pour changer le fond d'�cran
Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public class Wallpaper {
    [DllImport("user32.dll", CharSet = CharSet.Auto)]
    public static extern int SystemParametersInfo(int uAction, int uParam, string lpvParam, int fuWinIni);
}
"@

# D�finissez les constantes pour SystemParametersInfo
$SPI_SETDESKWALLPAPER = 0x0014
$SPIF_UPDATEINIFILE = 0x01
$SPIF_SENDCHANGE = 0x02

# Appliquez le nouveau fond d'�cran
[Wallpaper]::SystemParametersInfo($SPI_SETDESKWALLPAPER, 0, $ImagePath, $SPIF_UPDATEINIFILE -bor $SPIF_SENDCHANGE)
