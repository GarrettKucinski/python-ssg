import os
from markdown_to_html import markdown_to_html

def extract_page_title(markdown = "markdown not provided"):
  blocks = markdown.strip().split("\n")

  for block in blocks:
    if block.startswith("# "):
      return block.lstrip("# ")

  raise ValueError("h1 does not exist or is not the first element. Please add or relocate the h1 to the to of the page.")

def generate_page(from_path, template_path, dest_path):
  dir_to_write = os.path.dirname(dest_path)

  with (
    open(template_path, "r") as template,
    open(from_path, "r") as markdown,
    open(dest_path, "w") as writer
  ):
    markdown_content = markdown.read()
    page_title = extract_page_title(markdown_content)
    page_content = markdown_to_html(markdown_content)

    html_document = template.read().replace("{{ Title }}", page_title)
    html_document = html_document.replace("{{ Content }}", page_content.to_html())

    if not os.path.exists(dir_to_write):
      os.makedirs(dir_to_write)

    writer.write(html_document)
