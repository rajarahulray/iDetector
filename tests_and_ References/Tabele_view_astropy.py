from astropy.table import Table, Column

t = Table()
t['a'] = [1, 4]
t['b'] = Column([2.0, 5.0], unit='cm', description='Velocity')
t['c'] = ['x', 'y']

print(t);
