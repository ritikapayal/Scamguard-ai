try:
    exec(open('llm/prompts.py').read())
    print('executed')
    print('generate_prompt' in locals())
except Exception as e:
    print('error:', e)