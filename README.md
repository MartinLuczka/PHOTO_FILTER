# PHOTO FILTER

Aplikace sloužící k úpravě fotek pomocí zajímavého barevného uspořádání. Aplikace slouží jako podklad pro výuku funkcí v Pythonu. Výuka Pythonu probíhá v rámci předmětu Programování na SPŠEOL ve třetím ročníku.

- Filtr může kdokoliv volně využít a upravit si ho podle sebe.

- Pokud chcete filtr pouze vyzkoušet, tak můžeme volit ze 3 obrázků, které jsou součástí tohoto repozitáře.

## Jak filtr použít?

1) Stáhnětě si ZIP z repozitáře na GitHubu.

2) Tento ZIP si extrahujte do Vámi zvolené složky.

3) Zdrojový kód programu se jmenuje: photo_filter.py

4) Stáhněte/Spustťe si program, ve kterém můžete kód spusit a zadat svou fotku. Popřípadě si kód můžete vyzkoušet v nějakém online prostředí skrze internetové připojení.
Fotku mějte asi nejlépe přímo ve složce, ve které máte soubory repozitáře. Nebo jen vyzkoušejte program s obrázkem *oblicej.png*, popřípadě s jiným na výběr.

> [!CAUTION]
> Při zadávání cesty svého vlastního obrázku si dávejte pozor na jeho umístěný. Pro správnou funkci se musí uvést korektní místo umístění.

5) V případě chyby doinstalujte potřebná rozšíření či knihovny.

V našem případě budeme pravděpodobně muset doinstalovat knihovnu PIL/Pillow.

Pro nainstalování knihovny si otevřete terminál, popřípadě příkazový řádek. **Zadejte do nich tento příkaz:**

```python
pip install pillow
```

## Funkce aplikace

### Úvod do aplikace

Před spuštěním uživatel musí přepsat/ponechat zdroj obrázku, se kterým aplikace bude následně pracovat.

### Jednotlivé filtry

1) Na fotku aplikuje předdefinovanou paletu barev č.1

2) Na fotku aplikuje předdefinovanou paletu barev č.2

3) Na fotku aplikuje předdefinovanou paletu barev č.3

4) Na fotku aplikuje černobílý filtr

5) Na fotku aplikuje negativní filtr (změna všech barev do jiné)

6) Fotka zežloutnutím "zestárne"

7) Fotka se rozostří

8) Fotka bude působit jako nakreslená křídou na černou tabuli

9) Části fotky se změní na náhodnou barvu, filtr bude při každém použitím používat jinou paletu barev

10) Fotka se zpixelizuje (Minecraft effect :D)

11) Filtr fotku zesvětlí

12) Fotce se zvýší saturace a kontrast (hodí se jako kombinace k ostatním filtrům)

13) Filtr fotku ztmaví

14) Tato volba uživatele dostane do prostředí, ve kterém bude moct nakombinovat na jeden obrázek více filtrů najednou. Exportovat budete moct po 2 a více aplikovaných filtrech.

### Ukončení

Aplikaci můžeme při volbě filtru ukončit zadáním čísla **15** do terminálu. Mix filtrů (volba číslo 14) jde ukončit velice podobně.

### Export obrázku

Po výběru filtru aplikace uživatelovi zobrazí výsledek jeho volby. Upravený obrázek si uživatel může uložit a také pojmenovat podle sebe.

## Kontakt

Pro případné chyby či připomínky se mě nebojte kontaktovat.

E-mail: *luczka.martin@gmail.com*

**Martin Luczka**