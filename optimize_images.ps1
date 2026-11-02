
Add-Type -AssemblyName System.Drawing

function Resize-Image {
    param (
        [string]$ImagePath,
        [int]$MaxWidth,
        [int]$MaxHeight,
        [int]$Quality = 75
    )

    if (-not (Test-Path $ImagePath)) {
        Write-Host "File not found: $ImagePath"
        return
    }

    try {
        $img = [System.Drawing.Image]::FromFile($ImagePath)
        
        # Calculate new dimensions
        $ratioX = $MaxWidth / $img.Width
        $ratioY = $MaxHeight / $img.Height
        $ratio = [Math]::Min($ratioX, $ratioY)
        
        # Only resize if the image is larger than the target
        if ($ratio -ge 1) {
            $img.Dispose()
            Write-Host "Skipping $ImagePath (already small enough)"
            return
        }

        $newWidth = [int]($img.Width * $ratio)
        $newHeight = [int]($img.Height * $ratio)

        $newImg = new-object System.Drawing.Bitmap $newWidth, $newHeight
        $graph = [System.Drawing.Graphics]::FromImage($newImg)
        $graph.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
        $graph.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $graph.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
        $graph.DrawImage($img, 0, 0, $newWidth, $newHeight)
        
        $img.Dispose() # Release the original file handle

        # Save with compression
        $codec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq "image/jpeg" }
        $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
        $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, $Quality)

        # Save to a temporary file first
        $tempPath = "$ImagePath.tmp.jpg"
        if ($ImagePath -match "\.png$") {
            # If it was a PNG, we might want to keep it as PNG or convert to JPG. 
            # For photos (news, projects), JPG is better. For logos/icons, PNG is better.
            # Let's stick to the original format extension but compress if possible.
            # Actually, System.Drawing doesn't support easy PNG compression control like JPG.
            # So for PNGs, we'll just resize.
            $newImg.Save($ImagePath, [System.Drawing.Imaging.ImageFormat]::Png)
        }
        else {
            $newImg.Save($ImagePath, $codec, $encoderParams)
        }
        
        $newImg.Dispose()
        $graph.Dispose()
        
        Write-Host "Resized: $ImagePath"
    }
    catch {
        Write-Error "Failed to resize $ImagePath : $_"
    }
}

# Resize News Images
Get-ChildItem "images/news/*.jpg" | ForEach-Object { Resize-Image -ImagePath $_.FullName -MaxWidth 800 -MaxHeight 600 }

# Resize Service Center Image
Resize-Image -ImagePath "images/services/service-center.jpg" -MaxWidth 800 -MaxHeight 800

# Resize Project Images
Get-ChildItem "images/projects/*" | Where-Object { $_.Extension -match "jpg|png" } | ForEach-Object { Resize-Image -ImagePath $_.FullName -MaxWidth 800 -MaxHeight 600 }

# Resize Favicon (Special case, needs to be small)
Resize-Image -ImagePath "images/favicon.png" -MaxWidth 32 -MaxHeight 32

