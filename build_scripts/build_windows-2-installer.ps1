# $env:path should contain a path to editbin.exe and signtool.exe

$ErrorActionPreference = "Stop"

mkdir build_scripts\win_build

git status
git submodule

if (-not (Test-Path env:SSDCOIN_INSTALLER_VERSION)) {
  $env:SSDCOIN_INSTALLER_VERSION = '0.0.0'
  Write-Output "WARNING: No environment variable SSDCOIN_INSTALLER_VERSION set. Using 0.0.0"
}
Write-Output "SSDCoin Version is: $env:SSDCOIN_INSTALLER_VERSION"
Write-Output "   ---"

Write-Output "   ---"
Write-Output "Use pyinstaller to create ssd .exe's"
Write-Output "   ---"
$SPEC_FILE = (py -c 'import sys; from pathlib import Path; path = Path(sys.argv[1]); print(path.absolute().as_posix())' "pyinstaller.spec")
pyinstaller --log-level INFO $SPEC_FILE

Write-Output "   ---"
Write-Output "Creating a directory of licenses from pip and npm packages"
Write-Output "   ---"
bash ./build_win_license_dir.sh

Write-Output "   ---"
Write-Output "Copy ssdcoin executables to ssdcoin-blockchain-gui\"
Write-Output "   ---"
Copy-Item "dist\daemon" -Destination "..\ssdcoin-blockchain-gui\packages\gui\" -Recurse

Write-Output "   ---"
Write-Output "Setup npm packager"
Write-Output "   ---"
Set-Location -Path ".\npm_windows" -PassThru
npm ci

Set-Location -Path "..\..\" -PassThru

Write-Output "   ---"
Write-Output "Prepare Electron packager"
Write-Output "   ---"
$Env:NODE_OPTIONS = "--max-old-space-size=3000"

# Change to the GUI directory
Set-Location -Path "ssdcoin-blockchain-gui\packages\gui" -PassThru

Write-Output "   ---"
Write-Output "Increase the stack for ssdcoin command for (ssd plots create) chiapos limitations"
# editbin.exe needs to be in the path
editbin.exe /STACK:8000000 daemon\ssd.exe
Write-Output "   ---"

$packageVersion = "$env:SSDCOIN_INSTALLER_VERSION"
$packageName = "SSDCoin-$packageVersion"

Write-Output "packageName is $packageName"

Write-Output "   ---"
Write-Output "fix version in package.json"
choco install jq
cp package.json package.json.orig
jq --arg VER "$env:SSDCOIN_INSTALLER_VERSION" '.version=$VER' package.json > temp.json
rm package.json
mv temp.json package.json
Write-Output "   ---"

Write-Output "   ---"
Write-Output "electron-builder create package directory"
npx electron-builder build --win --x64 --config.productName="SSDCoin" --dir
Get-ChildItem dist\win-unpacked\resources
Write-Output "   ---"

If ($env:HAS_SIGNING_SECRET) {
   Write-Output "   ---"
   Write-Output "Sign all EXEs"
   Get-ChildItem ".\dist\win-unpacked" -Recurse | Where-Object { $_.Extension -eq ".exe" } | ForEach-Object {
      $exePath = $_.FullName
      Write-Output "Signing $exePath"
      signtool.exe sign /sha1 $env:SM_CODE_SIGNING_CERT_SHA1_HASH /tr http://timestamp.digicert.com /td SHA256 /fd SHA256 $exePath
      Write-Output "Verify signature"
      signtool.exe verify /v /pa $exePath
  }
}    Else    {
   Write-Output "Skipping verify signatures - no authorization to install certificates"
}

Write-Output "   ---"
Write-Output "electron-builder create installer"
npx electron-builder build --win --x64 --config.productName="SSDCoin" --pd ".\dist\win-unpacked"
Write-Output "   ---"

If ($env:HAS_SIGNING_SECRET) {
   Write-Output "   ---"
   Write-Output "Sign Final Installer App"
   signtool.exe sign /sha1 $env:SM_CODE_SIGNING_CERT_SHA1_HASH /tr http://timestamp.digicert.com /td SHA256 /fd SHA256 .\dist\SSDCoinSetup-$packageVersion.exe
   Write-Output "   ---"
   Write-Output "Verify signature"
   Write-Output "   ---"
   signtool.exe verify /v /pa .\dist\SSDCoinSetup-$packageVersion.exe
}   Else    {
   Write-Output "Skipping verify signatures - no authorization to install certificates"
}

Write-Output "   ---"
Write-Output "Moving final installers to expected location"
Write-Output "   ---"
Copy-Item ".\dist\win-unpacked" -Destination "$env:GITHUB_WORKSPACE\ssdcoin-blockchain-gui\SSDCoin-win32-x64" -Recurse
mkdir "$env:GITHUB_WORKSPACE\ssdcoin-blockchain-gui\release-builds\windows-installer" -ea 0
Copy-Item ".\dist\SSDCoinSetup-$packageVersion.exe" -Destination "$env:GITHUB_WORKSPACE\ssdcoin-blockchain-gui\release-builds\windows-installer"

Write-Output "   ---"
Write-Output "Windows Installer complete"
Write-Output "   ---"
