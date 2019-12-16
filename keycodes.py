class Keycode:
    """USB HID Keycode constants.
    This list is modeled after the names for USB keycodes defined in
    https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf#page=53.
    This list does not include every single code, but does include all the keys on
    a regular PC or Mac keyboard.
    Remember that keycodes are the names for key *positions* on a US keyboard, and may
    not correspond to the character that you mean to send if you want to emulate non-US keyboard.
    For instance, on a French keyboard (AZERTY instead of QWERTY),
    the keycode for 'q' is used to indicate an 'a'. Likewise, 'y' represents 'z' on
    a German keyboard. This is historical: the idea was that the keycaps could be changed
    without changing the keycodes sent, so that different firmware was not needed for
    different variations of a keyboard.
    """
    #pylint: disable-msg=invalid-name
    A = 4
    """``a`` and ``A``"""
    B = 5
    """``b`` and ``B``"""
    C = 6
    """``c`` and ``C``"""
    D = 7
    """``d`` and ``D``"""
    E = 8
    """``e`` and ``E``"""
    F = 9
    """``f`` and ``F``"""
    G = 10
    """``g`` and ``G``"""
    H = 11
    """``h`` and ``H``"""
    I = 12
    """``i`` and ``I``"""
    J = 13
    """``j`` and ``J``"""
    K = 14
    """``k`` and ``K``"""
    L = 15
    """``l`` and ``L``"""
    M = 16
    """``m`` and ``M``"""
    N = 17
    """``n`` and ``N``"""
    O = 18
    """``o`` and ``O``"""
    P = 19
    """``p`` and ``P``"""
    Q = 20
    """``q`` and ``Q``"""
    R = 21
    """``r`` and ``R``"""
    S = 22
    """``s`` and ``S``"""
    T = 23
    """``t`` and ``T``"""
    U = 24
    """``u`` and ``U``"""
    V = 25
    """``v`` and ``V``"""
    W = 26
    """``w`` and ``W``"""
    X = 27
    """``x`` and ``X``"""
    Y = 28
    """``y`` and ``Y``"""
    Z = 29
    """``z`` and ``Z``"""

    ONE = 30
    """``1`` and ``!``"""
    TWO = 31
    """``2`` and ``@``"""
    THREE = 32
    """``3`` and ``#``"""
    FOUR = 33
    """``4`` and ``$``"""
    FIVE = 34
    """``5`` and ``%``"""
    SIX = 35
    """``6`` and ``^``"""
    SEVEN = 36
    """``7`` and ``&``"""
    EIGHT = 37
    """``8`` and ``*``"""
    NINE = 38
    """``9`` and ``(``"""
    ZERO = 39
    """``0`` and ``)``"""
    ENTER = 40
    """Enter (Return)"""
    RETURN = ENTER
    """Alias for ``ENTER``"""
    ESCAPE = 41
    """Escape"""
    BACKSPACE = 42
    """Delete backward (Backspace)"""
    TAB = 43
    """Tab and Backtab"""
    SPACEBAR = 44
    """Spacebar"""
    SPACE = SPACEBAR
    """Alias for SPACEBAR"""
    MINUS = 45
    """``-` and ``_``"""
    EQUALS = 46
    """``=` and ``+``"""
    LEFT_BRACKET = 47
    """``[`` and ``{``"""
    RIGHT_BRACKET = 48
    """``]`` and ``}``"""
    BACKSLASH = 49
    r"""``\`` and ``|``"""
    POUND = 50
    """``#`` and ``~`` (Non-US keyboard)"""
    SEMICOLON = 51
    """``;`` and ``:``"""
    QUOTE = 52
    """``'`` and ``"``"""
    GRAVE_ACCENT = 53
    r""":literal:`\`` and ``~``"""
    COMMA = 54
    """``,`` and ``<``"""
    PERIOD = 55
    """``.`` and ``>``"""
    FORWARD_SLASH = 56
    """``/`` and ``?``"""

    CAPS_LOCK = 57
    """Caps Lock"""

    F1 = 58
    """Function key F1"""
    F2 = 59
    """Function key F2"""
    F3 = 60
    """Function key F3"""
    F4 = 61
    """Function key F4"""
    F5 = 62
    """Function key F5"""
    F6 = 63
    """Function key F6"""
    F7 = 64
    """Function key F7"""
    F8 = 65
    """Function key F8"""
    F9 = 66
    """Function key F9"""
    F10 = 67
    """Function key F10"""
    F11 = 68
    """Function key F11"""
    F12 = 69
    """Function key F12"""

    PRINT_SCREEN = 70
    """Print Screen (SysRq)"""
    SCROLL_LOCK =71
    """Scroll Lock"""
    PAUSE =72
    """Pause (Break)"""

    INSERT =73
    """Insert"""
    HOME =74
    """Home (often moves to beginning of line)"""
    PAGE_UP =75
    """Go back one page"""
    DELETE =76
    """Delete forward"""
    END =77
    """End (often moves to end of line)"""
    PAGE_DOWN =78
    """Go forward one page"""

    RIGHT_ARROW =79
    """Move the cursor right"""
    LEFT_ARROW =80
    """Move the cursor left"""
    DOWN_ARROW =81
    """Move the cursor down"""
    UP_ARROW =82
    """Move the cursor up"""

    KEYPAD_NUMLOCK =83
    """Num Lock (Clear on Mac)"""
    KEYPAD_FORWARD_SLASH =84
    """Keypad ``/``"""
    KEYPAD_ASTERISK =85
    """Keypad ``*``"""
    KEYPAD_MINUS =86
    """Keyapd ``-``"""
    KEYPAD_PLUS =87
    """Keypad ``+``"""
    KEYPAD_ENTER =88
    """Keypad Enter"""
    KEYPAD_ONE =89
    """Keypad ``1`` and End"""
    KEYPAD_TWO =90
    """Keypad ``2`` and Down Arrow"""
    KEYPAD_THREE =91
    """Keypad ``3`` and PgDn"""
    KEYPAD_FOUR =92
    """Keypad ``4`` and Left Arrow"""
    KEYPAD_FIVE =93
    """Keypad ``5``"""
    KEYPAD_SIX =94
    """Keypad ``6`` and Right Arrow"""
    KEYPAD_SEVEN =95
    """Keypad ``7`` and Home"""
    KEYPAD_EIGHT =96
    """Keypad ``8`` and Up Arrow"""
    KEYPAD_NINE =97
    """Keypad ``9`` and PgUp"""
    KEYPAD_ZERO =98
    """Keypad ``0`` and Ins"""
    KEYPAD_PERIOD =99
    """Keypad ``.`` and Del"""
    KEYPAD_BACKSLASH =100
    """Keypad ``\\`` and ``|`` (Non-US)"""

    APPLICATION =101
    """Application: also known as the Menu key (Windows)"""
    POWER =102
    """Power (Mac)"""
    KEYPAD_EQUALS =103
    """Keypad ``=`` (Mac)"""
    F13 =104
    """Function key F13 (Mac)"""
    F14 =105
    """Function key F14 (Mac)"""
    F15 =106
    """Function key F15 (Mac)"""
    F16 =107
    """Function key F16 (Mac)"""
    F17 =108
    """Function key F17 (Mac)"""
    F18 =109
    """Function key F18 (Mac)"""
    F19 =110
    """Function key F19 (Mac)"""

    LEFT_CONTROL =224
    """Control modifier left of the spacebar"""
    CONTROL = LEFT_CONTROL
    """Alias for LEFT_CONTROL"""
    LEFT_SHIFT =225
    """Shift modifier left of the spacebar"""
    SHIFT = LEFT_SHIFT
    """Alias for LEFT_SHIFT"""
    LEFT_ALT =226
    """Alt modifier left of the spacebar"""
    ALT = LEFT_ALT
    """Alias for LEFT_ALT; Alt is also known as Option (Mac)"""
    OPTION = ALT
    """Labeled as Option on some Mac keyboards"""
    LEFT_GUI =227
    """GUI modifier left of the spacebar"""
    GUI = LEFT_GUI
    """Alias for LEFT_GUI; GUI is also known as the Windows key, Command (Mac), or Meta"""
    WINDOWS = GUI
    """Labeled with a Windows logo on Windows keyboards"""
    COMMAND = GUI
    """Labeled as Command on Mac keyboards, with a clover glyph"""
    RIGHT_CONTROL =228
    """Control modifier right of the spacebar"""
    RIGHT_SHIFT =229
    """Shift modifier right of the spacebar"""
    RIGHT_ALT =230
    """Alt modifier right of the spacebar"""
    RIGHT_GUI =231
    """GUI modifier right of the spacebar"""

    #pylint: enable-msg=invalid-name
    @classmethod
    def modifier_bit(cls, keycode):
        """Return the modifer bit to be set in an HID keycode report if this is a
        modifier key; otherwise return 0."""
        return 1 << (keycode - 0xE0) if cls.LEFT_CONTROL <= keycode <= cls.RIGHT_GUI else 0
