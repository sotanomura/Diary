from diaries.AbstractDiary import AbstractDiary

class DiarySample(AbstractDiary):
    def get_date(self):
        return "2021-12-14"
    
    def get_summary(self):
        return """リーダーに就任してしまった。
        よい一年にしたかった。
        また来年は頑張ろう。"""
    
    def get_author(self):
        return "Matsudo"