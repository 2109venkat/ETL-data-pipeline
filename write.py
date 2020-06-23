import process
from sqlalchemy import create_engine
engine = create_engine('postgresql://retail_user:venkatramasai@34.72.140.44:5432/retail_dw')
process.dim_products_df.to_sql('dim_products', engine, if_exists='replace',index=False)
process.dim_customers_df.to_sql('dim_customers',engine,if_exists='replace',index=False)
process.fact_product_revenue_dly_df.to_sql('fact_product_revenue_dly',engine,if_exists='replace',index=False)
process.fact_revenue_dly.to_sql('fact_revenue_dly',engine,if_exists='replace',index=False)
