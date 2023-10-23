from app.config import app_configuration


class Config:
    data: dict = app_configuration

    @staticmethod
    def __site_name__() -> str:
        value = Config.data.get("site_name", "Site Name")
        return value if value else "Site Name"

    @staticmethod
    def __copy_right__() -> str:
        value = Config.data.get("copy_right", "")
        return value if value else ""

    @staticmethod
    def __attribute__() -> str:
        value = Config.data.get("attribute", "")
        return value if value else ""

    @staticmethod
    def __theme_font__() -> str:
        value = Config.data["theme"].get("font", "Times New Roman")
        return value if value else "Times New Roman"
