import os
from blocks_markdown import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("no title found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = open(from_path)
    markdown = markdown_file.read()
    markdown_file.close()

    # print(markdown)
    template_file = open(template_path)
    template = template_file.read()
    template_file.close()

    markdown_html = markdown_to_html_node(markdown).to_html()
    page_title = extract_title(markdown)

    page = template.replace("{{ Title }}", page_title).replace(
        "{{ Content }}", markdown_html
    )

    destination_file = open(dest_path, mode="w")
    destination_file.write(page)
    destination_file.close()


def generate_pages_rec(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename.replace(".md", ".html"))
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_rec(from_path, template_path, dest_path)
