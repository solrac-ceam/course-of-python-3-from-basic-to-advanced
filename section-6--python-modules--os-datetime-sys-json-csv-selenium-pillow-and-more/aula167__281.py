# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps

import calendar
import locale

locale.setlocale(locale.LC_ALL, '')  # Define o locale para o sistema atual

print(locale.getlocale())  # Obtém o locale atual

print(calendar.calendar(2022))  # Exibe o calendário completo do ano de 2022
