
Add-Type -AssemblyName System.Drawing

function Convert-PngToJpg {
    param (
        [string]$ImagePath,
        [int]$Quality = 80
    )

    if (-not (Test-Path $ImagePath)) {
        Write-Host "File not found: $ImagePath"
        return
    }

    try {
        $img = [System.Drawing.Image]::FromFile($ImagePath)
        $newPath = $ImagePath -replace "\.png$", ".jpg"

        $codec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq "image/jpeg" }
        $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
        $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, $Quality)

        $img.Save($newPath, $codec, $encoderParams)
        $img.Dispose()
        
        Write-Host "Converted: $ImagePath -> $newPath"
        Remove-Item $ImagePath
    }
    catch {
        Write-Error "Failed to convert $ImagePath : $_"
    }
}

Convert-PngToJpg -ImagePath "images/slider-main/bg1.png"
Convert-PngToJpg -ImagePath "images/slider-main/bg2.png"
Convert-PngToJpg -ImagePath "images/slider-main/bg3.png"
