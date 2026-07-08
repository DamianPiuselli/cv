#!/usr/bin/env python3
import os
import subprocess
import sys
import shutil

def find_chrome():
    """Finds a Chrome or Chromium executable on the system."""
    # Common executable names in PATH
    executables = [
        "google-chrome-stable",
        "google-chrome",
        "chromium-browser",
        "chromium",
        "chrome"
    ]
    
    # Check PATH first
    for name in executables:
        path = shutil.which(name)
        if path:
            return path
            
    # Platform-specific default paths
    if sys.platform == "darwin":  # macOS
        mac_paths = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Chromium.app/Contents/MacOS/Chromium"
        ]
        for path in mac_paths:
            if os.path.exists(path):
                return path
    elif sys.platform == "win32":  # Windows
        win_paths = [
            os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
            os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
            os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe")
        ]
        for path in win_paths:
            if os.path.exists(path):
                return path
                
    return None

def main():
    chrome_path = find_chrome()
    if not chrome_path:
        print("Error: Chrome/Chromium executable not found. Please install Google Chrome or Chromium.", file=sys.stderr)
        sys.exit(1)
        
    print(f"Using Chrome executable: {chrome_path}")
    
    # Define tasks: (input_html, output_pdf)
    tasks = [
        ("index.html", "cv_editorial.pdf"),
        ("cv_minimalist.html", "cv_minimalist.pdf")
    ]
    
    success = True
    for html_file, pdf_file in tasks:
        if not os.path.exists(html_file):
            print(f"Warning: {html_file} not found, skipping.", file=sys.stderr)
            continue
            
        print(f"Generating {pdf_file} from {html_file}...")
        
        cmd = [
            chrome_path,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_file}",
            html_file
        ]
        
        try:
            # Run the command with a 30 second timeout
            result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
            print(f"Successfully generated {pdf_file} ({os.path.getsize(pdf_file)} bytes).")
        except subprocess.CalledProcessError as e:
            print(f"Error generating {pdf_file}: {e.stderr.decode('utf-8', errors='ignore')}", file=sys.stderr)
            success = False
        except subprocess.TimeoutExpired:
            print(f"Error: Timeout expired while generating {pdf_file}", file=sys.stderr)
            success = False
            
    if not success:
        sys.exit(1)
        
    print("PDF generation completed successfully!")

if __name__ == "__main__":
    main()
