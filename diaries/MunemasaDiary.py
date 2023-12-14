from diaries.AbstractDiary import AbstractDiary

class MunemasaDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-14"
    
    def get_summary(self):
        return "班の人と話せて嬉しかった"
    
    def get_author(self):
        return "Munemasa"