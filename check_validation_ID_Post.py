
#* checking ID post is valid or not?

def check_validation(valid:str) -> None:
    if len(valid)==24 and valid.isdigit():
        pass
    else:
        print("Wrong code, valid code have 24-digit number!")
        exit()