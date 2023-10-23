from app.styles._base import base_css


class CSSHelper:
    @staticmethod
    def __base_css__() -> dict:
        return base_css
    
    @staticmethod
    def __header_css__() -> dict:
        return base_css.get("header_css", {})
    
    @staticmethod
    def __navigation_css__() -> dict:
        return base_css.get("navigation_css", {})
    
    @staticmethod
    def __navigation_item_css__() -> dict:
        return base_css.get("navigation_item_css", {})