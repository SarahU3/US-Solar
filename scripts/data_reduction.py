def state_data_source(statename):
    state_df = county_df[county_df.state_name == statename]
    dfs = GeoJSONDataSource(geojson=state_df.to_json())
    return dfs
