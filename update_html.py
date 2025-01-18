import os
import pyperclip
import time
import re


def wait_for_clipboard_change(prompt_message):
    print(prompt_message)
    print("Copy the content and press Enter, or press 'd' to delete this image section...")
    user_input = input()  # Get user input
    if user_input.lower() == 'd':
        return "DELETE"  # Special return value to indicate deletion
    time.sleep(0.5)
    return pyperclip.paste()



def process_bold_text(text):
    if '<b>' in text.lower() and '</b>' in text.lower():
        return text
    if '**' in text:
        return text.replace('**', '<b>', 1).replace('**', '</b>', 1)
    return text

def remove_image_elements(content, index):
    # Remove thumbnail label
    label_pattern = f'<label for="pic{index}"[^>]*?>.*?</label>'
    content = re.sub(label_pattern, '', content, flags=re.DOTALL)
    
    # Remove main view div
    main_view_pattern = f'<div class="p{index} Main-View">.*?</div>'
    content = re.sub(main_view_pattern, '', content, flags=re.DOTALL)
    
    # Remove radio input
    input_pattern = f'<input type="radio" name="pic" id="pic{index}"[^>]*?>'
    content = re.sub(input_pattern, '', content)
    
    return content

def modify_html_file():
    if not os.path.exists('index.html'):
        print("Error: index.html not found in current directory!")
        return

    try:
        with open('index.html', 'r', encoding='utf-8') as file:
            content = file.read()

        # Get heading
        print("\n=== Step 1: Copy your heading ===")
        heading = wait_for_clipboard_change("Copy your heading text to the clipboard")

        # Get description points
        print("\n=== Step 2: Copy your description points ===")
        points = wait_for_clipboard_change("Copy ALL your description points to the clipboard")
        # Split the points by line breaks and process them
        point_list = [p.strip() for p in points.splitlines() if p.strip()]
        processed_points = [process_bold_text(point) for point in point_list]

        # Get image links
                      # Get image links
        image_links = []
        print("\n=== Step 3: Copy image links ===")
        for i in range(4):
            prompt = f"Copy image link #{i+1} to the clipboard (or press 'd' to delete this image section)"
            link = wait_for_clipboard_change(prompt)
            
            if link == "DELETE":
                print(f"🗑️ Deleting image section {i+1}")
                content = remove_image_elements(content, i+1)
            elif link.strip():
                image_links.append(link.strip())
                print(f"✓ Image {i+1} link received")
            else:
                print(f"⨯ Skipping image {i+1}")

        # Proceed with modifying the HTML content as before
        # ... [Rest of your content modifications] ...

        # Replace heading
        heading_pattern = r'(<div\s+style="font-family: &quot;Times New Roman&quot;[^>]*?>[\s\S]*?<font size="4">)([\s\S]*?)(</font>)'
        content = re.sub(heading_pattern, f'\\1\n{heading}\n\\3', content)

        # Replace description points
        ul_start = content.find('<ul>')
        if ul_start != -1:
            ul_end = content.find('</ul>', ul_start)
            li_content = '\n'.join([f'''
              <li>
                <font face="Arial" size="4">
                  {point}
                </font>
              </li>''' for point in processed_points])
            content = content[:ul_start + 4] + li_content + content[ul_end:]

        # Handle image links and remove unused image elements
        for i in range(1, 5):
            if i <= len(image_links):
                # Replace image links for existing images
                link = image_links[i-1]
                
                # Replace in thumbnail
                thumb_start = content.find(f'<label for="pic{i}"')
                if thumb_start != -1:
                    src_start = content.find('src="', thumb_start) + 5
                    src_end = content.find('"', src_start)
                    content = content[:src_start] + link + content[src_end:]

                # Replace in main view
                main_start = content.find(f'<div class="p{i} Main-View">')
                if main_start != -1:
                    src_start = content.find('src="', main_start) + 5
                    src_end = content.find('"', src_start)
                    content = content[:src_start] + link + content[src_end:]
            else:
                # Remove unused image elements
                content = remove_image_elements(content, i)

        # Write to new file
        with open('index1.html', 'w', encoding='utf-8') as file:
            file.write(content)

        print("\nSuccess! Created index1.html with all modifications.")
        print(f"Number of images processed: {len(image_links)}")
        print("Please check the new file to ensure all changes are correct.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    try:
        import pyperclip
    except ImportError:
        print("pyperclip module not found. Installing...")
        os.system('pip install pyperclip')
        import pyperclip
    
    modify_html_file()