from diaries.AbstractDiary import AbstractDiary

class DiarySample(AbstractDiary):
    def get_date(self):
        return "2023-12-14"
    
    def get_summary(self):
        return "オブ演のグループ学習が始まった。足を引っ張ることがないように頑張りたい。"
    
    def get_author(self):
        return "Asai"