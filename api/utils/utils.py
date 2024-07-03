import pandas as pd

# Carregar dados dos CSVs
audience_df = pd.read_csv('tvaberta_program_audience.csv', delimiter=';')
availability_df = pd.read_csv('tvaberta_inventory_availability.csv', delimiter=';')

# Converter colunas de datas para o tipo datetime
audience_df['exhibition_date'] = pd.to_datetime(audience_df['exhibition_date'])
availability_df['date'] = pd.to_datetime(availability_df['date'])

# Calcular o dia da semana
audience_df['weekday'] = audience_df['exhibition_date'].dt.dayofweek

# Função para calcular a mediana das últimas 4 audiências
def calculate_predicted_audience(group):
    return group.rolling(4, min_periods=1)['average_audience'].median().shift()

# Calcular a mediana para cada sinal, programa e dia da semana
audience_df['predicted_audience'] = (
    audience_df.sort_values('exhibition_date')
    .groupby(['signal', 'program_code', 'weekday'])
    .apply(calculate_predicted_audience)
    .reset_index(level=[0, 1, 2], drop=True)
)

# Unir os dados com o dataframe de disponibilidade de inventário
merged_df = pd.merge(
    availability_df,
    audience_df[['signal', 'program_code', 'weekday', 'predicted_audience']],
    left_on=['signal', 'program_code', 'date'],
    right_on=['signal', 'program_code', 'exhibition_date'],
    how='left'
)

# Salvar o dataframe resultante
merged_df.to_csv('preprocessed_data.csv', index=False)
