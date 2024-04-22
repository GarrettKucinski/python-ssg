from pathlib import Path
from markdown_to_html import markdown_to_html

def extract_page_title(markdown = "markdown not provided"):
  blocks = markdown.strip().split("\n")

  for block in blocks:
    if block.startswith("# "):
      return block.lstrip("# ")

  raise ValueError("h1 does not exist or is not the first element. Please add or relocate the h1 to the to of the page.")

def generate_html_content(markdown, template):
  page_title = extract_page_title(markdown)
  page_content = markdown_to_html(markdown)

  html_document = template.replace("{{ Title }}", page_title)
  html_document = html_document.replace("{{ Content }}", page_content.to_html())

  return html_document

def write_parsed_file(from_path, template, dest_path):
  for path in Path(from_path).iterdir():
    output_path = Path(dest_path) / path.name

    if not output_path.parent.exists() and not output_path.parent.is_file():
      print("directory not found, creating...", output_path.parent)
      output_path.parent.mkdir(parents=True)

    if path.is_file():
      print('Opening file at:', path)
      markdown = Path(path)
      markdown_content = markdown.read_text(encoding="utf-8")

      html_document = generate_html_content(markdown_content, template)

      print("writing path", output_path.with_suffix(".html"))

      output_path.with_suffix(".html").write_text(html_document)
    else:
      print("Recursively parsing files in:", path)
      write_parsed_file(path, template, output_path)

def generate_page(from_path, template_path, dest_path):
  template_file = open(template_path)
  template = template_file.read()
  template_file.close()

  write_parsed_file(from_path, template, dest_path)
