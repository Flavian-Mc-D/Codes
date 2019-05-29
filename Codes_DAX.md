Dax lenguagem principal do PowerBI e powerQuery 

Lista com tudos os codigos DAX:

 [dax](https://dax.guide/)

Lista solta de codes que tem sido usados no projeto Natura por enquanto. 

1. Calendario:

Calendario = 
ADDCOLUMNS (
CALENDAR (DATE(2019;01;01); DATE(2019;12;31));
"DateAsInteger"; FORMAT ( [Date]; "YYYYMMDD" );
"Year"; YEAR ( [Date] );
"Monthnumber"; FORMAT ( [Date]; "MM" );
"YearMonthnumber"; FORMAT ( [Date]; "YYYY/MM" );
"YearMonthShort"; FORMAT ( [Date]; "YYYY/mmm" );
"MonthNameShort"; FORMAT ( [Date]; "mmm" );
"MonthNameLong"; FORMAT ( [Date]; "MMMM" );
"DayOfWeekNumber"; WEEKDAY ( [Date] );
"DayOfWeek"; FORMAT ( [Date]; "dddd" );
"DayOfWeekShort"; FORMAT ( [Date]; "ddd" );
"Dia"; format ([date]; "dd"))




