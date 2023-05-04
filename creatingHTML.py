import markdown

# Set the paths for the input and output files
input_path = "pyBrain/README.md"
output_path = "README.html"

# Read the input Markdown file
with open(input_path, "r") as input_file:
    md_text = input_file.read()

# Convert the Markdown to HTML
html = markdown.markdown(md_text, extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc'])


# Write the output HTML file
with open(output_path, "w") as output_file:
    output_file.write(html)

print(f"Conversion complete. HTML saved to {output_path}")