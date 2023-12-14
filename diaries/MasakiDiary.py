from diaries.AbstractDiary import AbstractDiary

class MasakiDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-14"

    def get_summary(self):
        return "GitHubの使い方を学ぶことができた。"

    def get_author(self):
        return "Yuya Masaki"