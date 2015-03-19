# zse
python kod za parsiranje svih povijesnih podataka sa zagrebacke burze

skripte su rasporedene u dva foldera. u jednom je skripta koja dohvaca sve dionice na zagrebackoj burzi i sve podatke trgovanja koje su ikada zabiljezene za svaku dionicu

u drugom folderu je skripta cija je namjena svakodnevno parsiranje skupa dionica ( crobex index) i ubacivanje u mongo bazu podatka. skripta je radena za debian server na koji bi se svaki dan podaci sami azurirali buduci da bi skripta bila cron job
