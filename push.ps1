python generate_all_content.py
python update_html.py
& "C:\Program Files\Git\cmd\git.exe" add .
$msg = $args[0]
if (-not $msg) { $msg = "Updates to curriculum contents" }
& "C:\Program Files\Git\cmd\git.exe" commit -m $msg
& "C:\Program Files\Git\cmd\git.exe" push origin main
Write-Host "Success! Changes pushed to GitHub and automatically deploying to Netlify!"