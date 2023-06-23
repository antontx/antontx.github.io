import markdown2

def main():
    paths = [(r"md\paper_deep.md", r"paper_deep.html")]

    md_to_html(paths)
    print("Done!")


def md_to_html(paths):
    for md_file, html_file in paths:
        with open(md_file, 'r', encoding='utf-8') as file:
            md_content = file.read()

        html_content = markdown2.markdown(md_content)
        full_html = f'''<!DOCTYPE html>
            <html>
                <head>
                    <title>Deep Learning</title>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" type="text/css" href="style.css">
                    <link href="https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;700&family=Spline+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
                </head>
                <body>
                    <main>
                    {html_content}
                    </main>
                    <footer>
                        <p>&copy; 2023 Anton K.  All rights reserved.</p>
                    </footer>
                </body>

            </html>'''
        
        with open(html_file, 'w', encoding='utf-8') as file:
            file.write(full_html)


if __name__ == "__main__":
    main()