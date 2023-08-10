import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from googletrans import Translator

class TranslatorApp(Gtk.Window):

    def _init_(self):
        super(TranslatorApp, self)._init_(title="AI Translator")

        self.translator = Translator()

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        self.textview_source = Gtk.TextView()
        vbox.pack_start(self.textview_source, True, True, 0)

        self.language_combobox = Gtk.ComboBoxText()
        self.language_mapping = {
            "English": "en",
            "Telugu": "te",
            "Tamil": "ta",
            "Hindi": "hi",
            "Kannada": "kn",
            "Malayalam": "ml",
            "Gujarati": "gu",
            "Spanish": "es",
            "Italian": "it",
            "German": "de"
        }

        for lang in self.language_mapping:
            self.language_combobox.append_text(lang)

        vbox.pack_start(self.language_combobox, False, False, 0)

        btn_translate = Gtk.Button(label="Translate")
        btn_translate.connect("clicked", self.on_translate_clicked)
        vbox.pack_start(btn_translate, False, False, 0)

        self.textview_translated = Gtk.TextView()
        vbox.pack_start(self.textview_translated, True, True, 0)

    def on_translate_clicked(self, widget):
        source_buffer = self.textview_source.get_buffer()
        source_text = source_buffer.get_text(source_buffer.get_start_iter(), source_buffer.get_end_iter(), True)
        target_language = self.language_mapping[self.language_combobox.get_active_text()]
        
        translated_text = self.google_translate(source_text, target_language)

        translated_buffer = self.textview_translated.get_buffer()
        translated_buffer.set_text(translated_text)

    def google_translate(self, source_text, target_language):
        translation = self.translator.translate(source_text, dest=target_language)
        return translation.text

css = """
* {
    font-size: 16px;
    padding: 10px;
}

GtkBox {
    border-radius: 8px;
    background-color: #f4f4f4;
    padding: 20px;
}

GtkWindow {
    background-color: #e0e0e0;
}

GtkTextView {
    background-color: #ffffff;
    border-radius: 5px;
    border: 1px solid #ccc;
    padding: 15px;
}

GtkComboBoxText {
    background-color: #ffffff;
    border-radius: 5px;
    border: 1px solid #ccc;
    padding: 10px 5px;
}

GtkButton {
    background-color: #007bff;
    border-radius: 5px;
    border: none;
    padding: 12px 20px;
    color: #FFFFFF;
    font-weight: bold;
    transition: background-color 0.3s;
}

GtkButton:hover {
    background-color: #0056b3;
}

GtkButton:active {
    background-color: #004499;
}

"""

style_provider = Gtk.CssProvider()
style_provider.load_from_data(bytes(css.encode()))

Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(),
    style_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

win = TranslatorApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()