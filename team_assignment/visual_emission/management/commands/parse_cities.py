import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from openpyxl import load_workbook

from visual_emission.models import Country, Data # load the models

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):
        Country.objects.all().delete()
        Data.objects.all().delete()
        print('table dropped')

        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        book_path = os.path.join(base_dir, 'visual_emission/country_data/data_upload.xlsx')
        book = load_workbook(book_path)
        sheet = book['Data']
        print(sheet.title)
        max_row_num = sheet.max_row
        max_col_num = sheet.max_column
        print(max_row_num)
        print(max_col_num)

        # placeholder variables for objects
        c_name = 'country_name'
        c_code = 'code'
        is_c = True
        reg = ''
        income = ''
        year_90 = 0.0
        year_91 = 0.0
        year_92 = 0.0
        year_93 = 0.0
        year_94 = 0.0
        year_95 = 0.0
        year_96 = 0.0
        year_97 = 0.0
        year_98 = 0.0
        year_99 = 0.0
        year_00 = 0.0
        year_01 = 0.0
        year_02 = 0.0
        year_03 = 0.0
        year_04 = 0.0
        year_05 = 0.0
        year_06 = 0.0
        year_07 = 0.0
        year_08 = 0.0
        year_09 = 0.0
        year_10 = 0.0
        year_11 = 0.0
        year_12 = 0.0
        year_13 = 0.0
        year_14 = 0.0
        year_15 = 0.0
        year_16 = 0.0
        year_17 = 0.0
        year_18 = 0.0
        year_19 = 0.0
        year_20 = 0.0

        for i in range(2, max_row_num+1):
            for j in range(1, max_col_num+1):
                cell_obj = sheet.cell(row=i, column=j)

                if cell_obj.column_letter == 'A':
                    c_name = cell_obj.value
                if cell_obj.column_letter == 'B':
                    c_code = cell_obj.value
                if cell_obj.column_letter == 'C':
                    is_c = cell_obj.value
                if cell_obj.column_letter == 'D':
                    if cell_obj.value is not None:
                        reg = cell_obj.value
                if cell_obj.column_letter == 'E':
                    if cell_obj.value is not None:
                        income = cell_obj.value
                if cell_obj.column_letter == 'F':
                    if cell_obj.value is not None:
                        year_90 = cell_obj.value
                if cell_obj.column_letter == 'G':
                    if cell_obj.value is not None:
                        year_91 = cell_obj.value
                if cell_obj.column_letter == 'H':
                    if cell_obj.value is not None:
                        year_92 = cell_obj.value
                if cell_obj.column_letter == 'I':
                    if cell_obj.value is not None:
                        year_93 = cell_obj.value
                if cell_obj.column_letter == 'J':
                    if cell_obj.value is not None:
                        year_94 = cell_obj.value
                if cell_obj.column_letter == 'K':
                    if cell_obj.value is not None:
                        year_95 = cell_obj.value
                if cell_obj.column_letter == 'L':
                    if cell_obj.value is not None:
                        year_96 = cell_obj.value
                if cell_obj.column_letter == 'M':
                    if cell_obj.value is not None:
                        year_97 = cell_obj.value
                if cell_obj.column_letter == 'N':
                    if cell_obj.value is not None:
                        year_98 = cell_obj.value
                if cell_obj.column_letter == 'O':
                    if cell_obj.value is not None:
                        year_99 = cell_obj.value
                if cell_obj.column_letter == 'P':
                    if cell_obj.value is not None:
                        year_00 = cell_obj.value
                if cell_obj.column_letter == 'Q':
                    if cell_obj.value is not None:
                        year_01 = cell_obj.value
                if cell_obj.column_letter == 'R':
                    if cell_obj.value is not None:
                        year_02 = cell_obj.value
                if cell_obj.column_letter == 'S':
                    if cell_obj.value is not None:
                        year_03 = cell_obj.value
                if cell_obj.column_letter == 'T':
                    if cell_obj.value is not None:
                        year_04 = cell_obj.value
                if cell_obj.column_letter == 'U':
                    if cell_obj.value is not None:
                        year_05 = cell_obj.value
                if cell_obj.column_letter == 'V':
                    if cell_obj.value is not None:
                        year_06 = cell_obj.value
                if cell_obj.column_letter == 'W':
                    if cell_obj.value is not None:
                        year_07 = cell_obj.value
                if cell_obj.column_letter == 'X':
                    if cell_obj.value is not None:
                        year_08 = cell_obj.value
                if cell_obj.column_letter == 'Y':
                    if cell_obj.value is not None:
                        year_09 = cell_obj.value
                if cell_obj.column_letter == 'Z':
                    if cell_obj.value is not None:
                        year_10 = cell_obj.value
                if cell_obj.column_letter == 'AA':
                    if cell_obj.value is not None:
                        year_11 = cell_obj.value
                if cell_obj.column_letter == 'AB':
                    if cell_obj.value is not None:
                        year_12 = cell_obj.value
                if cell_obj.column_letter == 'AC':
                    if cell_obj.value is not None:
                        year_13 = cell_obj.value
                if cell_obj.column_letter == 'AD':
                    if cell_obj.value is not None:
                        year_14 = cell_obj.value
                if cell_obj.column_letter == 'AE':
                    if cell_obj.value is not None:
                        year_15 = cell_obj.value
                if cell_obj.column_letter == 'AF':
                    if cell_obj.value is not None:
                        year_16 = cell_obj.value
                if cell_obj.column_letter == 'AG':
                    if cell_obj.value is not None:
                        year_17 = cell_obj.value
                if cell_obj.column_letter == 'AH':
                    if cell_obj.value is not None:
                        year_18 = cell_obj.value
                if cell_obj.column_letter == 'AI':
                    if cell_obj.value is not None:
                        year_19 = cell_obj.value
                if cell_obj.column_letter == 'AJ':
                    if cell_obj.value is not None:
                        year_20 = cell_obj.value
                
                print(cell_obj.value, end='|')
            #finish getting values in one row
            country = Country.objects.create(
                country_name = c_name,
                country_code = c_code,
                is_country = is_c,
                region = reg,
                income_group = income,
            )
            
            data_1 = Data.objects.create(country = country, year = 1990, emission = year_90)
            data_2 = Data.objects.create(country = country, year = 1991, emission = year_91)
            data_3 = Data.objects.create(country = country, year = 1992, emission = year_92)
            data_4 = Data.objects.create(country = country, year = 1993, emission = year_93)
            data_5 = Data.objects.create(country = country, year = 1994, emission = year_94)
            data_6 = Data.objects.create(country = country, year = 1995, emission = year_95)
            data_7 = Data.objects.create(country = country, year = 1996, emission = year_96)
            data_8 = Data.objects.create(country = country, year = 1997, emission = year_97)
            data_9 = Data.objects.create(country = country, year = 1998, emission = year_98)
            data_10 = Data.objects.create(country = country, year = 1999, emission = year_99)
            data_11 = Data.objects.create(country = country, year = 2000, emission = year_00)
            data_12 = Data.objects.create(country = country, year = 2001, emission = year_01)
            data_13 = Data.objects.create(country = country, year = 2002, emission = year_02)
            data_14 = Data.objects.create(country = country, year = 2003, emission = year_03)
            data_15 = Data.objects.create(country = country, year = 2004, emission = year_04)
            data_16 = Data.objects.create(country = country, year = 2005, emission = year_05)
            data_17 = Data.objects.create(country = country, year = 2006, emission = year_06)
            data_18 = Data.objects.create(country = country, year = 2007, emission = year_07)
            data_19 = Data.objects.create(country = country, year = 2008, emission = year_08)
            data_20 = Data.objects.create(country = country, year = 2009, emission = year_09)
            data_21 = Data.objects.create(country = country, year = 2010, emission = year_10)
            data_22 = Data.objects.create(country = country, year = 2011, emission = year_11)
            data_23 = Data.objects.create(country = country, year = 2012, emission = year_12)
            data_24 = Data.objects.create(country = country, year = 2013, emission = year_13)
            data_25 = Data.objects.create(country = country, year = 2014, emission = year_14)
            data_26 = Data.objects.create(country = country, year = 2015, emission = year_15)
            data_27 = Data.objects.create(country = country, year = 2016, emission = year_16)
            data_28 = Data.objects.create(country = country, year = 2017, emission = year_17)
            data_29 = Data.objects.create(country = country, year = 2018, emission = year_18)
            data_30 = Data.objects.create(country = country, year = 2019, emission = year_19)
            data_31 = Data.objects.create(country = country, year = 2020, emission = year_20)
            print(' saved ')
            print('\n')