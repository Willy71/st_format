import streamlit as st


def set_background(image_url, size="180%", position="top left", repeat="repeat", attachment="local"):
    """
    Sets a background image for the Streamlit app.

    Parameters:
    - image_url (str): The URL of the background image.
    - size (str): The size of the background image. (default: "180%")
    - position (str): The position of the background image. (default: "top left")
    - repeat (str): The background image repeat behavior. (default: "repeat")
    - attachment (str): The background image attachment behavior. (default: "local")
    """
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("{image_url}");
    background-size: {size};
    background-position: {position};
    background-repeat: {repeat};
    background-attachment: {attachment};
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)


def center_picture(image, width):
    """
    Centers an image on the Streamlit page.

    Parameters:
    - image (str): The URL of the image.
    - width (str): The width of the image.
    """
    st.markdown(
        f'<div style="display: flex; justify-content: center;">'
        f'<img src="{image}" width="{width}">'
        f'</div>',
        unsafe_allow_html=True
    )


def line(size, color):
    """
    Draws a horizontal line on the Streamlit page.

    Parameters:
    - size (str): The thickness of the line.
    - color (str): The color of the line.
    """
    st.markdown(
        f"<hr style='height:{size}px;border:none;color:{color};background-color:{color};' />",
        unsafe_allow_html=True
    )


def center_text(text, size, color):
    """
    Centers text on the Streamlit page.

    Parameters:
    - text (str): The text to display.
    - size (str): The size of the text (HTML heading size, e.g., "1" for <h1>).
    - color (str): The color of the text.
    """
    st.markdown(
        f"<h{size} style='text-align: center; color: {color}'>{text}</h{size}>",
        unsafe_allow_html=True
    )
    

def text_left(text, size, color):
    """
    Aligns text to the left on the Streamlit page.

    Parameters:
    - text (str): The text to display.
    - size (str): The size of the text (HTML heading size, e.g., "1" for <h1>).
    - color (str): The color of the text.
    """
    st.markdown(
        f"<h{size} style='text-align: left; color: {color}'>{text}</h{size}>",
        unsafe_allow_html=True
    )

def text_right(text, size, color):
    """
    Aligns text to the right on the Streamlit page.

    Parameters:
    - text (str): The text to display.
    - size (str): The size of the text (HTML heading size, e.g., "1" for <h1>).
    - color (str): The color of the text.
    """
    st.markdown(
        f"<h{size} style='text-align: right; color: {color}'>{text}</h{size}>",
        unsafe_allow_html=True
    )


def center_text_link(link_text, link_url, size, color):
    """
    Centers a hyperlink on the Streamlit page.

    Parameters:
    - link_text (str): The text to display as a hyperlink.
    - link_url (str): The URL the link points to.
    - size (str): The size of the text (HTML heading size, e.g., "1" for <h1>).
    - color (str): The color of the text.
    """
    st.markdown(
        f"<h{size} style='text-align: center; color: {color}'><a href='{link_url}' target='_blank'>{link_text}</a></h{size}>",
        unsafe_allow_html=True
    )

def left_text_link(link_text, link_url, size, color):
    """
    Place a hyperlink on the left

    Parameters:
    - link_text (str): The text to display as a hyperlink.
    - link_url (str): The URL the link points to.
    - size (str): The size of the text (HTML heading size, e.g., "1" for <h1>).
    - color (str): The color of the text.
    """
    st.markdown(
        f"<h{size} style='text-align: left; color: {color}'><a href='{link_url}' target='_blank'>{link_text}</a></h{size}>",
        unsafe_allow_html=True
    )


def photo_link(alt_text, img_url, link_url, img_width):
    """
    Creates a hyperlink with an image on the Streamlit page.

    Parameters:
    - alt_text (str): The alt text for the image.
    - img_url (str): The URL of the image.
    - link_url (str): The URL the image links to.
    - img_width (str): The width of the image in pixels.
    """
    markdown_code = f'<a href="{link_url}" target="_blank"><img src="{img_url}" alt="{alt_text}" width="{img_width}px"></a>'
    st.markdown(markdown_code, unsafe_allow_html=True)
