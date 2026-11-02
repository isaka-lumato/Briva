# Decap CMS Quick Start Script
# This script helps you convert your projects and prepare for Decap CMS

Write-Host ""
Write-Host "==================================" -ForegroundColor Cyan
Write-Host "  Briva Decap CMS Setup Helper" -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

# Check if Node.js is installed
Write-Host "[1/4] Checking Node.js installation..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version
    Write-Host "✅ Node.js is installed: $nodeVersion" -ForegroundColor Green
}
catch {
    Write-Host "❌ Node.js is not installed!" -ForegroundColor Red
    Write-Host "Please install Node.js from: https://nodejs.org/" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit
}

# Convert projects.json
Write-Host "`n[2/4] Converting projects.json to Decap CMS format..." -ForegroundColor Yellow
try {
    node admin/convert-projects.js
    Write-Host "✅ Projects converted successfully!" -ForegroundColor Green
}
catch {
    Write-Host "❌ Error converting projects: $_" -ForegroundColor Red
    Write-Host "You can do this manually later." -ForegroundColor Yellow
}

# Rename admin/decap-index.html to admin/index.html
Write-Host "`n[3/4] Setting up admin interface..." -ForegroundColor Yellow
if (Test-Path "admin/decap-index.html") {
    if (Test-Path "admin/index.html") {
        $backup = "admin/index-php-backup.html"
        Write-Host "Backing up existing admin/index.html to $backup..." -ForegroundColor Yellow
        Move-Item "admin/index.html" $backup -Force
    }
    Rename-Item "admin/decap-index.html" "index.html"
    Write-Host "✅ Admin interface configured!" -ForegroundColor Green
}
else {
    Write-Host "⚠️  admin/decap-index.html not found. Skipping..." -ForegroundColor Yellow
}

# Display next steps
Write-Host ""
Write-Host "[4/4] Setup complete! Next steps:" -ForegroundColor Yellow
Write-Host ""
Write-Host "NEXT STEPS:" -ForegroundColor Cyan
Write-Host "1. Go to Netlify Dashboard -> Your Site -> Identity" -ForegroundColor White
Write-Host "2. Click 'Enable Identity'" -ForegroundColor White
Write-Host "3. Under Services -> Enable 'Git Gateway'" -ForegroundColor White
Write-Host "4. Invite yourself as an admin user" -ForegroundColor White
Write-Host "5. Push these changes to GitHub:" -ForegroundColor White
Write-Host "   git add ." -ForegroundColor Gray
Write-Host "   git commit -m 'Add Decap CMS'" -ForegroundColor Gray
Write-Host "   git push origin main" -ForegroundColor Gray
Write-Host "6. Visit: https://your-site.netlify.app/admin/" -ForegroundColor White
Write-Host ""
Write-Host "For detailed instructions, see: DECAP_CMS_SETUP.md" -ForegroundColor Cyan
Write-Host ""
Write-Host "All done! Happy editing!" -ForegroundColor Green
Write-Host ""

Read-Host "Press Enter to exit"
