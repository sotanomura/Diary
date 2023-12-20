from diaries.AbstractDiary import AbstractDiary

class sotanomuraDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-14"

    def get_summary(self):
        return "GitHubの基本的な使い方について学んだ。fetch,pull,rebaseはまだ感覚的に慣れない。"

    def get_author(self):
        return "sotanomura"