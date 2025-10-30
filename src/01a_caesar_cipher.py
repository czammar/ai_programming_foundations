"""
A dummy implementation of Caesar Cypher
"""

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def caesar_cypher(message: str, displacement: int = 2) -> str:
    """
    Crea un cifrado cesar de una palabra desplazandose cierta cantidad
    de caracteres.
    """
    translated = ''
    key = displacement

    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)
            translated_index = (symbol_index + key) % len(SYMBOLS)
            if translated_index < 0:
                translated_index = translated_index + len(SYMBOLS)
            translated = translated + SYMBOLS[translated_index]
        else:
            translated = translated + symbol

    return translated


encrypted_messages = [
    "UymsuzqImxxI6tqI2q12xqIxu8uzsIxurqIuzI2qmoq",
    "JnVVk2cZbV2YfeVp,2bRidR2Zj2R2TRk52GliiZeX2Ze2dp2cRg2'TRljV2Zk2cfmVj2dV52 cVoZeX2cZbV2R2XfUURde2RTifSRk52DV2ReU2bRidR2mZSV2cZbV2kYRk",
    "Pwpec?ug?gu?vcp?xkglq?eqoq?rctc?dcknct?wp?wnvkoq?tqem?&?tqnn",
    "a8  84Vi4z?V8DV?.EV!JV .G4ClJV58CDEV .G4V1C.04V!JV74zCEV5.CVE74V58CDEVE8!4,Vaz1J,V1z1J,V1z1J,V.7Vk804V1z1J,V1z1J,V1z1J,V?.",
    "d1.1Sy 91ASB41SAC0,Sw0zSeSAwGS5B’ASw88S.534B",
    "KagwWZaiw9'YwefUXXwefMZPUZSwNQffQdwfTMZw9wQhQdwPUPw!aaWUZSwXUWQwMwfdgQwegdhUhad,wRQQXUZSwXUWQwMwXUffXQwWUPw9'YwefUXXwefMZPUZSwMRfQdwMXXwfTUewfUYQ"
]