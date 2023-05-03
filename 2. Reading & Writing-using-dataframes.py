import pandas as pd

# writing data to a new excel file
df = pd.DataFrame({'States': ['California', 'Florida', 'Montana', 'Colorado', 'Washington', 'Virginia'],
                   'Capitals': ['Sacramento', 'Tallahassee', 'Helena', 'Denver', 'Olympia', 'Richmond'],
                   'Population': [508529, 193551, 32315, 619968, 52555, 227032]})

df.to_excel('./states.xlsx', sheet_name='States', index=False)

# reading data from an existing xlsx file

states = pd.read_excel('./states.xlsx', sheet_name='States')
print(states.head())
