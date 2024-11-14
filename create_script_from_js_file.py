def create_script(js_file):

    text = open(js_file).read()
    
    return f"<script>\n{text}\n</script>"


