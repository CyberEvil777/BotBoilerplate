from telegram.ext.filters import Filters


class CustomFilters:
    class button(Filters.regex):
        def __init__(self, button_text):
            pattern = f"^({button_text})$"
            super().__init__(pattern)

