python generate_all_content.py
python update_html.py
Copy-Item -Path "index.html" -Destination "C:\Users\ankes\OneDrive\Desktop\svps lab book.html" -Force
Copy-Item -Path "index.html" -Destination "C:\Users\ankes\Downloads\svps lab book.html" -Force
Write-Host "Success! Local build completed and files copied to Desktop/Downloads. No deployment made."