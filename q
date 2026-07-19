[1mdiff --git a/holidays/financial/bolsas_y_mercados_espanoles.py b/holidays/financial/bolsas_y_mercados_espanoles.py[m
[1mindex 88f96ecd..1afc8e14 100644[m
[1m--- a/holidays/financial/bolsas_y_mercados_espanoles.py[m
[1m+++ b/holidays/financial/bolsas_y_mercados_espanoles.py[m
[36m@@ -70,8 +70,8 @@[m [mclass BolsasYMercadosEspanoles(ObservedHolidayBase, ChristianHolidays, Internati[m
         # Christmas Day.[m
         self._move_holiday(self._add_christmas_day(tr("Navidad")))[m
 [m
[31m-        # Saint Stephen's Day.[m
[31m-        self._move_holiday(self._add_christmas_day_two(tr("Boxing Day & San Esteban")))[m
[32m+[m[32m        # Saint Stephen's Day.[m
[32m+[m[32m        self._move_holiday(self._add_christmas_day_two(tr("San Esteban")))[m
 [m
     def _populate_half_day_holidays(self) -> None:[m
         # %s (markets close at 14:00 CET).[m
[1mdiff --git a/holidays/locale/en_US/LC_MESSAGES/XMAD.po b/holidays/locale/en_US/LC_MESSAGES/XMAD.po[m
[1mindex 23541a23..bdafd7f7 100644[m
[1m--- a/holidays/locale/en_US/LC_MESSAGES/XMAD.po[m
[1m+++ b/holidays/locale/en_US/LC_MESSAGES/XMAD.po[m
[36m@@ -47,9 +47,9 @@[m [mmsgstr "Labor Day"[m
 msgid "Navidad"[m
 msgstr "Christmas Day"[m
 [m
[31m-#. Saint Stephen's Day.[m
[31m-msgid "Boxing Day & San Esteban"[m
[31m-msgstr "Saint Stephen's Day"[m
[32m+[m[32m#. Saint Stephen's Day.[m
[32m+[m[32mmsgid "San Esteban"[m
[32m+[m[32mmsgstr "Saint Stephen's Day"[m
 [m
 #. %s (markets close at 14:00 CET).[m
 #, c-format[m
[1mdiff --git a/holidays/locale/es/LC_MESSAGES/XMAD.po b/holidays/locale/es/LC_MESSAGES/XMAD.po[m
[1mindex 74d4457f..093623af 100644[m
[1m--- a/holidays/locale/es/LC_MESSAGES/XMAD.po[m
[1m+++ b/holidays/locale/es/LC_MESSAGES/XMAD.po[m
[36m@@ -47,8 +47,8 @@[m [mmsgstr ""[m
 msgid "Navidad"[m
 msgstr ""[m
 [m
[31m-#. Saint Stephen's Day.[m
[31m-msgid "Boxing Day & San Esteban"[m
[32m+[m[32m#. Saint Stephen's Day.[m
[32m+[m[32mmsgid "San Esteban"[m
 msgstr ""[m
 [m
 #. %s (markets close at 14:00 CET).[m
[1mdiff --git a/tests/financial/test_bolsas_y_mercados_espanoles.py b/tests/financial/test_bolsas_y_mercados_espanoles.py[m
[1mindex ce21f2f4..df7718ed 100644[m
[1m--- a/tests/financial/test_bolsas_y_mercados_espanoles.py[m
[1m+++ b/tests/financial/test_bolsas_y_mercados_espanoles.py[m
[36m@@ -103,7 +103,7 @@[m [mclass TestBolsasYMercadosEspanoles(CommonFinancialTests, TestCase):[m
         )[m
 [m
     def test_boxing_day_and_san_esteban(self):[m
[31m-        name = "Boxing Day & San Esteban"[m
[32m+[m[32m        name = "San Esteban"[m
         self.assertNonObservedHolidayName(name, (f"{year}-12-26" for year in self.full_range))[m
         self.assertHolidayName([m
             name,[m
[36m@@ -168,7 +168,7 @@[m [mclass TestBolsasYMercadosEspanoles(CommonFinancialTests, TestCase):[m
             ("2025-04-21", "Lunes de Pascua"),[m
             ("2025-05-01", "Día del Trabajo"),[m
             ("2025-12-25", "Navidad"),[m
[31m-            ("2025-12-26", "Boxing Day & San Esteban"),[m
[32m+[m[32m            ("2025-12-26", "San Esteban"),[m
         )[m
 [m
     def test_half_day_2025(self):[m
[36m@@ -186,7 +186,7 @@[m [mclass TestBolsasYMercadosEspanoles(CommonFinancialTests, TestCase):[m
             ("2024-05-01", "Día del Trabajo"),[m
             ("2024-12-24", "Nochebuena (los mercados cierran a las 14:00 CET)"),[m
             ("2024-12-25", "Navidad"),[m
[31m-            ("2024-12-26", "Boxing Day & San Esteban"),[m
[32m+[m[32m            ("2024-12-26", "San Esteban"),[m
             ("2024-12-31", "Nochevieja (los mercados cierran a las 14:00 CET)"),[m
         )[m
 [m
[1mdiff --git a/tests/test_docs.py b/tests/test_docs.py[m
[1mindex 57f1168e..e29092d4 100644[m
[1m--- a/tests/test_docs.py[m
[1m+++ b/tests/test_docs.py[m
[36m@@ -252,7 +252,7 @@[m [mclass TestReadme(TestCase):[m
 [m
         # Parse 2nd table.[m
         table_content = self._parse_table(1)[m
[31m-        replace_chars = str.maketrans({" ": "", ",": "", "ã": "a"})[m
[32m+[m[32m        replace_chars = str.maketrans({" ": "", ",": "", "ã": "a", "ñ": "n"})[m
 [m
         for row in table_content:[m
             # Market: 1st column.[m
