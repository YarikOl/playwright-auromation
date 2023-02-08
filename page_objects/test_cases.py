from playwright.sync_api import Page

class TestCases:
    def __init__(self, page: Page):
        self.page = page

    def check_test_exists(self, test_name: str):
        return self.page.get_by_label("test1")

    def delete_test_by_name(self, test_name: str):
        self.page.click("//tbody/descendant::tr[12]/descendant::td[9]")

    def check_columns_hidden(self):
        description = self.page.is_hidden('.thDes')
        author = self.page.is_hidden('.thAuthor')
        executor = self.page.is_hidden('.thLast')
        return description and author and executor