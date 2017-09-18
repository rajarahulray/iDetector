import plotly.plotly as py
import plotly.figure_factory as ff

data_matrix = [['Country', 'Year', 'Population'],
               ['United States', 2000, 282200000],
               ['Canada', 2000, 27790000],
               ['United States', 2005, 295500000],
               ['Canada', 2005, 32310000],
               ['United States', 2010, 309000000],
               ['Canada', 2010, 34000000]]

table = ff.create_table(data_matrix)
py.iplot(table, filename='simple_table')
