# zse

skripte su raspoređene u dva foldera. u jednom je skripta koja dohvaca sve dionice na zagrebackoj burzi i sve podatke trgovanja koje su ikada zabiljezene za svaku dionicu i daje output kao csv file.

u drugom folderu je skripta čija je namjena svakodnevno parsiranje skupa dionica (crobex index) i ubacivanje csv outputa u mongo bazu podatka. skripta je rađena za debian server na koji bi se svaki dan podaci sami ažurirali kad se na serveru namjesti cron job.
