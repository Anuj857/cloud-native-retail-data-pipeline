Write-Host "Cleaning old build..."

if (Test-Path build) {
    Remove-Item build -Recurse -Force
}

New-Item -ItemType Directory build | Out-Null

Write-Host "Installing Lambda dependencies..."

pip install -r requirements-lambda.txt -t build

Write-Host "Copying source..."

Copy-Item src\* build -Recurse -Force

Write-Host "Build folder ready."