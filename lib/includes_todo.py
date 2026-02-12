
def includes_todo(text):
    # it should check #TODO
    if "#TODO" in text or "#todo" in text:
        return True
    else:    
        return False