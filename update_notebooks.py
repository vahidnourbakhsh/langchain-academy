#!/usr/bin/env python3
"""Update all notebooks to use Ollama instead of OpenAI."""

import json
import os
from pathlib import Path

def update_notebook(notebook_path):
    """Update a single notebook to use Ollama instead of OpenAI."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    changed = False
    
    for cell in notebook.get('cells', []):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Remove OPENAI_API_KEY prompts
            if '_set_env("OPENAI_API_KEY")' in source or "_set_env('OPENAI_API_KEY')" in source:
                cell['source'] = ['# Ollama - no API key required\n']
                changed = True
            
            # Replace ChatOpenAI imports
            elif 'from langchain_openai import ChatOpenAI' in source:
                new_source = source.replace(
                    'from langchain_openai import ChatOpenAI',
                    'from langchain_ollama import ChatOllama'
                )
                cell['source'] = [new_source]
                changed = True
            
            # Replace ChatOpenAI instantiation
            elif 'ChatOpenAI(' in source:
                new_source = source.replace('ChatOpenAI(', 'ChatOllama(')
                new_source = new_source.replace('model="gpt-4o"', 'model="llama3:latest"')
                new_source = new_source.replace("model='gpt-4o'", "model='llama3:latest'")
                new_source = new_source.replace('gpt-4o', 'llama3:latest')
                cell['source'] = [new_source]
                changed = True
        
        elif cell['cell_type'] == 'markdown':
            source = ''.join(cell['source'])
            
            # Update markdown mentioning OpenAI API key
            if 'OPENAI_API_KEY' in source and 'check' in source.lower():
                new_source = source.replace(
                    "Let's check that your `OPENAI_API_KEY` is set and, if not, you will be asked to enter it.",
                    "Using Ollama - no API key required."
                )
                if new_source != source:
                    cell['source'] = [new_source]
                    changed = True
    
    if changed:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
        return True
    return False

def main():
    """Update all notebooks in the repository."""
    repo_root = Path(__file__).parent
    notebooks = list(repo_root.glob('**/*.ipynb'))
    
    # Exclude checkpoints
    notebooks = [nb for nb in notebooks if '.ipynb_checkpoints' not in str(nb)]
    
    updated_count = 0
    for notebook_path in notebooks:
        if update_notebook(notebook_path):
            print(f"Updated: {notebook_path.relative_to(repo_root)}")
            updated_count += 1
        else:
            print(f"No changes: {notebook_path.relative_to(repo_root)}")
    
    print(f"\nTotal updated: {updated_count}/{len(notebooks)} notebooks")

if __name__ == '__main__':
    main()
