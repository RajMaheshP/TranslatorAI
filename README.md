# TranslatorAI

```markdown
# AI Translator App

The AI Translator App is a simple graphical user interface (GUI) application built using Python and the GTK library. It allows you to easily translate text using the Google Translate API. The app provides a user-friendly interface where you can enter the source text, select the target language, and view the translated text.

![AI Translator App](screenshot.png)

## Features

- Translate text from one language to another using Google Translate API.
- Supports various languages for translation.
- User-friendly graphical interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- `googletrans` and `pygobject` Python packages installed. You can install them using the following command:

```bash
pip install googletrans==4.0.0-rc1 pygobject
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/RajMaheshP/TranslatorAI
```

2. Navigate to the project directory:

```bash
cd TranslatorAI/src/main.py
```

## Usage

Run the translator app using the following command:

```bash
python translator_app.py
```

## How to Use

1. Enter the text you want to translate in the source text box.
2. Choose the target language from the dropdown menu.
3. Click the "Translate" button to see the translated text in the output box.

## Customization

You can customize the styling of the app by modifying the CSS code in the `translator_app.py` file. The CSS is used to style various components of the GUI.

## Contributions

Contributions are welcome! If you find a bug or want to enhance the application, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgements

- This app was created as a learning exercise using Python and GTK.
- Thanks to the creators of the `googletrans` library for providing an easy-to-use translation API.

**Disclaimer:** This app is intended for educational and personal use. It relies on the Google Translate API, which may have usage limitations. Please refer to the [Google Translate API documentation](https://cloud.google.com/translate/docs) for more information.
