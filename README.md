# Ebay EasyLister Pro Automator


 Overview
Transform your eBay listing workflow with SwiftLister Pro, a powerful Python-based automation tool that streamlines the process of updating eBay HTML listing templates. Built for sellers who value efficiency and professional presentation.
 Key Features
 Smart Content Management
One-Click Heading Updates: Instantly modify product titles
Intelligent Description Formatting:
Automatic bullet point formatting
Smart bold text processing (**text** → <b>text</b>)
Multi-line support
 Advanced Image Handler
Multi-Image Support: Manage up to 4 product images
Flexible Operations:
Quick image addition via clipboard
Instant image section deletion with 'd' key
Smart skip functionality
Auto-Cleanup: Removes unused image elements automatically
 Technical Requirements
Python 3.x
pyperclip module (auto-installs if missing)
 Quick Start Guide
Installation
bash


# Clone the repository
git clone https://github.com/babar0081/Ebay-EasyLister-Pro-Automator.git

# Navigate to directory
cd SwiftLister-Pro

# Run the script
python update_html.py
Template Setup
Place your index.html template in the script directory
Ensure template contains required HTML structure
Run script and follow interactive prompts
 Usage Guide
1. Heading Configuration
javascript


=== Step 1: Copy your heading ===
• Copy heading text
• Press Enter
2. Description Setup
javascript


=== Step 2: Copy your description points ===
• Paste description points
• Use **text** for bold formatting
• Press Enter
3. Image Management
javascript


=== Step 3: Copy image links ===
• Press 'd' → Delete image section
• Paste URL → Add image
• Press Enter → Skip section
🎉 Output
Generates index1.html with all modifications
Maintains original template integrity
Automatically optimizes image sections
🤝 Contributing
We welcome contributions! Feel free to:
Submit bug reports
Propose new features
Create pull requests
Share feedback