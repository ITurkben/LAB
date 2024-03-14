$headers = @{
    "Authorization" = "Bearer "
    "Content-Type" = "application/json"
}

$body = @{
    "model" = "tts-1-hd"
    "input" = "Bonjour et bienvenue dans la société Groupe Lepine, enlevez vos chaussures"
    "voice" = "shimmer"
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri "https://api.openai.com/v1/audio/speech" -Method Post -Headers $headers -Body $body -OutFile "speech.mp3"
