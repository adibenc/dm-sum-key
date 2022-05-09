


def log(text):
    def test(text):
        print("[log]-",text)
    
    return test

@log
def summarize(text1):
    summarizd = "1"
    print("why")

    # return summarizd

summarize("sum test", text1="1")