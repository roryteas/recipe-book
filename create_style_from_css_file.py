def create_style(css_file):

    text = open(css_file).read()
    
    return f"<style>\n{text}\n</script>"

