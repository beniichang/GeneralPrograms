''' This program was adapted from an online source '''
''' Serves as a good example of cleaning data in a concise way '''

def transform_data(df):

# select columns of interest
cols = ['Region', 'Var1', 'Age']

# return a clean DataFrame
return(df
      [cols]
      .dropna()
      .rename (columns = new_col_names)
      .assign(gender  = lambda x: x['gender'].str.split('\s+').str[1],
              age_group = lambda df: df['age_grp'].replace(new_age_cats),
              population = lambda x: x['population'].astype('int')
        )
        .query('gender != "Total" & age_group != "Total"')
        .groupby(['state', 'gender', 'age_group'])
        .agg(population = ('population', 'sum'))
        .reset_index()
)
