# This is Day 59 project : Markdown to HTML Converter

import os
import webbrowser
from pathlib import Path

import markdown
from flask import Flask, render_template_string

app = Flask(__name__)

preview_content = ""
preview_css = ""
preview_title = "Markdown Preview"

def read_markdown_file(file_path):
    """Read Markdown content from a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
def read_css_file(css_path):
    """Read CSS content from a file."""
    with open(css_path, "r", encoding="utf-8") as file:
        return file.read()
    
def convert_markdown_to_html(markdown_text):
    """Convert Markdown text into HTML."""
    return markdown.markdown(markdown_text, extensions=["tables", "fenced_code", "nl2br"])

def wrap_in_html_template(content, css_content="", title="Markdown to HTML"):
    """Wrap converted Markdown HTML inside a complete HTML document."""
    html_template = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                max-width: 900px;
                margin: 40px auto;
                padding: 0 20px;
                color: #333;
            }}
            h1, h2, h3 {{
                color: #222;
            }}
            a {{
                color: #1a73e8;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            img {{
                max-width: 100%;
                height: auto;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid #ccc;
                padding: 10px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            pre {{
                background-color: #f4f4f4;
                padding: 15px;
                overflow-x: auto;
                border-radius: 6px;
            }}
            code {{
                font-family: Consolas, monospace;
            }}
            blockquote {{
                border-left: 4px solid #ccc;
                padding-left: 15px;
                color: #666;
            }}
            {css_content}
        </style>
    </head>
    <body>
        {content}
    </body>
    </html>
    """
    return html_template

def write_html_file(html_content, output_path):
    """Write generated HTML to a file."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html_content)
        
def convert_single_file(markdown_path, output_path, css_path=None):
    """Convert one Markdown file into an HTML file."""
    markdown_path = Path(markdown_path)
    output_path = Path(output_path)

    markdown_text = read_markdown_file(markdown_path)
    html_content = convert_markdown_to_html(markdown_text)
    css_content = ""

    if css_path:
        css_content = read_css_file(css_path)
    title = markdown_path.stem.replace("_", " ").title()

    final_html = wrap_in_html_template(html_content, css_content, title)
    write_html_file(final_html, output_path)
    return output_path

def convert_folder(input_folder, output_folder, css_path=None):
    """Convert all Markdown files inside a folder."""
    input_folder = Path(input_folder)
    output_folder = Path(output_folder)

    if not input_folder.exists():
        raise FileNotFoundError("Input folder does not exist.")

    if not input_folder.is_dir():
        raise NotADirectoryError("Input path is not a folder.")

    markdown_files = list(input_folder.rglob("*.md"))
    markdown_files += list(input_folder.rglob("*.markdown"))

    if not markdown_files:
        print("\nNo Markdown files were found.")
        return []

    converted_files = []
    print(f"\nFound {len(markdown_files)} Markdown file(s).")
    print("-" * 50)

    for markdown_file in markdown_files:
        relative_path = markdown_file.relative_to(input_folder)
        output_file = output_folder / relative_path.with_suffix(".html")

        try:
            convert_single_file(markdown_file, output_file, css_path)
            converted_files.append(output_file)
            print(f"✓ {markdown_file} → {output_file}")
        except Exception as error:
            print(f"✗ Failed: {markdown_file}")
            print(f"  Error: {error}")
    print("-" * 50)
    print(f"Successfully converted: {len(converted_files)} file(s)")
    return converted_files

@app.route("/")
def preview():
    """Display the generated Markdown as a webpage."""
    return render_template_string(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{{ title }}</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    max-width: 900px;
                    margin: 40px auto;
                    padding: 0 20px;
                    color: #333;
                }
                h1, h2, h3 {
                    color: #222;
                }
                a {
                    color: #1a73e8;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
                img {
                    max-width: 100%;
                    height: auto;
                }
                table {
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }
                th, td {
                    border: 1px solid #ccc;
                    padding: 10px;
                    text-align: left;
                }
                th {
                    background-color: #f2f2f2;
                }
                pre {
                    background-color: #f4f4f4;
                    padding: 15px;
                    overflow-x: auto;
                    border-radius: 6px;
                }
                blockquote {
                    border-left: 4px solid #ccc;
                    padding-left: 15px;
                    color: #666;
                }
                {{ css|safe }}
            </style>
        </head>
        <body>
            {{ content|safe }}
            <script>
                setTimeout(function() {
                    location.reload();
                }, 3000);
            </script>
        </body>
        </html>
        """, content=preview_content, css=preview_css, title=preview_title)

def start_preview(html_content, css_content="", title="Markdown Preview"):
    """Start Flask preview server."""
    global preview_content
    global preview_css
    global preview_title

    preview_content = html_content
    preview_css = css_content
    preview_title = title

    print("\nStarting Flask live preview...")
    print("Open http://127.0.0.1:5000 in your browser.")
    print("Press CTRL+C in the terminal to stop the preview.\n")

    webbrowser.open("http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=False)
        
def get_css_file():
    """Ask the user whether they want to use a custom CSS file."""
    use_css = input("\nDo you want to use a custom CSS file? (y/n): ").strip().lower()

    if use_css != "y":
        return None
    css_path = input("Enter CSS file path: ").strip()

    if not os.path.isfile(css_path):
        print("CSS file not found. Continuing without custom CSS.")
        return None
    return css_path

def main():
    print("=" * 55)
    print("       MARKDOWN TO HTML CONVERTER")
    print("=" * 55)

    while True:
        print("\nChoose an option:")
        print("1. Convert a Markdown file")
        print("2. Convert all Markdown files in a folder")
        print("3. Live preview")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            markdown_file = input("\nEnter Markdown file path: ").strip()
            if not os.path.isfile(markdown_file):
                print("✗ Markdown file not found.")
                continue

            output_file = input("Enter output HTML file path: ").strip()
            css_file = get_css_file()

            try:
                output_path = convert_single_file(markdown_file, output_file, css_file)
                print("\n✓ Conversion successful!")
                print(f"✓ HTML saved to: {output_path}")
            except Exception as error:
                print(f"\n✗ Conversion failed: {error}")
                
        elif choice == "2":
            input_folder = input("\nEnter Markdown folder path: ").strip()
            output_folder = input("Enter output folder path: ").strip()
            css_file = get_css_file()

            try:
                convert_folder(input_folder, output_folder, css_file)
            except Exception as error:
                print(f"\n✗ Bulk conversion failed: {error}")

        elif choice == "3":
            markdown_file = input("\nEnter Markdown file path for preview: ").strip()
            if not os.path.isfile(markdown_file):
                print("✗ Markdown file not found.")
                continue

            css_file = get_css_file()

            try:
                markdown_text = read_markdown_file(markdown_file)
                html_content = convert_markdown_to_html(markdown_text)
                css_content = ""

                if css_file:
                    css_content = read_css_file(css_file)

                title = Path(markdown_file).stem.replace("_", " ").title()
                start_preview(html_content, css_content, title)
            except Exception as error:
                print(f"\n✗ Preview failed: {error}")
                
        elif choice == "4":
            print("\nThank you for using Markdown to HTML Converter!")
            break
        else:
            print("\n✗ Invalid choice. Please select 1-4.")
                
if __name__ == "__main__":
    main()
    
# Done