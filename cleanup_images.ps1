
# 1. Gather all image references from HTML files
$htmlFiles = Get-ChildItem -Path "c:\Users\LUMATO TECH\Pictures\Briva-1" -Filter "*.html"
$usedImages = @()

foreach ($file in $htmlFiles) {
    $content = Get-Content $file.FullName
    # Regex to find src="images/..." or url('images/...')
    $matches = [regex]::Matches($content, 'images/[\w\-\./]+\.(jpg|png|gif|jpeg|svg)')
    foreach ($match in $matches) {
        $usedImages += $match.Value.Replace('/', '\')
    }
    # Also check for inline styles like background-image:url(images/...)
    $matchesBg = [regex]::Matches($content, 'url\((?:["'']?)(images/[\w\-\./]+\.(jpg|png|gif|jpeg|svg))(?:["'']?)\)')
    foreach ($match in $matchesBg) {
        $usedImages += $match.Groups[1].Value.Replace('/', '\')
    }
}

# 2. Add images found in CSS (hardcoded based on my grep)
$usedImages += "images\preload.gif"
$usedImages += "images\crossword.png"
$usedImages += "images\parallax2.jpg"

# 3. Add images that might be dynamically loaded or essential
$usedImages += "images\favicon.png"
$usedImages += "images\marker.png" # Google maps marker often used

# Normalize paths
$usedImages = $usedImages | ForEach-Object { "c:\Users\LUMATO TECH\Pictures\Briva-1\$_" } | Select-Object -Unique

# 4. List all actual images
$allImages = Get-ChildItem -Path "c:\Users\LUMATO TECH\Pictures\Briva-1\images" -Recurse | Where-Object { $_.Extension -match "\.(jpg|png|gif|jpeg|svg)$" }

# 5. Delete unused
foreach ($image in $allImages) {
    if ($usedImages -notcontains $image.FullName) {
        Write-Host "Deleting unused image: $($image.FullName)"
        Remove-Item $image.FullName -Force
    }
    else {
        Write-Host "Keeping: $($image.FullName)"
    }
}
