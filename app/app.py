import reflex as rx
from app.helpers.css_helper import CSSHelper
from app.helpers.app_config import Config


class State(rx.State):
    pass


class Header:
    
    def __init__(self) -> None:
        self.header: rx.flex = rx.flex(
            style=CSSHelper.__header_css__()
        )
        self.site_name: rx.hstack = rx.hstack(
            rx.avatar(name="Horizon Lin", size="md"),
            rx.text(Config.__site_name__(), font_weight="normal", font_size="2rem")
        )
        self.button_group = rx.button_group(
            rx.button("Home", size="lg", on_click=rx.redirect("/")),
            rx.button("About", size="lg", on_click=rx.redirect("/#about")),
            rx.button("Work", size="lg", on_click=rx.redirect("/#work")),
            rx.button("Event", size="lg", on_click=rx.redirect("/#event")),
            variant="ghost",
            spacing=8,
            margin_left="12vw"
        )
    
    def compile_component(self):
        return [self.site_name, self.button_group]
    
    def build(self):
        self.header.children = self.compile_component()
        return self.header


class Content:
    
    def __init__(self) -> None:
        self.main_area: rx.vstack = rx.vstack()
        self.banner: rx.image = rx.image(
            src="/banner.png", width="100%", height="auto", class_name="banner"
        )
        self.content_about: rx.flex = rx.flex(
            rx.box(
                rx.text("About Me", class_name="about_me"),
                rx.text("01", class_name="about_me_num"),
                rx.text("I love games and creating gaming experiences. ", class_name="about_me_title"),
                rx.text("""Hello, I'm Horizon Lin.
                
I have a bachelor's degree in journalism and worked at Minecraft China (Authorized by Microsoft and represented by NetEase Games) in marketing position for two years.

Based on my past experience working with Minecraft China, I became very interested in game-based learning. I love creating games to express my ideas, especially in Minecraft. I hoping for creating immersive experiences for kids all over the world sometime in the future.
                """, white_space="pre-wrap", class_name="about_me_content"),
                width="23.5rem",
                height="35rem"
            ),
            rx.box(
                bg="blue",
                width="23.5rem",
                height="35rem",
                margin_left="20rem"
            ),
            justify_content="center",
            justify_items="center",
            id="about"
        )
        self.content_spacer_top: rx.box = rx.box(
            height="1.55rem"
        )
        self.content_spacer_bottom: rx.box = rx.box(
            height="2rem"
        )
        self.content_work_from_student: rx.flex = rx.flex(
            rx.box(
                rx.box(
                    rx.span("Works ", color="#F59A23", font_weight="bold"),
                    rx.text("from student days", color="black", font_weight="bold"),
                    class_name="work-title-from-student"
                ),
                rx.video(
                    url="https://www.youtube.com/embed/X6C5txfa5Uw?si=13Vm7uMB8RCrk75a",
                    width="532px",
                    height="300px",
                    class_name="work-video-1"
                ),
                rx.box(
                    rx.heading("Lost Era", color="black", font_weight="bold", class_name="work-title-2"),
                    rx.text(
                        """Info:

Prehistoric behemoths ruled our blue planet for hundreds of millions of years, and with this add-on, users will follow in the footsteps of time and explore the mysteries of unknown life in the past.

Main Contributions: Game Design, Game Development.
                        """, white_space="pre-wrap", class_name="work-info-2", width="30rem"
                    )
                ),
                rx.video(
                    url="https://www.youtube.com/embed/6kg0PB2S-bU?si=VjBQmPvQm9JDWrtH",
                    width="532px",
                    height="300px",
                    class_name="work-video-3"
                ),
                rx.box(
                    rx.span("Works ", color="#F59A23", font_weight="bold"),
                    rx.text("from previous job", color="black", font_weight="bold"),
                    class_name="work-title-from-job"
                ),
                rx.box(
                    rx.heading("Minecraft 2021 College Creator Summer Camp", color="black", font_weight="bold", class_name="work-title-4", width="30rem"),
                    rx.text(
                        """Info:

As an official staff member of Minecraft China, I explain the technical skills of creating content for Minecraft to college students on Internet.

Main Contributions: Course Instructor.
                        """, white_space="pre-wrap", class_name="work-info-4", width="30rem"
                    )
                ),
                rx.box(
                    rx.box(
                        rx.tooltip(
                            rx.image(src="/school_0.png", _hover={"cursor": "pointer"}),
                            label="Click it to be redirected to the news website.",
                            on_click=rx.redirect("https://mc.163.com/developer_cn/news/secondary/20220629/33941_1026022.html", True)
                        ),
                        width="540px",
                        height="304px",
                        class_name="work-job-1"
                    )
                ),
                rx.heading(
                    "Shanghai Film Academy Joint Development Course", color="black", font_weight="bold",
                    width="30rem", class_name="work-job-2-title"
                ),
                rx.text(
                    """Info:

As an online instructor, I record instructional videos, provide online tutoring and in-class homework reviews for students participating in the course.

Main Contributions: Online instructor.
                    """, white_space="pre-wrap", class_name="work-job-2-info", width="30rem"
                ),
                width="22.5rem",
                height="63.4375rem",
                class_name="work-area-1"
            ),
            rx.box(
                rx.text("02", class_name="work-num"),
                rx.heading("Machine Armor", color="black", font_weight="bold", class_name="work-title-1"),
                rx.text(
                    """Info:
                    
Users will pilot three robots with different armed forces to face a bizarre biochemical crisis using robot workbenches and cutting-edge technology!

Main Contributions: Game Design, Game Development.
                    """, white_space="pre-wrap", class_name="work-info-1", width="30rem"
                ),
                rx.video(
                    url="https://www.youtube.com/embed/ES4c5_sZeD4?si=Ko1lirXvwkAqO035",
                    width="532px",
                    height="300px",
                    class_name="work-video-2"
                ),
                rx.heading("Apocalypse: Endless Fantasy", color="black", font_weight="bold", class_name="work-title-3", width="30rem"),
                rx.text(
                    """Info:

After ending the reign of the Tide Queen, the beings of the Apocalypse Continent gained a brief moment of peace.But with the reappearance of the Empress's palace and the mastermind behind it, players will take on the role of a new Chosen One and resume a fantastical adventure.

Main Contributions: Game Development.
                    """, white_space="pre-wrap", class_name="work-info-3", width="30rem"
                ),
                rx.box(
                    rx.tooltip(
                        rx.image(src="/course_0.png", _hover={"cursor": "pointer"}),
                        label="Click it to be redirected to the course website."
                    ),
                    width="540px",
                    height="304px",
                    text_align="justify",
                    class_name="work-job-0",
                    on_click=rx.redirect("https://game.academy.163.com/live?id=ga-1624441250437", True)
                ),
                rx.heading(
                    "Xiamen University Joint development of elective courses", color="black", font_weight="bold", width="30rem", class_name="work-job-1-title"
                ),
                rx.text(
                    """Info:

As an online instructor, I record instructional videos, provide online tutoring and in-class homework reviews for students participating in the course.

Main Contributions: Online instructor.
                    """, white_space="pre-wrap", class_name="work-job-1-info", width="30rem"
                ),
                rx.box(
                    rx.tooltip(
                        rx.image(src="/school_1.jpg", _hover={"cursor": "pointer"}),
                        label="Click it to be redirected to the news website."
                    ),
                    width="540px",
                    height="304px",
                    text_align="justify",
                    class_name="work-job-2",
                    on_click=rx.redirect("https://mc.163.com/developer_cn/news/latest/20220325/36504_1009307.html", True)
                ),
                width="22.5rem",
                height="63.4375rem"
            ),
            justify_content="center",
            justify_items="center",
            id="work",
            width="100%",
            height="170rem"
        )
        self.content_what_more: rx.vstack = rx.vstack(
            rx.text("Furthermore", color="black", font_weight="bold", class_name="work-what-more-title"),
            rx.text("I continue to develop myself as a game design polymath. I learned C4D and used scene models and 3D props to render visuals to tell stories.", class_name="work-what-more-info"),
            rx.vstack(
                rx.hstack(
                    rx.image(
                        src="/PirateIsland.png", width="512px", height="288px"
                    ),
                    rx.box(
                        width="1.8rem"
                    ),
                    rx.image(
                        src="/MapleVillage.png", width="512px", height="288px"
                    )
                ),
                rx.hstack(
                    rx.text("""Info:
                    
The beach house is lit up at night and exudes an eerie atmosphere.

Tools: C4D, Photoshop""", white_space="pre-wrap", position="relative", right="4.75rem", top="2.55rem"),
                    rx.text("""Info:
                    
Horizon Lin is watching the sunset in the forest with a deer.

Tools: C4D, Photoshop""", white_space="pre-wrap", position="relative", right="0.75rem", top="2.55rem")
                )
            ),
            rx.box(
                height="5rem"
            ),
            bg="#828181",
            width="100vw"
        )
        self.content_event: rx.flex = rx.flex(
            rx.box(
            rx.box(
                rx.box(
                    rx.span("Event ", color="#F59A23", font_weight="bold"),
                    rx.text("presented from student days", color="black", font_weight="bold"),
                    class_name="event-title"
                ),
                rx.text("03", class_name="event-num"),
                rx.box(
                    rx.heading("Minecraft China Conference 2019", color="black", font_weight="bold", class_name="event-title-1"),
                    rx.text(
                        """Info:

Participating as a speaker on the the Minecraft China Conference 2019.""", white_space="pre-wrap", class_name="event-info-1"
                    )
                ),
                height="23.4375rem",
                class_name="event-left"
            ),
            rx.box(
                rx.box(
                    rx.tooltip(
                        rx.image(src="/conference_0.png", _hover={"cursor": "pointer"}),
                        label="Click it to be redirected to the news website."
                    ),
                    width="540px",
                    height="360px",
                    class_name="event-1",
                    on_click=rx.redirect("https://mc.163.com/news/20191209/29175_853351.html", True)
                ),
                width="30rem",
                height="23.4375rem",
            ),
            justify_content="center",
            justify_items="center",
            id="event"
        ))
        
    def compile_component(self):
        return [self.banner,
                self.content_spacer_top,
                self.content_about,
                self.content_spacer_bottom,
                self.content_what_more,
                self.content_work_from_student,
                self.content_event
                ]
    
    def build(self):
        self.main_area.children = self.compile_component()
        return self.main_area


class Footer:
    
    def __init__(self):
        self.footer: rx.flex = rx.flex(
            justify_content="space-around",
            justify_items="center",
            bg="#000000",
            width="100vw"
        )
        self.copyright = rx.container(
            rx.text(Config.__copy_right__(), font_weight="bold", padding=10, color="white", text_align="center")
        )
    
    def compile_component(self):
        return [self.copyright]
    
    def build(self):
        self.footer.children = self.compile_component()
        return self.footer


@rx.page("/")
def index() -> rx.component:
    header: object = Header().build()
    content: object = Content().build()
    footer: object = Footer().build()
    root = rx.vstack(background="#F8F5F4")
    root.children = [
        header,
        content,
        footer
    ]
    return root


app = rx.App(state=State, style=CSSHelper.__base_css__().get("app"), stylesheets=[
    "/extra.css"
])
app.add_page(index)
app.compile()
