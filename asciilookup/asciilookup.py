def char(index: int) -> str:
    '''
    Return the character associated with an index, via the ASCII charset.

    For example:
    5 -> 'ENQ', 
    81 -> 'Q', 
    and so on...
    '''
    return ascii_chars[index]["char"]


def name(index: int) -> str:
    ''' Returns the name of an ASCII character given it's code.

    For example,
    5 -> 'Enquiry',
    81 -> 'Uppercase Q',
    and so on...
    '''
    return ascii_chars[index]["name"]



ascii_chars = [
    {
        "char": "NUL",
        "name": "Null"
    },
    {
        "char": "SOH",
        "name": "Start of heading"
    },
    {
        "char": "STX",
        "name": "Start of text"
    },
    {
        "char": "ETX",
        "name": "End of text"
    },
    {
        "char": "EOT",
        "name": "End of transmission"
    },
    {
        "char": "ENQ",
        "name": "Enquiry"
    },
    {
        "char": "ACK",
        "name": "Acknowledgement"
    },
    {
        "char": "BEL",
        "name": "Bell"
    },
    {
        "char": "BS",
        "name": "Backspace"
    },
    {
        "char": "HT",
        "name": "Horizontal tab"
    },
    {
        "char": "LF",
        "name": "Line feed"
    },
    {
        "char": "VT",
        "name": "Vertical tab"
    },
    {
        "char": "FF",
        "name": "Form feed"
    },
    {
        "char": "CR",
        "name": "Carriage return"
    },
    {
        "char": "SO",
        "name": "Shift out/xon"
    },
    {
        "char": "SI",
        "name": "Shift in/xoff"
    },
    {
        "char": "DLE",
        "name": "Data line escape"
    },
    {
        "char": "DC1",
        "name": "Device control 1/xon"
    },
    {
        "char": "DC2",
        "name": "Device control 2"
    },
    {
        "char": "DC3",
        "name": "Device control 3/xoff"
    },
    {
        "char": "DC4",
        "name": "Device control 4"
    },
    {
        "char": "NAK",
        "name": "Negative acknowledgement"
    },
    {
        "char": "SYN",
        "name": "Synchronous idle"
    },
    {
        "char": "ETB",
        "name": "End transmission block"
    },
    {
        "char": "CAN",
        "name": "Cancel"
    },
    {
        "char": "EM",
        "name": "End of medium"
    },
    {
        "char": "SUB",
        "name": "Substitute"
    },
    {
        "char": "ESC",
        "name": "Escape"
    },
    {
        "char": "FS",
        "name": "File separator"
    },
    {
        "char": "GS",
        "name": "Group separator"
    },
    {
        "char": "RS",
        "name": "Record separator"
    },
    {
        "char": "US",
        "name": "Unit separator"
    },
    {
        "char": "SPACE",
        "name": "Space"
    },
    {
        "char": "!",
        "name": "Exclamation mark"
    },
    {
        "char": "\"",
        "name": "Double quotes"
    },
    {
        "char": "#",
        "name": "Number/hash/pound"
    },
    {
        "char": "$",
        "name": "Dollar"
    },
    {
        "char": "%",
        "name": "Percent"
    },
    {
        "char": "&",
        "name": "Ampersand"
    },
    {
        "char": "'",
        "name": "Single quote"
    },
    {
        "char": "(",
        "name": "Open parenthesis"
    },
    {
        "char": ")",
        "name": "Close parenthesis"
    },
    {
        "char": "*",
        "name": "Asterisk"
    },
    {
        "char": "+",
        "name": "Plus"
    },
    {
        "char": ",",
        "name": "Comma"
    },
    {
        "char": "-",
        "name": "Minus/dash"
    },
    {
        "char": ".",
        "name": "Period"
    },
    {
        "char": "/",
        "name": "Divide/forward slash"
    },
    {
        "char": "0",
        "name": "Zero"
    },
    {
        "char": "1",
        "name": "One"
    },
    {
        "char": "2",
        "name": "Two"
    },
    {
        "char": "3",
        "name": "Three"
    },
    {
        "char": "4",
        "name": "Four"
    },
    {
        "char": "5",
        "name": "Five"
    },
    {
        "char": "6",
        "name": "Six"
    },
    {
        "char": "7",
        "name": "Seven"
    },
    {
        "char": "8",
        "name": "Eight"
    },
    {
        "char": "9",
        "name": "Nine"
    },
    {
        "char": ":",
        "name": "Colon"
    },
    {
        "char": ";",
        "name": "Semicolon"
    },
    {
        "char": "<",
        "name": "Less than"
    },
    {
        "char": "=",
        "name": "Equals"
    },
    {
        "char": ">",
        "name": "Greater than"
    },
    {
        "char": "?",
        "name": "Question mark"
    },
    {
        "char": "@",
        "name": "At"
    },
    {
        "char": "A",
        "name": "Uppercase A"
    },
    {
        "char": "B",
        "name": "Uppercase B"
    },
    {
        "char": "C",
        "name": "Uppercase C"
    },
    {
        "char": "D",
        "name": "Uppercase D"
    },
    {
        "char": "E",
        "name": "Uppercase E"
    },
    {
        "char": "F",
        "name": "Uppercase F"
    },
    {
        "char": "G",
        "name": "Uppercase G"
    },
    {
        "char": "H",
        "name": "Uppercase H"
    },
    {
        "char": "I",
        "name": "Uppercase I"
    },
    {
        "char": "J",
        "name": "Uppercase J"
    },
    {
        "char": "K",
        "name": "Uppercase K"
    },
    {
        "char": "L",
        "name": "Uppercase L"
    },
    {
        "char": "M",
        "name": "Uppercase M"
    },
    {
        "char": "N",
        "name": "Uppercase N"
    },
    {
        "char": "O",
        "name": "Uppercase O"
    },
    {
        "char": "P",
        "name": "Uppercase P"
    },
    {
        "char": "Q",
        "name": "Uppercase Q"
    },
    {
        "char": "R",
        "name": "Uppercase R"
    },
    {
        "char": "S",
        "name": "Uppercase S"
    },
    {
        "char": "T",
        "name": "Uppercase T"
    },
    {
        "char": "U",
        "name": "Uppercase U"
    },
    {
        "char": "V",
        "name": "Uppercase V"
    },
    {
        "char": "W",
        "name": "Uppercase W"
    },
    {
        "char": "X",
        "name": "Uppercase X"
    },
    {
        "char": "Y",
        "name": "Uppercase Y"
    },
    {
        "char": "Z",
        "name": "Uppercase Z"
    },
    {
        "char": "[",
        "name": "Open bracket"
    },
    {
        "char": "\\",
        "name": "Backslash"
    },
    {
        "char": "]",
        "name": "Close bracket"
    },
    {
        "char": "^",
        "name": "Caret"
    },
    {
        "char": "_",
        "name": "Underscore"
    },
    {
        "char": "`",
        "name": "Backtick"
    },
    {
        "char": "a",
        "name": "Lowercase a"
    },
    {
        "char": "b",
        "name": "Lowercase b"
    },
    {
        "char": "c",
        "name": "Lowercase c"
    },
    {
        "char": "d",
        "name": "Lowercase d"
    },
    {
        "char": "e",
        "name": "Lowercase e"
    },
    {
        "char": "f",
        "name": "Lowercase f"
    },
    {
        "char": "g",
        "name": "Lowercase g"
    },
    {
        "char": "h",
        "name": "Lowercase h"
    },
    {
        "char": "i",
        "name": "Lowercase i"
    },
    {
        "char": "j",
        "name": "Lowercase j"
    },
    {
        "char": "k",
        "name": "Lowercase k"
    },
    {
        "char": "l",
        "name": "Lowercase l"
    },
    {
        "char": "m",
        "name": "Lowercase m"
    },
    {
        "char": "n",
        "name": "Lowercase n"
    },
    {
        "char": "o",
        "name": "Lowercase o"
    },
    {
        "char": "p",
        "name": "Lowercase p"
    },
    {
        "char": "q",
        "name": "Lowercase q"
    },
    {
        "char": "r",
        "name": "Lowercase r"
    },
    {
        "char": "s",
        "name": "Lowercase s"
    },
    {
        "char": "t",
        "name": "Lowercase t"
    },
    {
        "char": "u",
        "name": "Lowercase u"
    },
    {
        "char": "v",
        "name": "Lowercase v"
    },
    {
        "char": "w",
        "name": "Lowercase w"
    },
    {
        "char": "x",
        "name": "Lowercase x"
    },
    {
        "char": "y",
        "name": "Lowercase y"
    },
    {
        "char": "z",
        "name": "Lowercase z"
    },
    {
        "char": "{",
        "name": "Open brace"
    },
    {
        "char": "|",
        "name": "Vertical bar"
    },
    {
        "char": "}",
        "name": "Close brace"
    },
    {
        "char": "~",
        "name": "Tilde"
    },
    {
        "char": "DEL",
        "name": "Delete"
    }
]