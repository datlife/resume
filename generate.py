import yaml
from jinja2 import Environment, FileSystemLoader
import os
import shutil

def generate():
    with open('data.yaml', 'r') as f:
        data = yaml.safe_load(f)

    # Ensure docs directory exists
    os.makedirs('docs', exist_ok=True)
    
    # Copy assets to docs/assets for GitHub Pages
    if os.path.exists('assets'):
        shutil.copytree('assets', 'docs/assets', dirs_exist_ok=True)
    
    # Copy static files to docs
    for static_file in ['style.css']:
        if os.path.exists(static_file):
            shutil.copy(static_file, 'docs/')

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')
    
    rendered = template.render(
        profile=data['profile'],
        header=data['header'],
        sections=data['sections']
    )

    with open('docs/index.html', 'w') as f:
        f.write(rendered)

    print('Generated docs/index.html with assets')

if __name__ == '__main__':
    generate()
