# Get the directory of the current script
$ScriptDir = Split-Path -Parent -Path $MyInvocation.MyCommand.Definition

# Function to check if a command exists
function Test-CommandExists {
    param (
        [string]$Command
    )
    $exists = $null -ne (Get-Command $Command -ErrorAction SilentlyContinue)
    return $exists
}

# Check if pip is installed
if (-not (Test-CommandExists 'pip')) {
    Write-Host "pip could not be found"
    exit 1
}

# Check if pytest is installed, if not, install it
if (-not (Test-CommandExists 'pytest')) {
    pip install pytest
}

# Double check if pytest is installed (in case pip install failed)
if (-not (Test-CommandExists 'pytest')) {
    Write-Host "pytest could not be found or installed"
    exit 1
}

# Run pytest
pytest -v $ScriptDir
