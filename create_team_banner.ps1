# PowerShell script to create team banner from individual photos
Add-Type -AssemblyName System.Drawing

# Create banner dimensions
$bannerWidth = 1920
$bannerHeight = 400

# Create new bitmap for banner
$banner = New-Object System.Drawing.Bitmap($bannerWidth, $bannerHeight)
$graphics = [System.Drawing.Graphics]::FromImage($banner)
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic

# Create dark gradient background
$brush = New-Object System.Drawing.Drawing2D.LinearGradientBrush(
    (New-Object System.Drawing.Point(0, 0)),
    (New-Object System.Drawing.Point($bannerWidth, $bannerHeight)),
    [System.Drawing.Color]::FromArgb(255, 30, 30, 40),
    [System.Drawing.Color]::FromArgb(255, 50, 50, 60)
)
$graphics.FillRectangle($brush, 0, 0, $bannerWidth, $bannerHeight)

# Load team images
$teamPath = "c:\Users\LUMATO TECH\Pictures\Briva-1\images\team\"
$images = @(
    "Alex S Bashire.jpg",
    "Vashty J Nyembera.jpg",
    "Dr. Kolipaka Venu.jpg",
    "SRIRAMA GOPAL YELLAPRAGADA.jpg",
    "RAJU BADUGU.jpg",
    "JACKLINE SAYI KIDENDEI.jpg"
)

# Calculate spacing
$photoSize = 300
$spacing = ($bannerWidth - ($images.Count * $photoSize)) / ($images.Count + 1)
$yPosition = ($bannerHeight - $photoSize) / 2

# Add each team member photo
$xPosition = $spacing
foreach ($imgFile in $images) {
    $imgPath = Join-Path $teamPath $imgFile
    if (Test-Path $imgPath) {
        $teamImg = [System.Drawing.Image]::FromFile($imgPath)
        
        # Create circular clip path
        $path = New-Object System.Drawing.Drawing2D.GraphicsPath
        $rect = New-Object System.Drawing.Rectangle($xPosition, $yPosition, $photoSize, $photoSize)
        $path.AddEllipse($rect)
        
        # Draw with circular clip
        $graphics.SetClip($path)
        $graphics.DrawImage($teamImg, $xPosition, $yPosition, $photoSize, $photoSize)
        $graphics.ResetClip()
        
        # Add border
        $pen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(200, 255, 255, 255), 4)
        $graphics.DrawEllipse($pen, $rect)
        
        $teamImg.Dispose()
        $xPosition += $photoSize + $spacing
    }
}

# Add semi-transparent overlay for text readability
$overlayBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(120, 0, 0, 0))
$graphics.FillRectangle($overlayBrush, 0, 0, $bannerWidth, $bannerHeight)

# Save banner
$outputPath = "c:\Users\LUMATO TECH\Pictures\Briva-1\images\banner\team_banner_composite.jpg"
$banner.Save($outputPath, [System.Drawing.Imaging.ImageFormat]::Jpeg)

# Cleanup
$graphics.Dispose()
$banner.Dispose()
$brush.Dispose()

Write-Output "Team banner created successfully at: $outputPath"
