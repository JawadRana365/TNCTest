from currency.models import CurrencyFaits
from table import Table
from table.columns import Column

class CurrencyFaitsTable(Table):
	id = Column(field='id',header="ID")
	name = Column(field='name',header="Name")
	clickable = {'class':'Row'}
	conversionFactor = Column(field='conversionFactor',header="Conversion Factor",attrs=clickable)
	fromcurrency = Column(field='fromcurrency',header="From Currency")
	tocurrency = Column(field='tocurrency',header="To Currency")
	class Meta:
		model = CurrencyFaits
