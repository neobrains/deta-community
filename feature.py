import re
import json


def parse():
    with open("./feature.json") as f:
        json_data = json.load(f)
    with open('./docs/feature-boiler.md', 'rb') as f:
        pattern = re.compile('<!--start (?:.*?)-->((.|\n)*?)<!--end-->')
        name = re.compile('<!--start (.*?)-->')
        chunk = f.read().decode('utf-8')
        matches = pattern.finditer(chunk)
        for match in matches:
            full_block = match.group(0)
            matched_content = match.group(1)
            raw_project_name = name.search(full_block).group(1)
            project_name = raw_project_name.replace("-", " ").title()
            project = json_data.get(raw_project_name)
            if project:
                about = project['about'].replace('\\n', f'  \n\t')
                details = project['details'].replace('\\n', f'  \n\t')
                preview = project['preview']
                content = (
                    f"<!--start {raw_project_name}-->"
                    f"""\n=== "About {project_name}"\n\t{about}"""
                    f"""\n=== "Project Details"\n\t{details}"""
                    )
                if preview == 1:
                    image_uri = project['image_uri']
                    content += f"""\n=== "Preview"\n\t![{project_name}]({image_uri})\n<!--end-->"""
                else:
                    content += "\n<!--end-->"
                chunk = chunk.replace(full_block, content)
                
    with open('./docs/featured.md', 'wb') as f:
        f.write(chunk.encode('utf-8'))

if __name__ == '__main__':
    parse()
    print("Done file editing")
