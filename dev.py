import re
import os

SOURCE_DIR = "./doc/main"
TOC_DIR = "./doc/toc"
MAX_LEVEL = 3


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return text.replace(" ", "-")


def generate_toc(md_content, md_file_name, max_level=3):
    toc = []
    for line in md_content.splitlines():
        match = re.match(r"(#{1,6})\s+(.*)", line)
        if match:
            level = len(match.group(1))
            if level > max_level:
                continue

            title = match.group(2).strip()
            anchor = slugify(title)

            toc.append(
                f"{'  ' * (level - 1)}- " f"[{title}](../main/{md_file_name}#{anchor})"
            )

    return "\n".join(toc)


def create_toc_file(md_file_path):
    with open(md_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    file_name = os.path.basename(md_file_path)

    toc = generate_toc(content, file_name)

    base_name = os.path.splitext(file_name)[0]

    os.makedirs(TOC_DIR, exist_ok=True)
    toc_file_path = os.path.join(TOC_DIR, f"{base_name}_toc.md")

    toc_content = f'<link rel="stylesheet" href="https://devnamdev2003.github.io/md/static/style.css"> \n\n# Table of Contents\n\n{toc}\n'

    with open(toc_file_path, "w", encoding="utf-8") as f:
        f.write(toc_content)

    print(f"✅ TOC created: {toc_file_path}")


if __name__ == "__main__":

    if not os.path.isdir(SOURCE_DIR):
        raise Exception(f"Source directory not found: {SOURCE_DIR}")

    md_files = [
        os.path.join(SOURCE_DIR, f)
        for f in os.listdir(SOURCE_DIR)
        if f.lower().endswith(".md")
    ]

    if not md_files:
        print("⚠️ No markdown files found")
    else:
        for md_file in md_files:
            create_toc_file(md_file)
