from app.helpers.app_config import Config

base_css: dict = {
    "app": {
        "font_family": Config.__theme_font__(),
        
    },
    "header_css":  {
        "width": "100vw",
        "padding": "15px",
        "justify_content": "center",
        "justify_items": "center"
    }
}