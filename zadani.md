
## 🧪 Test – Node-RED02 + Git + práce s API

### 1) Stažení a příprava

1. Stáhni repozitář:
   [https://github.com/mathes2/NodeRED02](https://github.com/mathes2/NodeRED02)
2. Importuj přiložený flow.json do Node-RED.
3. Po úspěšném importu pořiď screenshot **`screenshot01.png`**, na kterém bude viditelné celé flow.
4. Proveď **1. commit** (soubor musí být součástí repozitáře).

---

### 2) Zjištění IP adresy

1. Zjisti svou IP adresu (v lokální síti).
2. Pořiď screenshot **`screenshot02.png`**, na kterém bude IP adresa jasně čitelná.
3. Proveď **2. commit**.

---

### 3) Úprava zdroje dat

1. Podle své IP adresy najdi odpovídající `st_id` v tabulce.

```
+-------------------+-------+------------------------+-------------+-------------+
| ip                | st_id | nazev                  | 1.velicina  | 2.velicina  |
+-------------------+-------+------------------------+-------------+-------------+
| 192.168.135.13    | 11406 | Cheb                   | F           | D           |
| 192.168.135.14    | 11414 | Karlovy Vary           | P           | T           |
| 192.168.135.15    | 11423 | Přimda                 | H           | T           |
| 192.168.135.16    | 11433 | Kopisty                | F           | D           |
| 192.168.135.17    | 11438 | Tušimice               | P           | T           |
| 192.168.135.18    | 11450 | Plzeň-Mikulka          | H           | T           |
| 192.168.135.19    | 11457 | Churáňov               | F           | D           |
| 192.168.135.20    | 11464 | Milešovka              | P           | T           |
| 192.168.135.21    | 11487 | Kocelovice             | H           | T           |
| 192.168.135.22    | 11502 | Ústí nad Labem         | F           | D           |
| 192.168.135.23    | 11509 | Doksany                | P           | T           |
| 192.168.135.24    | 11518 | Praha-Ruzyně           | H           | T           |
| 192.168.135.25    | 11519 | Praha-Karlov           | F           | D           |
| 192.168.135.26    | 11520 | Praha-Libuš            | P           | T           |
| 192.168.135.27    | 11538 | Temelín                | H           | T           |
| 192.168.135.28    | 11546 | České Budějovice       | F           | D           |
| 192.168.135.29    | 11567 | Praha-Kbely            | P           | T           |
| 192.168.135.30    | 11603 | Liberec                | H           | T           |
| 192.168.135.31    | 11609 | Jičín                  | F           | D           |
| 192.168.135.32    | 11624 | Čáslav                 | P           | T           |
| 192.168.135.33    | 11628 | Košetice               | H           | T           |
| 192.168.135.34    | 11636 | Kostelní Myslová       | F           | D           |
| 192.168.135.35    | 11643 | Pec pod Sněžkou        | P           | T           |
| 192.168.135.36    | 11652 | Pardubice              | H           | T           |
| 192.168.135.37    | 11659 | Přibyslav              | F           | D           |
| 192.168.135.38    | 11669 | Polom                  | P           | T           |
| 192.168.135.39    | 11679 | Ústí nad Orlicí        | H           | T           |
| 192.168.135.40    | 11683 | Svratouch              | F           | D           |
| 192.168.135.41    | 11692 | Náměšť nad Oslavou     | P           | T           |
| 192.168.135.42    | 11693 | Dukovany               | H           | T           |
| 192.168.135.43    | 11698 | Kuchařovice            | F           | D           |
| 192.168.135.44    | 11710 | Luká                   | P           | T           |
| 192.168.135.45    | 11723 | Brno-Tuřany            | H           | T           |
| 192.168.135.46    | 11730 | Šerák                  | F           | D           |
| 192.168.135.47    | 11747 | Prostějov              | P           | T           |
| 192.168.135.48    | 11766 | Červená u Libavé       | H           | T           |
| 192.168.135.49    | 11774 | Holešov                | F           | D           |
| 192.168.135.50    | 11782 | Ostrava-Mošnov         | P           | T           |
| 192.168.135.51    | 11787 | Lysá hora              | H           | T           |
| 192.168.135.52    | 11791 | Maruška                | F           | D           |
+-------------------+-------+------------------------+-------------+-------------+
```

2. Uprav URL v HTTP request node podle zjištěného st_id:

---

### 4) Nastavení debug výstupů

1. Podle své IP adresy zjisti v tabulce své:

   * **1. velicina**
   * **2. velicina**
2. Ve flow:

   * připoj **debug node** pouze na odpovídající výstupy function node pro **1.velicina** a **2.velicina**
   * jiné výstupy nesmí být připojeny
3. Spusť flow a otevři debug panel.
4. Ověř, že se zobrazují **pouze tvoje dvě přidělené veličiny**.

---

### 5) Dokumentace výsledku

1. Pořiď jeden screenshot **`screenshot03.png`**, na kterém bude současně vidět:

   * upravené flow (včetně zapojených debug node)
   * debug panel s přicházejícími daty (zprávy o hodnotách veličin ve formátu json)
2. Proveď **3. commit**.

---

### 6) Export flow

1. Exportuj flow do souboru **`myflow.json`**.
2. Soubor ulož do repozitáře.
3. Proveď **4. commit**.

---

### 7) Odevzdání

1. Nahraj repozitář na GitHub.
2. Do svého adresáře na sdíleném disku ulož **odkaz na repozitář**.

---

# 📊 Hodnocení (striktní podmínky)

## Povinné soubory

Repozitář musí obsahovat:

* `screenshot01.png`
* `screenshot02.png`
* `screenshot03.png`
* `myflow.json`

---

## Screenshoty – přesné požadavky

### screenshot01.png

* musí obsahovat celé flow
* musí odpovídat původnímu (neupravenému) stavu

### screenshot02.png

* musí obsahovat IP adresu
* IP musí být čitelná
* nesmí být ručně dopsaná nebo upravená

### screenshot03.png

* musí obsahovat:

  * upravené flow
  * zapojené debug nody
  * debug panel s daty
* musí být vidět **obě správné veličiny**
* nesmí obsahovat jiné veličiny

---

## Flow (myflow.json)

* musí obsahovat:

  * správné `st_id` podle IP
  * správně zapojené debug nody
* nesmí obsahovat:

  * debug nody na jiných výstupech
  * nefunkční nebo nepropojené části

---

## Git – povinné požadavky

* minimálně **4 commity**:

  1. import flow + screenshot01
  2. IP + screenshot02
  3. debug + screenshot03
  4. export myflow.json
* commity musí dávat smysl (chronologicky odpovídat postupu práce)


---

# 📊 Bodovací tabulka (max. 20 bodů)

| Oblast                  | Požadavek                                                        | Body |
| ----------------------- | ---------------------------------------------------------------- | ---- |
| **1. Import flow**      | `screenshot01.png` – kompletní, čitelný, odpovídá původnímu flow | 2    |
| **2. IP adresa**        | `screenshot02.png` – IP jasně čitelná a reálná                   | 2    |
| **3. Úprava API**       | správně nastavené `st_id` podle IP                               | 3    |
| **4. Debug – zapojení** | připojeny **pouze správné 2 výstupy**                            | 3    |
| **5. Debug – data**     | v debug okně se zobrazují správné veličiny                       | 3    |
| **6. screenshot03**     | obsahuje flow + debug + správná data                             | 3    |
| **7. Export**           | `myflow.json` existuje a odpovídá řešení                         | 2    |
| **8. Git commity**      | min. 4 logické commity ve správném pořadí                        | 2    |

**Celkem: 20 bodů**


# 📊 Převod bodů na známku

| Body    | Známka               |
| ------- | -------------------- |
| 18 – 20 | **1 (výborný)**      |
| 15 – 17 | **2 (chvalitebný)**  |
| 12 – 14 | **3 (dobrý)**        |
| 9 – 11  | **4 (dostatečný)**   |
| 0 – 8   | **5 (nedostatečný)** |
