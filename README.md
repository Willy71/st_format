`st_format` 
# - Streamlit Formatting Utilities

`st_format` is a Python library designed to enhance the presentation of Streamlit apps by providing utility functions for formatting and layout customization. This library allows you to easily set backgrounds, center images, create custom text alignments, and more.

Installation

You can install `st_format` directly from PyPI:

```bash
pip install st-format
```

Functions

1. `set_background`

Sets a background image for the Streamlit app.

**Parameters:**
- `image_url` (str): The URL of the background image.
- `size` (str): The size of the background image. (default: `"180%"`)
- `position` (str): The position of the background image. (default: `"top left"`)
- `repeat` (str): The background image repeat behavior. (default: `"repeat"`)
- `attachment` (str): The background image attachment behavior. (default: `"local"`)

**Usage:**

```python
import streamlit as st
from st_format import set_background

set_background(
    image_url="https://raw.githubusercontent.com/Willy71/background/main/picture/pxfuel%20(1).jpg"
)
```

### 2. `center_picture`

Centers an image on the Streamlit page.

**Parameters:**
- `image` (str): The URL of the image.
- `width` (str): The width of the image.

**Usage:**

```python
from st_format import center_picture

center_picture(
    image="https://example.com/image.png",
    width="300px"
)
```

### 3. `line`

Draws a horizontal line on the Streamlit page.

**Parameters:**
- `size` (str): The thickness of the line.
- `color` (str): The color of the line.

**Usage:**

```python
from st_format import line

line(
    size="2",
    color="black"
)
```

### 4. `center_text`

Centers text on the Streamlit page.

**Parameters:**
- `text` (str): The text to display.
- `size` (str): The size of the text (HTML heading size, e.g., `"1"` for `<h1>`).
- `color` (str): The color of the text.

**Usage:**

```python
from st_format import center_text

center_text(
    text="Welcome to My App",
    size="2",
    color="blue"
)
```

### 5. `text_left`

Aligns text to the left on the Streamlit page.

**Parameters:**
- `text` (str): The text to display.
- `size` (str): The size of the text (HTML heading size, e.g., `"1"` for `<h1>`).
- `color` (str): The color of the text.

**Usage:**

```python
from st_format import text_left

text_left(
    text="This is left-aligned text.",
    size="3",
    color="green"
)
```

### 6. `center_text_link`

Centers a hyperlink on the Streamlit page.

**Parameters:**
- `link_text` (str): The text to display as a hyperlink.
- `link_url` (str): The URL the link points to.
- `size` (str): The size of the text (HTML heading size, e.g., `"1"` for `<h1>`).
- `color` (str): The color of the text.

**Usage:**

```python
from st_format import center_text_link

center_text_link(
    link_text="Visit My Website",
    link_url="https://example.com",
    size="3",
    color="red"
)
```
### 7. 'left_text_link'

Place a hyperlink on the left

**Parameters:**
    - 'link_text' (str): The text to display as a hyperlink.
    - 'link_url' (str): The URL the link points to.
    - 'size' (str): The size of the text (HTML heading size, e.g., "1" for <h1>).
    - 'color' (str): The color of the text.

**Usage:**

```python
from st_format import left_text_link

left_text_link(
    link_text="Visit My Website",
    link_url="https://example.com",
    size="3",
    color="red"
)
```

### 8. `photo_link`

Creates a hyperlink with an image on the Streamlit page.

**Parameters:**
- `alt_text` (str): The alt text for the image.
- `img_url` (str): The URL of the image.
- `link_url` (str): The URL the image links to.
- `img_width` (str): The width of the image in pixels.

**Usage:**

```python
from st_format import photo_link

photo_link(
    alt_text="Image description",
    img_url="https://example.com/image.png",
    link_url="https://example.com",
    img_width="200"
)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
