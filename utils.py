import readline

# function to prefill input for editing tasks/actions
def input_with_prefill(prompt, text) -> str:
    text = str(text)

    def hook():
        readline.insert_text(text)
        readline.redisplay()

    readline.set_pre_input_hook(hook)
    result = input(prompt)
    readline.set_pre_input_hook()
    return result
