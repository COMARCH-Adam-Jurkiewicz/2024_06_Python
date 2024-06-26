"""
Pola:

values=['ROK', 'MIESIAC', 'TYDZIEN', 'DZIEN', 'OMNICODE_ORDER',
 'OMNICODE_BUNDLE', 'ID_RODZ_REALIZACJI', 'DATA_KONCA_PROCESU',
  'MIESIAC_DORECZENIA', 'TYDZIEN_DORECZENIA', 'STARY_PLAN',
  'TYP_PROCESU', 'SLOWNIK_TYP_PROCESU', 'USER_ID', 'KOD_BSCS',
  'NAZWA_NOWY_RATEPLAN', 'ID_OFERTY', 'NAZWA_OFERTY',
  'ID_ANEKSU', 'TYP_OFERTY', 'KANAL_SPRZEDAZY', 'LINK_EUMOWA',
  'STATUS_UMOWY', 'DATA_STATUS_UMOWY', 'STATUS_TOWAR',
  'DATA_STATUS_TOWAR', 'DATA_BUNDLE', 'ID_KOLEJKI',
  'WYNIK_WERYF_RECZNEJ_STATUS', 'KOD_WERYF_RECZNEJ_POWOD',
  'WYNIK_WERYFIKACJI_CV', 'ID_KOMUNIKATU_Z_CV_DO_SALES',
  'STATUS_ZAMOWIENIA', 'STATUS_BANDLA', 'NAZWA_OFERTY_CV',
  'NAZWA_PROMOCJI', 'PLAN_TARYFOWY', 'KWOTA_ABONAMENTU',
  'NAZWA_TERMINALA', 'CENA_TERMINALA', 'KANAL_SPRZEDAZY_SIS',
  'KANAL_SPRZEDAZY_SZCCZEGOLOWY_SIS', 'RATY', 'ML_STATUS',
  'ML_DATA_STATUSU', 'ML_OPISBLEDU', 'ML_KOD_KURIERA',
  'OPIS_KODU', 'KOD_ZWROTU', 'POWOD_ZWROTU', 'ID_PRODUKTU',
  'OSTAT_DATA_MODYF', 'STATUS_CRM_USLUGI',
  'DATA_KONCA_PROMOCJI', 'STATUS_NEW', 'STATUS_ZALICZENIOWY',
  'RYNEK', 'ILE_POWODOW', 'WYNIK_KOMUNIKATU_Z_CV_DO_SALES',
   'MAPOWANIE_DO_RAPORTU', 'IS_TEST', 'TYP_OFERTY_PLANY',
   'TYP_PRODUKTU_PLANY', 'TYP_SIM', 'E_REGULAMINY',
   'ID_PACZKI', 'STATUS_PICKUP', 'DATA_STATUS_PICKUP',
   'LOGIN_OTSA_PICKUP', 'SHORT_BSCS_PICKUP', 'STATUS_SAP',
   'DATA_STATUS_SAP', 'LOGIN_OTSA_SAP', 'SHORT_BSCS_SAP',
   'PICKUP_ZATOW', 'PICKUP_ZATOW_DATA', 'PICKUP_SALON',
   'PICKUP_SIEC', 'REGION', 'DYSTRYKT', 'DANE_SPRZEDAWCY',
   'MANAGER', 'MANAGER_1', 'MANAGER_2', 'MANAGER_3',
   'LOKALIZACJA', 'AGENT', 'CZY_E_UMOWA', 'WARUNEK_DOSTEPU',
    'KURIER_PLATNY', 'METODA_PLATNOSCI', 'STATUS_PLATNOSCI',
    'KPI', 'FLAGA_RAID', 'FORMA_PRAWNA', 'SEGMENT',
    'SHELF_STOCKING', 'WPROWADZIL_W_IMIENIU_SPRZEDAWCY',
     'LOGIN_OTSA_SPZED_W_IMIENIU', 'FULL_BSCS_SPZED_W_IMIENIU',
      'CZY_W_IMIENIU', 'AGENT_PICKUP', 'OPLATA_NA_START',
      'OPLATA_KURIER', 'OPLATA_POBRANIE', 'KWOTA_KAUCJI',
       'LINK_Z_OFERTA', 'KOT_W_WORKU', 'NIP', 'FRAKCJA',
       'CZY_SENIOR', 'BAZA', 'PESEL']

"""

from time import time
from pyxlsb import open_workbook

t_start = time()
print(f"{t_start=}")
with open_workbook('test.xlsb') as wb:
    with wb.get_sheet("DANE") as sheet:
        for i, row in enumerate(sheet.rows()):
            values = [r.v for r in row]
            print(f"{values=}")
            if i > 2:
                break


t_xlsb = time()
print(f"{t_xlsb=} / {t_xlsb-t_start=}")

t_csv = time()
print(f"{t_csv=} / {t_csv-t_start=}")