from diaries.AbstractDiary import AbstractDiary

class KimuraDiary(AbstractDiary):
    def get_date(self):
        return "2023-12-14"
    
    def get_summary(self):
        return "何もかも思い通りに行くと思ってはいけないと思い知らされた。"
    
    def get_author(self):
        return "Kimura"