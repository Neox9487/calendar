class Date:
    def __init__(
        self,
        day : int,
        month : int,
        year : int
    ):
        self.day = day
        self.month = month
        self.year = year

    def toStr(self) -> str:
        return f"{self.day}/{self.month}/{self.year}"
    
def toDate(date : str) -> Date:
    d = ""
    m = ""
    y = ""
    i = 0
    for c in date:
        if i==0:
            if c == "/":
                i+=1
                continue
            d+=c
        elif i==1:
            if c == "/":
                i+=1
                continue
            m+=c
        else:
            y+=c
    return Date(int(d), int(m), int(y))