import os
import sys
import tkinter
import tkinter.ttk

# Local Imports
from util import new_widget
from responsive_entry import ResponsiveEntry

# Constant Definitions
FRAME = tkinter.ttk.Frame
BUTTON = tkinter.ttk.Button

class CommandBar(FRAME):
    RUN_TEXT = "Run"
    SAVE_TEXT = "Save"
    CLEAR_TEXT = "Clear"
    COMMAND_DEFAULT_TEXT = "Enter Command"

    def __init__(self, root, **kwargs):

        # Class variable initializations
        self._root = root
        self._config = root._config
        self._run_btn = None
        self._save_btn = None
        self._clear_btn = None
        self._btn_frm = None
        self._cmd_entry = None

        # Create main frame
        new_widget(root, super(), **kwargs)

        # Add children to main frame
        s_cmd_entry = {"pack": {"fill": "x", "pady": (0, 5)}, "default": self.COMMAND_DEFAULT_TEXT}
        self._cmd_entry = ResponsiveEntry(self, **s_cmd_entry)
        self._cmd_entry.focus()
        self._add_actions()

        # Add event bindings
        self._cmd_entry.bind("<Return>", lambda e: self._action_click(self.RUN_TEXT))

        return None

    def __call__(self):
        return self

    def _add_actions(self):
        btn_texts = [self.RUN_TEXT, self.SAVE_TEXT, self.CLEAR_TEXT]
        btn_vars = [self._run_btn, self._save_btn, self._clear_btn]

        # Button Frame
        s_btn_frm = {"pack": {"fill": "x"}}
        self._btn_frm = new_widget(self, FRAME, **s_btn_frm)

        # Adding all command buttons
        for i in range(len(btn_vars)):
            s_btn = {"pack": {"side": "right", "padx": (5, 0)}, "text": btn_texts[i]}
            btn_vars[i] = new_widget(self._btn_frm, BUTTON, **s_btn)
            btn_vars[i]["command"] = lambda text=btn_texts[i]: self._action_click(text)

        return None

    def _action_click(self, btn_text):
        cmd = self._cmd_entry.get()
        no_cmd = cmd == self.COMMAND_DEFAULT_TEXT

        # Check the type of button clicked
        if btn_text == self.CLEAR_TEXT:
            self._cmd_entry.clear()
        elif btn_text == self.RUN_TEXT and not no_cmd:
            t_cmd = self._config.get_terminal_command()
            os.system(t_cmd.format(cmd))
        elif btn_text == self.SAVE_TEXT and not no_cmd:
            #TODO: Create popup to pick save location
            pass
        else: pass

        return None